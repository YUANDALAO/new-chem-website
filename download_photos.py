#!/usr/bin/env python3
"""
易伟课题组成员照片批量下载脚本
从X-MOL网站下载所有成员照片，保存到本地目录

使用方法：
1. 安装依赖：pip install requests
2. 运行脚本：python download_photos.py
3. 照片将保存到 ./people/ 目录下
"""

import os
import requests
import time
from urllib.parse import urljoin

# 创建保存目录
SAVE_DIR = "./people"
os.makedirs(SAVE_DIR, exist_ok=True)

# X-MOL基础URL
BASE_URL = "https://www.x-mol.com"

# 请求头，模拟浏览器
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Referer': 'https://www.x-mol.com/groups/Yi_wei/people',
}

# ==================== 成员照片信息 ====================
# 格式: (图片URL路径, 保存文件名)

PHOTOS = [
    # ========== 导师 ==========
    ("/groups/uploadfile/20250618_1750228159412.png", "yiwei.png"),
    ("/groups/uploadfile/20250618_1750229505767.jpg", "zhouzhi.jpg"),
    ("/groups/uploadfile/20250618_1750230711762.jpg", "wangshengdong.jpg"),
    ("/groups/uploadfile/20250618_1750230841958.png", "zengzhongyi.png"),
    ("/groups/uploadfile/20250618_1750238874624.jpg", "liuxiawen.jpg"),
    ("/groups/uploadfile/20250618_1750239120416.jpg", "huangjunjun.jpg"),
    ("/groups/uploadfile/20250620_1750420659021.jpg", "wuwenhao.jpg"),
    ("/groups/uploadfile/20250620_1750421646660.jpg", "zhaoxin.jpg"),
    ("/groups/uploadfile/20250620_1750421843078.png", "liaosiyan.png"),
    ("/groups/uploadfile/20250620_1750422130797.jpg", "huangyugang.jpg"),
    
    # ========== 博士后 ==========
    ("/groups/uploadfile/20250620_1750422782685.jpg", "malei.jpg"),
    ("/groups/uploadfile/20250623_1750649368189.png", "chenfangyuan.png"),
    ("/groups/uploadfile/20250623_1750682905870.jpg", "chenweijie.jpg"),
    ("/groups/uploadfile/20250623_1750683292343.png", "liufuxiaomin.png"),
    ("/groups/uploadfile/20250623_1750683842941.png", "wangmei.png"),
    ("/groups/uploadfile/20250624_1750750323975.jpg", "zamanmanzoor.jpg"),
    ("/groups/uploadfile/20250623_1750683713290.jpg", "jianghong.jpg"),
    ("/groups/uploadfile/20250623_1750684393932.png", "luguangsheng.png"),
    ("/groups/uploadfile/20250623_1750685665964.jpg", "tangjunyuan.jpg"),
    ("/groups/uploadfile/20250625_1750844630683.png", "wangkezhi.png"),
    ("/groups/uploadfile/20250625_1750836086408.png", "quliye.png"),
    ("/groups/uploadfile/20250625_1750836689922.jpg", "wuyunxiang.jpg"),
    ("/groups/uploadfile/20250902_1756796708371.jpg", "wumin.jpg"),
    
    # ========== 科研助理 ==========
    ("/groups/uploadfile/20250623_1750686277553.png", "zengru.png"),
    ("/groups/uploadfile/20250624_1750749405942.jpg", "luojiayu.jpg"),
    ("/groups/uploadfile/20250623_1750688153377.png", "weiwei.png"),
    ("/groups/uploadfile/20250625_1750835690211.png", "shouqingguo.png"),
    
    # ========== 博士研究生 ==========
    ("/groups/uploadfile/20250625_1750820335146.jpg", "liuqingmei.jpg"),
    ("/groups/uploadfile/20250625_1750843449944.jpg", "zhangsilin.jpg"),
    
    # ========== 硕士研究生 ==========
    # 2022级
    ("/groups/uploadfile/20250625_1750838240331.jpg", "liuxuehui.jpg"),
    # 2023级
    ("/groups/uploadfile/20250625_1750838556974.jpg", "liyang.jpg"),
    ("/groups/uploadfile/20250625_1750838781490.jpg", "zhuxinyuan.jpg"),
    ("/groups/uploadfile/20250625_1750843149716.jpg", "liusuixia.jpg"),
    ("/groups/uploadfile/20250625_1750839710581.jpg", "huangping.jpg"),
    ("/groups/uploadfile/20250625_1750840226972.jpg", "huangjianlian.jpg"),
    ("/groups/uploadfile/20250625_1750840499525.jpg", "gaoshiyu.jpg"),
    ("/groups/uploadfile/20250625_1750840581262.png", "yangmingkai.png"),
    ("/groups/uploadfile/20250625_1750840982663.jpg", "lilinzai.jpg"),
    ("/groups/uploadfile/20250625_1750840675327.jpg", "liujiayi.jpg"),
    ("/groups/uploadfile/20250625_1750840838699.jpg", "liangmiao.jpg"),
    ("/groups/uploadfile/20250625_1750840920887.jpg", "duanruxia.jpg"),
    ("/groups/uploadfile/20250625_1750841062150.jpg", "zhengjunyuan.jpg"),
    ("/groups/uploadfile/20250625_1750838851968.jpg", "chenzhijin.jpg"),
    ("/groups/uploadfile/20250625_1750840157279.jpg", "liumianni.jpg"),
    ("/groups/uploadfile/20250625_1750839639701.jpg", "huangbaohua.jpg"),
    ("/groups/uploadfile/20250625_1750840770312.jpg", "zhanshiping.jpg"),
    ("/groups/uploadfile/20250625_1750841111416.jpg", "zhangtianwan.jpg"),
    ("/groups/uploadfile/20250625_1750841185613.jpg", "lisuifei.jpg"),
    # 2024级
    ("/groups/uploadfile/20250625_1750841741204.jpg", "helincan.jpg"),
    ("/groups/uploadfile/20250625_1750842999188.jpg", "yancuishi.jpg"),
    ("/groups/uploadfile/20250625_1750843541972.png", "gaoxinyu.png"),
    ("/groups/uploadfile/20250625_1750843629795.png", "liqixin.png"),
    ("/groups/uploadfile/20250625_1750843692595.png", "wuxinhong.png"),
    ("/groups/uploadfile/20250625_1750843776607.png", "qiudan.png"),
    ("/groups/uploadfile/20250625_1750843847885.png", "wangchuitain.png"),
    ("/groups/uploadfile/20250701_1751336583347.png", "liujie.png"),
    ("/groups/uploadfile/20250625_1750843928008.png", "xieqinxie.png"),
    ("/groups/uploadfile/20250625_1750844026577.png", "zoupei.png"),
    ("/groups/uploadfile/20250625_1750844085089.png", "dongmenghan.png"),
    ("/groups/uploadfile/20250625_1750844151388.png", "xiangyu.png"),
    ("/groups/uploadfile/20250625_1750842778306.jpg", "huangjiayin.jpg"),
]


def download_photo(url_path, filename):
    """下载单张照片"""
    full_url = urljoin(BASE_URL, url_path)
    save_path = os.path.join(SAVE_DIR, filename)
    
    try:
        print(f"下载中: {filename} ...", end=" ")
        response = requests.get(full_url, headers=HEADERS, timeout=30)
        
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print(f"✓ 成功 ({len(response.content)//1024}KB)")
            return True
        else:
            print(f"✗ 失败 (HTTP {response.status_code})")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"✗ 错误: {e}")
        return False


def main():
    print("=" * 60)
    print("易伟课题组成员照片批量下载工具")
    print("=" * 60)
    print(f"保存目录: {os.path.abspath(SAVE_DIR)}")
    print(f"共 {len(PHOTOS)} 张照片待下载")
    print("-" * 60)
    
    success_count = 0
    fail_count = 0
    
    for i, (url_path, filename) in enumerate(PHOTOS, 1):
        print(f"[{i}/{len(PHOTOS)}] ", end="")
        if download_photo(url_path, filename):
            success_count += 1
        else:
            fail_count += 1
        
        # 添加延时，避免请求过快
        time.sleep(0.3)
    
    print("-" * 60)
    print(f"下载完成！成功: {success_count}, 失败: {fail_count}")
    print(f"照片保存在: {os.path.abspath(SAVE_DIR)}")
    print()
    print("接下来请将 people 文件夹中的所有图片复制到网站的")
    print("/assets/img/people/ 目录下即可。")


if __name__ == "__main__":
    main()
