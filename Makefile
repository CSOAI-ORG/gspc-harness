# CSOAI M2 lane — Makefile
#
# One entry point for the master pipeline. Self-documenting via `make help`.
# Run from the repo root: `make` lists targets.
#
# All targets are idempotent. Targets that need `ots` say so in their recipe.

.PHONY: help audit stamp rebuild selfcheck verify pipeline clean

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
