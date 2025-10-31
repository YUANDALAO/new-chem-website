#!/usr/bin/env python3
"""
从 _data/molecules.yml 读取所有分子数据并生成统一尺寸的结构图
这个脚本会读取你用 prepare_chemlib.py 生成的所有分子数据
"""
from rdkit import Chem
from rdkit.Chem import Draw, AllChem
from rdkit.Chem.Draw import rdMolDraw2D
import yaml
import os

# 配置
IMAGE_SIZE = (400, 400)
OUTPUT_DIR = 'assets/images/compounds'
YAML_FILE = '_data/molecules.yml'

def load_molecules_from_yaml():
    """从 YAML 文件加载分子数据"""
    if not os.path.exists(YAML_FILE):
        print(f'❌ 错误: 找不到文件 {YAML_FILE}')
        print(f'请先运行 prepare_chemlib.py 生成 YAML 文件')
        return []
    
    with open(YAML_FILE, 'r', encoding='utf-8') as f:
        molecules = yaml.safe_load(f)
    
    return molecules if molecules else []

def generate_structure(mol_id, smiles, output_dir):
    """生成统一大小和样式的分子结构图"""
    try:
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            print(f'❌ {mol_id}: Invalid SMILES - {smiles}')
            return False
        
        # 生成2D坐标
        AllChem.Compute2DCoords(mol)
        
        # === PNG版本（高分辨率）===
        png_path = os.path.join(output_dir, f'{mol_id}.png')
        img = Draw.MolToImage(
            mol, 
            size=IMAGE_SIZE, 
            kekulize=True,
            fitImage=True  # 自动缩放以适应画布
        )
        img.save(png_path, dpi=(300, 300))
        
        # === SVG版本（统一尺寸）===
        svg_path = os.path.join(output_dir, f'{mol_id}.svg')
        drawer = rdMolDraw2D.MolDraw2DSVG(IMAGE_SIZE[0], IMAGE_SIZE[1])
        
        # 设置绘图选项 - 确保统一尺寸
        opts = drawer.drawOptions()
        opts.bondLineWidth = 2.0          # 线条粗细
        opts.atomLabelFontSize = 32       # 字体大小
        opts.minFontSize = 20             # 最小字体
        opts.fixedBondLength = 30         # 固定键长（关键！）
        opts.padding = 0.1                # 内边距
        opts.additionalAtomLabelPadding = 0.1
        
        # 绘制分子（自动缩放）
        drawer.DrawMolecule(mol)
        drawer.FinishDrawing()
        
        # 保存SVG
        svg = drawer.GetDrawingText()
        with open(svg_path, 'w') as f:
            f.write(svg)
        
        print(f'✓ {mol_id}')
        return True
        
    except Exception as e:
        print(f'❌ {mol_id}: {str(e)}')
        return False

def main():
    print('🔬 从 YAML 文件生成统一尺寸的分子结构图...\n')
    
    # 加载分子数据
    molecules = load_molecules_from_yaml()
    
    if not molecules:
        print('❌ 没有找到分子数据！')
        print('\n请确保：')
        print('1. 已运行 prepare_chemlib.py')
        print('2. _chemlib_data/ 文件夹中有 Excel 文件')
        print('3. Excel 文件包含 ID 和 SMILES 列')
        return
    
    print(f'📊 找到 {len(molecules)} 个分子\n')
    
    # 创建输出目录
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # 生成结构图
    count = 0
    failed = []
    
    for molecule in molecules:
        mol_id = molecule.get('ID', '')
        smiles = molecule.get('SMILES', '')
        
        if not mol_id or not smiles:
            print(f'⚠️  跳过: 缺少 ID 或 SMILES')
            continue
        
        if generate_structure(mol_id, smiles, OUTPUT_DIR):
            count += 1
        else:
            failed.append(mol_id)
    
    # 总结
    print(f'\n{"="*50}')
    print(f'✅ 成功生成: {count}/{len(molecules)} 个结构图')
    
    if failed:
        print(f'❌ 失败的分子: {", ".join(failed)}')
    
    print(f'📂 输出目录: {OUTPUT_DIR}/')
    print(f'{"="*50}')
    print('\n💡 所有结构图现在都是统一尺寸！')
    print('💡 可以直接在网页中使用了')

if __name__ == '__main__':
    main()
