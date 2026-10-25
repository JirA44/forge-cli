# forge-cli

## Français — présentation

**forge-cli** réunit trois outils Git en ligne de commande : générer un `.gitignore`, résumer l’activité d’un dépôt et renommer des fichiers en lot. Il s’adresse aux développeurs qui veulent accomplir ces tâches courantes sans assembler plusieurs scripts.

### À quoi ça sert, et pourquoi ?

Une CLI unique rassemble ces opérations et permet de les relancer de la même façon dans différents dépôts ou dossiers. Le renommage propose un mode `--dry-run` pour examiner les changements avant de les appliquer.

### Exemples

```bash
pip install forge-cli
forge ignore python,node,vscode -o .gitignore
forge stats ./mon-repo
forge rename ./photos --strip-accents --prefix 2026_ --dry-run
```

## English — overview

**forge-cli** combines three everyday command-line tools: generate a `.gitignore`, summarize Git activity and batch-rename files. It helps developers run these common tasks from one CLI instead of maintaining separate scripts.

### What is it for, and why use it?

A single CLI makes the operations easy to repeat across repositories and folders. The rename command supports `--dry-run` so you can review proposed changes before applying them.

### Examples

```bash
pip install forge-cli
forge ignore python,node,vscode -o .gitignore
forge stats ./my-repo
forge rename ./photos --strip-accents --prefix 2026_ --dry-run
```

## Installation et utilisation (français)



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
