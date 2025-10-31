#!/usr/bin/env python3
"""
终极分子结构生成器 - 修复版
移除了不存在的SetBackgroundColour方法
"""
from rdkit import Chem
from rdkit.Chem import AllChem, Draw
from rdkit.Chem.Draw import rdMolDraw2D
import yaml
import os

OUTPUT_DIR = 'assets/images/compounds'
YAML_FILE = '_data/molecules.yml'
IMAGE_SIZE = 400

def load_molecules():
    if not os.path.exists(YAML_FILE):
        print(f'❌ 找不到 {YAML_FILE}')
        return []
    
    with open(YAML_FILE, 'r', encoding='utf-8') as f:
        molecules = yaml.safe_load(f)
    
    return molecules if molecules else []

def generate_clean_svg(mol_id, smiles, output_dir):
    try:
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            print(f'❌ {mol_id}: 无效SMILES')
            return False
        
        AllChem.Compute2DCoords(mol)
        
        # 创建SVG绘图器
        drawer = rdMolDraw2D.MolDraw2DSVG(IMAGE_SIZE, IMAGE_SIZE)
        
        # 设置绘图选项
        opts = drawer.drawOptions()
        
        # 核心设置
        opts.fixedBondLength = 30           # 统一键长
        opts.bondLineWidth = 1.2            # 细线条
        opts.minFontSize = 12
        opts.maxFontSize = 14
        opts.atomLabelFontSize = 13
        opts.padding = 0.15
        
        # 黑白配色 - 使用RDKit内置方法
        opts.useBWAtomPalette()
        
        # 绘制（不要用SetBackgroundColour，这个方法不存在）
        drawer.DrawMolecule(mol)
        drawer.FinishDrawing()
        
        svg = drawer.GetDrawingText()
        
        # 保存
        svg_path = os.path.join(output_dir, f'{mol_id}.svg')
        with open(svg_path, 'w', encoding='utf-8') as f:
            f.write(svg)
        
        print(f'✓ {mol_id}')
        return True
        
    except Exception as e:
        print(f'❌ {mol_id}: {str(e)}')
        return False

def main():
    print('🔬 生成分子结构...\n')
    
    molecules = load_molecules()
    if not molecules:
        print('❌ 没有数据！')
        return
    
    print(f'📊 {len(molecules)} 个分子')
    print(f'📐 键长: 30px 统一')
    print(f'🎨 黑白配色\n')
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    success = 0
    failed = []
    
    for molecule in molecules:
        mol_id = molecule.get('ID', '')
        smiles = molecule.get('SMILES', '')
        
        if not mol_id or not smiles:
            continue
        
        if generate_clean_svg(mol_id, smiles, OUTPUT_DIR):
            success += 1
        else:
            failed.append(mol_id)
    
    print(f'\n✅ 成功: {success}/{len(molecules)}')
    
    if failed:
        print(f'❌ 失败 {len(failed)} 个')
        if len(failed) <= 10:
            print(f'   {", ".join(failed)}')
    
    print(f'📂 {OUTPUT_DIR}/')

if __name__ == '__main__':
    main()
