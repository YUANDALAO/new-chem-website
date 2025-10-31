#!/usr/bin/env python3
"""
改进版分子结构生成脚本
- 统一缩放所有分子
- 更清晰的线条和字体
- 自动居中
"""
from rdkit import Chem
from rdkit.Chem import Draw, AllChem
from rdkit.Chem.Draw import rdMolDraw2D
import os

# 配置
IMAGE_SIZE = (400, 400)
OUTPUT_DIR = 'assets/images/compounds'

COMPOUNDS = {
    'A002': 'Cc1ccc(cc1)C2=NC(=CO2)c3ccccc3',
    'A003': 'Cc1ccc(cc1)C2=NC(=CO2)c3ccccc3',
    'A004': 'c1ccc2c(c1)oc(c2)C3=NC(=CS3)c4ccccc4',
    'A005': 'Cc1ccc(cc1)C2=NC(=CS2)c3ccc[nH]3',
    'B001': 'O=C1Nc2ccccc2S1',
    'B002': 'O=C1Nc2cc(Cl)ccc2S1',
    'B003': 'O=C1Nc2cc(Br)ccc2S1',
    'B004': 'O=C1Nc2cc(C(F)(F)F)ccc2S1',
    'B005': 'CN1C(=O)c2ccccc2S1',
    'B006': 'O=C1N(CC(F)(F)F)c2ccccc2S1',
}

def generate_structure(smiles, comp_id, output_dir):
    """生成统一大小和样式的分子结构图"""
    try:
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            print(f'❌ {comp_id}: Invalid SMILES')
            return False
        
        # 生成2D坐标
        AllChem.Compute2DCoords(mol)
        
        # === PNG版本（高分辨率）===
        png_path = os.path.join(output_dir, f'{comp_id}.png')
        img = Draw.MolToImage(
            mol, 
            size=IMAGE_SIZE, 
            kekulize=True,
            fitImage=True  # 自动缩放以适应画布
        )
        img.save(png_path, dpi=(300, 300))
        
        # === SVG版本（改进的绘图选项）===
        svg_path = os.path.join(output_dir, f'{comp_id}.svg')
        drawer = rdMolDraw2D.MolDraw2DSVG(IMAGE_SIZE[0], IMAGE_SIZE[1])
        
        # 设置绘图选项
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
        
        print(f'✓ {comp_id}')
        return True
        
    except Exception as e:
        print(f'❌ {comp_id}: {str(e)}')
        return False

def main():
    print('🔬 Generating uniform structures...\n')
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    count = 0
    for comp_id, smiles in COMPOUNDS.items():
        if generate_structure(smiles, comp_id, OUTPUT_DIR):
            count += 1
    
    print(f'\n✅ {count}/{len(COMPOUNDS)} structures generated')
    print(f'📂 Output: {OUTPUT_DIR}/')
    print('\n💡 All structures now have uniform size and scaling!')

if __name__ == '__main__':
    main()
