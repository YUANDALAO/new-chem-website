#!/usr/bin/env python3
"""
图片重命名脚本
将浏览器保存的X-MOL图片重命名为对应的成员名字

使用方法：
1. 将此脚本放到 "组员介绍 - 易伟 课题组_files" 文件夹的同级目录
2. 运行: python rename_photos.py
3. 重命名后的图片会保存到 ./people/ 文件夹
"""

import os
import shutil

# 源文件夹（浏览器保存的图片文件夹）
SOURCE_DIR = "./组员介绍 - 易伟 课题组_files"

# 目标文件夹
TARGET_DIR = "./people"

# 文件名映射：X-MOL原文件名 -> 新文件名
RENAME_MAP = {
    # ========== 导师 ==========
    "20250618_1750228159412.png": "yiwei.png",
    "20250618_1750229505767.jpg": "zhouzhi.jpg",
    "20250618_1750230711762.jpg": "wangshengdong.jpg",
    "20250618_1750230841958.png": "zengzhongyi.png",
    "20250618_1750238874624.jpg": "liuxiawen.jpg",
    "20250618_1750239120416.jpg": "huangjunjun.jpg",
    "20250620_1750420659021.jpg": "wuwenhao.jpg",
    "20250620_1750421646660.jpg": "zhaoxin.jpg",
    "20250620_1750421843078.png": "liaosiyan.png",
    "20250620_1750422130797.jpg": "huangyugang.jpg",
    
    # ========== 博士后 ==========
    "20250620_1750422782685.jpg": "malei.jpg",
    "20250623_1750649368189.png": "chenfangyuan.png",
    "20250623_1750682905870.jpg": "chenweijie.jpg",
    "20250623_1750683292343.png": "liufuxiaomin.png",
    "20250623_1750683842941.png": "wangmei.png",
    "20250624_1750750323975.jpg": "zamanmanzoor.jpg",
    "20250623_1750683713290.jpg": "jianghong.jpg",
    "20250623_1750684393932.png": "luguangsheng.png",
    "20250623_1750685665964.jpg": "tangjunyuan.jpg",
    "20250625_1750844630683.png": "wangkezhi.png",
    "20250625_1750836086408.png": "quliye.png",
    "20250625_1750836689922.jpg": "wuyunxiang.jpg",
    "20250902_1756796708371.jpg": "wumin.jpg",
    
    # ========== 科研助理 ==========
    "20250623_1750686277553.png": "zengru.png",
    "20250624_1750749405942.jpg": "luojiayu.jpg",
    "20250623_1750688153377.png": "weiwei.png",
    "20250625_1750835690211.png": "shouqingguo.png",
    
    # ========== 博士研究生 ==========
    "20250625_1750820335146.jpg": "liuqingmei.jpg",
    "20250625_1750843449944.jpg": "zhangsilin.jpg",
    
    # ========== 硕士研究生 ==========
    "20250625_1750838240331.jpg": "liuxuehui.jpg",
    "20250625_1750838556974.jpg": "liyang.jpg",
    "20250625_1750838781490.jpg": "zhuxinyuan.jpg",
    "20250625_1750843149716.jpg": "liusuixia.jpg",
    "20250625_1750839710581.jpg": "huangping.jpg",
    "20250625_1750840226972.jpg": "huangjianlian.jpg",
    "20250625_1750840499525.jpg": "gaoshiyu.jpg",
    "20250625_1750840581262.png": "yangmingkai.png",
    "20250625_1750840982663.jpg": "lilinzai.jpg",
    "20250625_1750840675327.jpg": "liujiayi.jpg",
    "20250625_1750840838699.jpg": "liangmiao.jpg",
    "20250625_1750840920887.jpg": "duanruxia.jpg",
    "20250625_1750841062150.jpg": "zhengjunyuan.jpg",
    "20250625_1750838851968.jpg": "chenzhijin.jpg",
    "20250625_1750840157279.jpg": "liumianni.jpg",
    "20250625_1750839639701.jpg": "huangbaohua.jpg",
    "20250625_1750840770312.jpg": "zhanshiping.jpg",
    "20250625_1750841111416.jpg": "zhangtianwan.jpg",
    "20250625_1750841185613.jpg": "lisuifei.jpg",
    "20250625_1750841741204.jpg": "helincan.jpg",
    "20250625_1750842999188.jpg": "yancuishi.jpg",
    "20250625_1750843541972.png": "gaoxinyu.png",
    "20250625_1750843629795.png": "liqixin.png",
    "20250625_1750843692595.png": "wuxinhong.png",
    "20250625_1750843776607.png": "qiudan.png",
    "20250625_1750843847885.png": "wangchuitain.png",
    "20250701_1751336583347.png": "liujie.png",
    "20250625_1750843928008.png": "xieqinxie.png",
    "20250625_1750844026577.png": "zoupei.png",
    "20250625_1750844085089.png": "dongmenghan.png",
    "20250625_1750844151388.png": "xiangyu.png",
    "20250625_1750842778306.jpg": "huangjiayin.jpg",
}


def main():
    print("=" * 60)
    print("X-MOL图片重命名工具")
    print("=" * 60)
    
    # 检查源文件夹
    if not os.path.exists(SOURCE_DIR):
        print(f"错误：找不到源文件夹 '{SOURCE_DIR}'")
        print(f"请确保脚本与 '组员介绍 - 易伟 课题组_files' 文件夹在同一目录")
        return
    
    # 创建目标文件夹
    os.makedirs(TARGET_DIR, exist_ok=True)
    print(f"源文件夹: {os.path.abspath(SOURCE_DIR)}")
    print(f"目标文件夹: {os.path.abspath(TARGET_DIR)}")
    print("-" * 60)
    
    success = 0
    not_found = 0
    
    for old_name, new_name in RENAME_MAP.items():
        src_path = os.path.join(SOURCE_DIR, old_name)
        dst_path = os.path.join(TARGET_DIR, new_name)
        
        if os.path.exists(src_path):
            shutil.copy2(src_path, dst_path)
            print(f"✓ {new_name}")
            success += 1
        else:
            print(f"✗ 未找到: {old_name}")
            not_found += 1
    
    print("-" * 60)
    print(f"完成！成功: {success}, 未找到: {not_found}")
    print(f"\n图片已保存到: {os.path.abspath(TARGET_DIR)}")
    print("\n下一步：将 people 文件夹复制到网站的 /assets/img/ 目录下")


if __name__ == "__main__":
    main()
