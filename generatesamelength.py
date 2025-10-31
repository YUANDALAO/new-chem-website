#!/usr/bin/env python3
"""
终极精确统一键长方案
基于分子边界框计算缩放比例
"""
from rdkit import Chem
from rdkit.Chem import AllChem, Descriptors
from rdkit.Chem.Draw import rdMolDraw2D
import yaml
import os

OUTPUT_DIR = 'assets/images/compounds'
YAML_FILE = '_data/molecules.yml'
IMAGE_SIZE = 400
TARGET_BOND_LENGTH = 20

def load_molecules():
    if not os.path.exists(YAML_FILE):
        print(f'❌ 找不到 {YAML_FILE}')
        return []
    
    with open(YAML_FILE, 'r', encoding='utf-8') as f:
        molecules = yaml.safe_load(f)
    
    return molecules if molecules else []

def get_molecule_extent(mol):
    """
    计算分子的实际占用范围（边界框）
    这个更准确反映RDKit的缩放行为
    """
    conf = mol.GetConformer()
    
    xs = [conf.GetAtomPosition(i).x for i in range(mol.GetNumAtoms())]
    ys = [conf.GetAtomPosition(i).y for i in range(mol.GetNumAtoms())]
    
    x_range = max(xs) - min(xs)
    y_range = max(ys) - min(ys)
    
    # 使用最大范围作为特征尺寸
    extent = max(x_range, y_range)
    
    # 考虑原子数量的影响（更多原子 = 更复杂）
    num_atoms = mol.GetNumAtoms()
    
    # 组合因子：边界框大小 + 原子数量的影响
    complexity_factor = extent * (1 + num_atoms * 0.01)
    
    return complexity_factor

def generate_svg_with_scale(mol_id, smiles, output_dir):
    try:
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            print(f'❌ {mol_id}: 无效SMILES')
            return False, None, None
        
        AllChem.Compute2DCoords(mol)
        
        # 计算分子的实际占用范围
        extent = get_molecule_extent(mol)
        
        # 创建SVG绘图器
        drawer = rdMolDraw2D.MolDraw2DSVG(IMAGE_SIZE, IMAGE_SIZE)
        
        opts = drawer.drawOptions()
        opts.fixedBondLength = TARGET_BOND_LENGTH
        opts.bondLineWidth = 1.2
        opts.minFontSize = 12
        opts.maxFontSize = 14
        opts.atomLabelFontSize = 13
        opts.padding = 0.15
        opts.useBWAtomPalette()
        
        drawer.DrawMolecule(mol)
        drawer.FinishDrawing()
        
        svg = drawer.GetDrawingText()
        
        # 保存SVG
        svg_path = os.path.join(output_dir, f'{mol_id}.svg')
        with open(svg_path, 'w', encoding='utf-8') as f:
            f.write(svg)
        
        mw = Descriptors.MolWt(mol)
        num_atoms = mol.GetNumAtoms()
        
        print(f'✓ {mol_id} (MW: {mw:.1f}, Atoms: {num_atoms}, Extent: {extent:.2f})')
        return True, mw, extent
        
    except Exception as e:
        print(f'❌ {mol_id}: {str(e)}')
        return False, None, None

def main():
    print('🔬 精确计算键长统一方案...\n')
    
    molecules = load_molecules()
    if not molecules:
        print('❌ 没有数据！')
        return
    
    print(f'📊 {len(molecules)} 个分子')
    print(f'📐 目标键长: {TARGET_BOND_LENGTH}px\n')
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    success = 0
    failed = []
    mol_info = {}
    
    # 第一遍：生成SVG并收集数据
    for molecule in molecules:
        mol_id = molecule.get('ID', '')
        smiles = molecule.get('SMILES', '')
        
        if not mol_id or not smiles:
            continue
        
        result, mw, extent = generate_svg_with_scale(mol_id, smiles, OUTPUT_DIR)
        
        if result:
            success += 1
            mol_info[mol_id] = {
                'mw': mw,
                'extent': extent
            }
        else:
            failed.append(mol_id)
    
    print(f'\n✅ 成功: {success}/{len(molecules)}')
    
    if failed:
        print(f'❌ 失败 {len(failed)} 个')
    
    # 使用中位数作为参考值
    extents = [info['extent'] for info in mol_info.values()]
    extents.sort()
    ref_extent = extents[len(extents)//2]
    
    print(f'\n参考extent: {ref_extent:.2f}')
    
    # 计算每个分子的缩放比例
    print(f'\n计算缩放比例...')
    for mol_id, info in mol_info.items():
        # 缩放比例 = 参考值 / 当前值
        # extent大的分子需要缩小，extent小的分子需要放大
        scale = ref_extent / info['extent']
        info['scale'] = scale
        print(f'{mol_id}: extent={info["extent"]:.2f}, scale={scale:.3f}')
    
    # 更新YAML
    print(f'\n更新YAML文件...')
    updated_molecules = []
    for molecule in molecules:
        mol_id = molecule.get('ID', '')
        if mol_id in mol_info:
            molecule['MW'] = round(mol_info[mol_id]['mw'], 2)
            molecule['scale'] = round(mol_info[mol_id]['scale'], 3)
        updated_molecules.append(molecule)
    
    with open(YAML_FILE, 'w', encoding='utf-8') as f:
        yaml.dump(updated_molecules, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
    
    print(f'✓ 已更新 {YAML_FILE}')
    print(f'📂 输出目录: {OUTPUT_DIR}/')

if __name__ == '__main__':
    main()