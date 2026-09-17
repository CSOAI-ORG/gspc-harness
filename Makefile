# CSOAI M2 lane — Makefile
#
# One entry point for the master pipeline. Self-documenting via `make help`.
# Run from the repo root: `make` lists targets.
#
# All targets are idempotent. Targets that need `ots` say so in their recipe.

.PHONY: help audit stamp rebuild selfcheck verify pipeline clean stamp-age wait-ots revision health tui-a

# Allow `make BRANCH=foo` to override; default is the canonical lane branch.
BRANCH ?= hermes/inspect-register-readiness
SHELL := /bin/bash

help:
	@echo "CSOAI M2 lane - make targets:"
	@echo "  make audit       self-check the master (7 assertions)"
	@echo "  make stamp       anchor current bytes in OTS calendars (real CLI)"
	@echo "  make rebuild     reindex sha256 of every file in MASTER/"
	@echo "  make selfcheck   alias for audit"
	@echo "  make verify      full stamp -> rebuild -> selfcheck pipeline"
	@echo "  make pipeline    alias for verify"
	@echo "  make clean       remove stray worktrees + tmp dirs"
	@echo "  make stamp-age   print how old the OTS stamp is + hint whether to re-run"
	@echo "  make wait-ots    poll the master stamp until Bitcoin confirmation (or 1h timeout)"
	@echo "  make revision    print git HEAD + pipeline file SHAs + stamp state + age"
	@echo "  make health      run estate + master checks in one command (alias for tools/both.sh)"
	@echo "  make tui-a       print TUI A summary + operator decisions (reads partial_observations.json)"
	@echo
	@echo "Default branch: $(BRANCH)"
	@echo "Override: make BRANCH=foo audit"
	@echo
	@echo "OTS dependency: macOS brew install opentimestamps"

# Run a master script via the bootstrap export. Pattern: one bash -c that
# does eval + cd + exec. Avoids $() substitution pitfalls.
audit:
	@bash -c 'eval "$$(bash tools/bootstrap.sh --export)" && cd "$$REPO" && "$$PY" scripts/selfcheck_master.py'

stamp:
	@bash -c 'eval "$$(bash tools/bootstrap.sh --export)" && cd "$$REPO" && "$$PY" scripts/stamp_master_package.py'

rebuild:
	@bash -c 'eval "$$(bash tools/bootstrap.sh --export)" && cd "$$REPO" && "$$PY" scripts/rebuild_master_files.py'

selfcheck: audit

verify pipeline: stamp rebuild audit

stamp-age:
	@bash tools/stamp_age.sh

clean:
	@echo ">> cleaning stray worktrees under repo parent"
	@for wt in $$(ls -d ../tmp-hermes-wt-* 2>/dev/null); do \
		if [ -d "$$wt/.git" ]; then \
			git worktree remove --force "$$wt" 2>/dev/null || true; \
		fi; \
		rm -rf "$$wt"; \
	done
	@git worktree prune 2>/dev/null || true
	@echo ">> done"

# Default timeout: 1h. Override: make wait-ots WAIT_TIMEOUT=600 wait-ots
WAIT_TIMEOUT ?= 3600
WAIT_INTERVAL ?= 60
wait-ots:
	@bash tools/ots_wait_until_confirmed.sh \
		--root MASTER/MANIFEST.sha256 \
		--stamp MASTER/MASTER_PACKAGE.ots \
		--timeout $(WAIT_TIMEOUT) --interval $(WAIT_INTERVAL)

revision:
	@bash tools/master_revision.sh

# One-command health verdict: estate state (hermes-align) + master state
# (make verify). Pass --apply via env: HEALTH_APPLY=1 make health
HEALTH_APPLY ?=
health:
	@bash -c 'if [ -n "$(HEALTH_APPLY)" ]; then bash tools/both.sh --apply; else bash tools/both.sh; fi'

tui-a:
	@bash tools/tui_a_summary.sh
