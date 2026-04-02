# CLAUDE.md — synfinder.com (new-chem-website)

## Site overview
Jekyll static site for the Center for Drug Discovery, Guangzhou Medical University.
Deployed at **synfinder.com** via GitHub Pages, branch `gh-pages`.
Repo: `https://github.com/YUANDALAO/new-chem-website`

## Key pages
| URL | File |
|-----|------|
| `/` | `index.html` (standalone, no layout) |
| `/chemlib/` | `chemlib.md` — hub with 4 library cards |
| `/chemlib/active/` | `chemlib/active.md` |
| `/chemlib/natural/` | `chemlib/natural.md` |
| `/chemlib/scaffold/` | `chemlib/scaffold.md` |
| `/chemlib/druglike/` | `chemlib/druglike.md` |
| `/research/` | `Research.md` |
| `/people/` | `people.md` |
| `/publications/` | `publications.md` |
| `/contact/` | `contact.md` |

## ChemLib data pipeline

### Adding or updating compound data
1. Drop `.xlsx` files into `_chemlib_data/`
2. Run `python3 prepare_chemlib.py`
3. Commit `_data/molecules.yml` and `assets/data/compounds_*.json`

### How category is assigned (priority order)
1. If the Excel sheet has a `Category` column → use that value
2. Otherwise detected from the **filename** keyword:
   - `natural` → `natural`
   - `active` → `active`
   - `druglike` / `drug-like` / `drug_like` → `druglike`
   - `scaffold` → `scaffold`

### Column mapping per dataset
| Dataset file | Sheet | ID column | SMILES | MW | Name | Subcategory |
|---|---|---|---|---|---|---|
| `scaffold_ZhangLab_ChemLib_3.2.xlsx` | Sheet1 | `ID` | `SMILES` | — | — | — (has built-in `Category` col) |
| `active_DO1200-*.xlsx` | Sheet1 | `No.` (→ `ID`) | `SMILES` | `MW` | — | `Library` |
| `natural_L6000-*.xlsx` | `Compound List` | `ID` | `SMILES` | `MolWt` | `MOLENAME` | `category` |
| `druglike_L1000-*.xlsx` | `Compound List` | `ID` | `SMILES` | `MolWt` | `MOLENAME` | `Disease` |

### Output files
- `_data/molecules.yml` — only libraries with ≤ 3000 compounds (used by Jekyll/Liquid for scaffold page)
- `assets/data/compounds_<category>.json` — one file per category, used by JS client-side rendering

### Structure images
- **Scaffold** (`A001.svg` … `L999.svg`): pre-generated SVGs in `assets/images/compounds/`
- **Active / Natural / Druglike**: no SVG files — structures rendered live in browser from SMILES using **RDKit.js**

## Key includes
| File | Purpose |
|------|---------|
| `_includes/library_list.html` | Compound grid: fetches JSON, paginates 60/page, live search, RDKit.js rendering |
| `_includes/lib-page-styles.html` | Shared CSS for library sub-page headers |
| `_includes/header.html` | Sticky nav bar (active state via `page.url`) |
| `_includes/head.html` | Meta, fonts, Bootstrap, FontAwesome, RDKit.js preload |

## People page
- People list controlled by `_data/settings.yml` under the `people:` key
- Each entry: `name`, `title`, `image` (path relative to site root), `url` (slug matching `people/<slug>.md`)
- Profile pages live in `people/<slug>.md` — use `layout: page`
- Photos go in `assets/img/`

## Layout
- All subpages use `layout: default` (`_layouts/default.html`)
- `default.html` wraps content in `.content-wrapper` (max-width 1200px, 120px top padding for fixed nav)
- Primary colour: `#8b9cb6` (slate blue); text: `#2c3540`
