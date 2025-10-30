import pandas as pd
import yaml
import os

# --- 配置 ---
# 你的Excel文件所在的文件夹路径
# 我们使用_chemlib_data来避免与网页路径冲突
SOURCE_FOLDER = '_chemlib_data'
# 输出的Jekyll数据文件路径
OUTPUT_FILE = '_data/molecules.yml'

def process_files():
    """
    读取SOURCE_FOLDER中所有的.xlsx文件, 提取ID和SMILES,
    并将其写入到Jekyll的_data文件夹下的YAML文件中。
    """
    all_molecules = []
    
    print(f"开始扫描文件夹: {SOURCE_FOLDER}")

    # 检查源文件夹是否存在
    if not os.path.isdir(SOURCE_FOLDER):
        print(f"[错误] 源文件夹 '{SOURCE_FOLDER}' 不存在。请确保你已经创建了该文件夹并放入了Excel文件。")
        return

    # 遍历文件夹中的所有文件
    for filename in os.listdir(SOURCE_FOLDER):
        if filename.endswith('.xlsx') and not filename.startswith('~'):
            file_path = os.path.join(SOURCE_FOLDER, filename)
            print(f"  正在处理文件: {file_path}")
            
            try:
                # 读取Excel文件
                df = pd.read_excel(file_path)
                
                # 确保文件中包含'ID'和'SMILES'列
                if 'ID' in df.columns and 'SMILES' in df.columns:
                    # 遍历每一行
                    for index, row in df.iterrows():
                        # 确保ID和SMILES不为空
                        if pd.notna(row['ID']) and pd.notna(row['SMILES']):
                            molecule_data = {
                                'ID': str(row['ID']),        # 使用大写 'ID'
                                'SMILES': str(row['SMILES'])   # 使用大写 'SMILES'
                            }
                            all_molecules.append(molecule_data)
                else:
                    print(f"    [警告] 文件 {filename} 缺少 'ID' 或 'SMILES' 列, 已跳过。")
            
            except Exception as e:
                print(f"    [错误] 处理文件 {filename} 时出错: {e}")

    # 如果没有找到任何分子数据，则提示并退出
    if not all_molecules:
        print("\n[警告] 没有从任何Excel文件中提取到分子数据。请检查文件内容和列名。")
        return

    # 确保_data文件夹存在
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    # 将所有分子数据写入YAML文件
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        yaml.dump(all_molecules, f, default_flow_style=False, allow_unicode=True)
        
    print(f"\n处理完成! 总共 {len(all_molecules)} 个分子数据已成功写入到 {OUTPUT_FILE}")

if __name__ == '__main__':
    process_files()