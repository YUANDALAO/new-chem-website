import pandas as pd
import yaml
import json
import os
from collections import Counter

# --- Config ---
SOURCE_FOLDER   = '_chemlib_data'
OUTPUT_YAML     = '_data/molecules.yml'       # small scaffold data for Jekyll
OUTPUT_JSON_DIR = 'assets/data'               # per-category JSON for JS rendering

# Category is detected from the Excel filename.
CATEGORY_KEYWORDS = [
    ('natural',   'natural'),
    ('active',    'active'),
    ('druglike',  'druglike'),
    ('drug_like', 'druglike'),
    ('drug-like', 'druglike'),
    ('scaffold',  'scaffold'),
]

# Libraries with <= this many compounds are also kept in molecules.yml
# (used by Jekyll/Liquid for small collections like scaffold).
YAML_SIZE_LIMIT = 3000

def detect_category(filename):
    name_lower = filename.lower()
    for keyword, category in CATEGORY_KEYWORDS:
        if keyword in name_lower:
            return category
    return 'unknown'

def process_files():
    all_molecules = []

    print(f"Scanning: {SOURCE_FOLDER}\n")

    if not os.path.isdir(SOURCE_FOLDER):
        print(f"[Error] Folder '{SOURCE_FOLDER}' not found.")
        return

    for filename in sorted(os.listdir(SOURCE_FOLDER)):
        if not filename.endswith('.xlsx') or filename.startswith('~'):
            continue

        file_path = os.path.join(SOURCE_FOLDER, filename)
        category  = detect_category(filename)
        print(f"  {filename}  →  category = '{category}'")

        try:
            try:
                df = pd.read_excel(file_path, sheet_name='Compound List')
            except Exception:
                df = pd.read_excel(file_path)

            # Normalise ID column
            if 'ID' not in df.columns and 'IDNUMBER' in df.columns:
                df = df.rename(columns={'IDNUMBER': 'ID'})

            if 'ID' not in df.columns or 'SMILES' not in df.columns:
                print(f"    [Warning] Missing 'ID' or 'SMILES' — skipped.")
                print(f"    Columns found: {df.columns.tolist()}")
                continue

            count = 0
            for _, row in df.iterrows():
                if pd.isna(row['ID']) or pd.isna(row['SMILES']):
                    continue

                # Use Category column from Excel if available
                if 'Category' in df.columns and pd.notna(row['Category']):
                    cat = str(row['Category']).strip().lower()
                else:
                    cat = category

                mol = {
                    'ID':       str(row['ID']).strip(),
                    'SMILES':   str(row['SMILES']).strip(),
                    'Category': cat,
                }
                if 'MW' in df.columns and pd.notna(row['MW']):
                    mol['MW'] = round(float(row['MW']), 2)
                if 'scale' in df.columns and pd.notna(row['scale']):
                    mol['scale'] = round(float(row['scale']), 3)

                all_molecules.append(mol)
                count += 1

            print(f"    {count} compounds loaded")

        except Exception as e:
            print(f"    [Error] {e}")

    if not all_molecules:
        print("\n[Warning] No molecule data found.")
        return

    # ── Group by category ──────────────────────────────────
    by_category = {}
    for mol in all_molecules:
        by_category.setdefault(mol['Category'], []).append(mol)

    cats = Counter(m['Category'] for m in all_molecules)
    print(f"\nTotal: {len(all_molecules)} compounds")
    print("  Category breakdown:")
    for cat, count in sorted(cats.items()):
        print(f"    {cat:12s}: {count}")

    # ── Write per-category JSON (for client-side rendering) ─
    os.makedirs(OUTPUT_JSON_DIR, exist_ok=True)
    for cat, mols in by_category.items():
        json_path = os.path.join(OUTPUT_JSON_DIR, f"compounds_{cat}.json")
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(mols, f, ensure_ascii=False, separators=(',', ':'))
        print(f"  → {json_path}  ({len(mols)} compounds)")

    # ── Write molecules.yml for Jekyll (small libs only) ────
    yaml_mols = [m for m in all_molecules if cats[m['Category']] <= YAML_SIZE_LIMIT]
    os.makedirs(os.path.dirname(OUTPUT_YAML), exist_ok=True)
    with open(OUTPUT_YAML, 'w', encoding='utf-8') as f:
        yaml.dump(yaml_mols, f,
                  default_flow_style=False,
                  allow_unicode=True,
                  sort_keys=False)
    print(f"\n  molecules.yml: {len(yaml_mols)} compounds (libraries ≤ {YAML_SIZE_LIMIT})")
    print("  Larger libraries use JSON + client-side rendering.\n")

if __name__ == '__main__':
    process_files()
