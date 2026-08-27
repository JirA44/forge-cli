# forge-cli — Git Forge CLI (public)

3 outils en 1 binaire Python :

```bash
pip install -e .
forge ignore python,node,vscode -o .gitignore
forge stats ./mon-repo
forge rename ./photos --strip-accents --prefix 2026- --dry-run
forge rename ./src --regex " +\.py$" --replace ".py"
```

## Dev
```bash
pytest -q
forge --help
```

MIT — public Git ready.
