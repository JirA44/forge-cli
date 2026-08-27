# forge-cli

> **3 outils Git du quotidien en une CLI** — `pip install` et c'est prêt.

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-2%20passed-brightgreen)](#)

### En 1 ligne
```bash
pip install forge-cli
forge ignore python,node,vscode -o .gitignore
forge stats ./mon-repo
forge rename ./photos --strip-accents --prefix 2026_ --dry-run
```

---

## Présentation

**forge-cli** regroupe 3 commandes que tout dev tape à la main :

| Commande | À quoi ça sert ? | Exemple concret |
|---|---|---|
| `forge ignore` | Génère un `.gitignore` propre depuis [gitignore.io](https://www.toptal.com/developers/gitignore) | Nouveau projet Python+Node → `forge ignore python,node,macos` évite de committer `__pycache__`/`node_modules` |
| `forge stats` | Audit Git éclair (commits, fichiers, top auteurs) | Lead qui vérifie avant une soutenance : `forge stats D:/Code/mon-projet` |
| `forge rename` | Renommage masse (regex, préfixe, accents) | 500 photos `Café à Paris.jpg` → `2026_Cafe-a-Paris.jpg` en 1s |

**Pour qui ?** Étudiants, devs, ops — 0 config, 0 compte, 1 binaire Python.

---

## Installation

```bash
git clone https://github.com/JirA44/forge-cli
cd forge-cli
pip install -e .
forge --help
```

## Utilisation

### 1) `.gitignore` intelligent
```bash
# Python + VSCode
forge ignore python,vscode -o .gitignore

# Stack complète
forge ignore python,node,macos,windows,linux,vscode,jetbrains -o .gitignore

# Lister les templates disponibles → https://www.toptal.com/developers/gitignore
```

### 2) Stats Git
```bash
forge stats .
# Commits: 127  Auteurs: 4  Fichiers: 89
#   Alice                          72
#   Bob                            34

forge stats D:/Code/forge_portfolio/V1.07/proofforge
```

### 3) Renommage masse
```bash
# Dry-run d'abord (sécurité)
forge rename ./photos --strip-accents --dry-run
forge rename ./photos --strip-accents --prefix 2026_

# Regex: .jpeg → .jpg
forge rename ./images --regex "\.jpeg$" --replace ".jpg"

# Espaces → tirets
forge rename ./docs --regex " " --replace "-"

# Combiner
forge rename ./vacances --strip-accents --regex " " --replace "-" --prefix trip_
```

---

## Exemples d'usage (cas réels)

- **Nouveau repo** : `forge ignore python` avant le premier `git commit`
- **Audit pédagogique** : `forge stats ./rendus-etudiants/*` pour voir la répartition des commits
- **Nettoyage import** : `forge rename ./import --strip-accents --lowercase` (à venir)

---

## Dev

```bash
pytest -q          # 2 tests
forge --help
```

## Roadmap
- [ ] `forge ignore --list`
- [ ] `forge stats --since 1.month --by-file`
- [ ] `forge rename --lowercase` / `--slugify`

MIT — PRs bienvenues.
