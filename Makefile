# Makefile — agentbench 任务入口（把散在 CLAUDE.md/TODO 的命令收敛成可发现的 target）。
# 约定:纯 Python(stdlib + pyyaml/jsonschema),无构建系统。数据层=schema/ + entries/。
# 详见 CLAUDE.md / docs/SOURCING.md。列出全部 target:make help

PY   := python3
PORT ?= 8000

.DEFAULT_GOAL := help
.PHONY: help install check check-schema coverage coverage-strict render serve site clean

help:  ## 列出所有 target
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
	  | awk 'BEGIN{FS=":.*?## "}{printf "  \033[36m%-16s\033[0m %s\n", $$1, $$2}'

install:  ## 安装依赖(pyyaml + jsonschema)
	pip install pyyaml jsonschema

check:  ## 发布门禁:逐条检查是否已签发(含 stale as_of 告警)
	$(PY) bin/check_publish.py

check-schema:  ## CI 硬门禁:只校验 schema(草稿放行,签字不阻断)
	$(PY) bin/check_publish.py --schema-only

coverage:  ## 覆盖体检:genre 分布 + 去医疗偏斜 + 年份谱(census,信息性)
	$(PY) bin/coverage_report.py

coverage-strict:  ## 覆盖体检(严格):有 thin genre / 医疗过偏则 exit 1
	$(PY) bin/coverage_report.py --strict

render:  ## 渲染静态站点到 site/(只渲染已签发条目)
	$(PY) bin/render_site.py

serve: render  ## 渲染后本地预览(http://localhost:$(PORT))
	$(PY) -m http.server $(PORT) -d site

site: render  ## render 的别名

clean:  ## 删除渲染产物 site/
	rm -rf site
