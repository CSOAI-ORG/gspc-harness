# Inspect Evals Register (Beta) — upstream requirements

For an upstream eval repo to be listed in the Register, the published
README requires:

1. pyproject.toml with [project] table (PEP 517)
2. inspect_ai declared as a dependency
3. each @task-decorated function exposed
4. external assets pinned in stable, version-controlled storage

Plus three submission-time items:

- arXiv paper URL
- GitHub blob URL pinned to a 40-character commit SHA
- two complete model-run log files