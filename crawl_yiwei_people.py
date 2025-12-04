import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
import os
import shutil

# 目标网页 URL
TARGET_URL = "https://www.x-mol.com/groups/Yi_wei/people"

# 请求头（模拟浏览器）
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Referer": "https://www.x-mol.com/"
}

def download_image(img_url, save_dir):
    """下载图片到本地"""
    try:
        img_name = os.path.basename(img_url)
        if not img_name:
            img_name = f"avatar_{hash(img_url)}.jpg"
        save_path = os.path.join(save_dir, img_name)
        
        response = requests.get(img_url, headers=headers, timeout=10, stream=True)
        response.raise_for_status()
        with open(save_path, "wb") as f:
            shutil.copyfileobj(response.raw, f)
        return img_name
    except:
        return None

def crawl_people_info():
    try:
        # 1. 获取网页内容
        response = requests.get(TARGET_URL, headers=headers, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # 2. 定位截图中的 container 容器（修复核心）
        container = soup.find("div", class_="container")
        if not container:
            print("未找到 container 容器！")
            return

        # 3. 提取导师介绍（member-teacher 类）
        mentors = []
        teacher_container = container.find("div", class_="member-teacher")
        if teacher_container:
            # 提取每个导师卡片
            teacher_cards = teacher_container.find_all("div", recursive=False)  # 只找直接子元素
            for card in teacher_cards:
                # 提取头像
                avatar_img = card.find("img")
                avatar_url = urljoin(TARGET_URL, avatar_img["src"]) if avatar_img else ""
                # 提取姓名+职务
                name_elem = card.find("b") or card.find("h3")
                name = name_elem.get_text(strip=True) if name_elem else "未知"
                title_elem = card.find(string=re.compile(r"教授|副教授|博导|硕导"))
                title = title_elem.strip() if title_elem else ""
                # 提取简介
                bio_elem = card.find("div", string=re.compile(r"个人介绍|研究领域"))
                bio = bio_elem.get_text(strip=True, separator="\n") if bio_elem else ""
                
                mentors.append({
                    "name": name,
                    "title": title,
                    "bio": bio,
                    "avatar_url": avatar_url
                })

        # 4. 提取当前组员（member-on 类）
        current_members = []
        on_container = container.find("div", class_="member-on")
        if on_container:
            members_elem = on_container.find("div")
            if members_elem:
                current_members = [m.strip() for m in members_elem.get_text().split("、") if m.strip()]

        # 5. 提取往届组员（member-history 类）
        history_members = []
        history_container = container.find("div", class_="member-history")
        if history_container:
            members_elem = history_container.find("div")
            if members_elem:
                history_members = [m.strip() for m in members_elem.get_text().split("、") if m.strip()]

        # 6. 保存数据+下载图片
        output_dir = "yiwei_people_data"
        img_dir = os.path.join(output_dir, "avatars")
        os.makedirs(img_dir, exist_ok=True)

        # 保存文本信息
        with open(os.path.join(output_dir, "people_data.txt"), "w", encoding="utf-8") as f:
            f.write("=== 导师介绍 ===\n")
            for m in mentors:
                f.write(f"姓名：{m['name']}\n职务：{m['title']}\n简介：{m['bio']}\n头像链接：{m['avatar_url']}\n\n")
            
            f.write("=== 当前组员 ===\n")
            f.write("、".join(current_members) + "\n\n")
            
            f.write("=== 往届组员 ===\n")
            f.write("、".join(history_members) + "\n")

        # 下载头像
        with open(os.path.join(output_dir, "avatar_local_paths.txt"), "w", encoding="utf-8") as f:
            f.write("头像本地路径（对应导师）：\n")
            for m in mentors:
                if m["avatar_url"]:
                    local_img = download_image(m["avatar_url"], img_dir)
                    if local_img:
                        f.write(f"{m['name']}：avatars/{local_img}\n")

        print(f"✅ 抓取成功！数据已保存到 {output_dir} 文件夹")
        print(f"- 导师数量：{len(mentors)}")
        print(f"- 当前组员数量：{len(current_members)}")
        print(f"- 往届组员数量：{len(history_members)}")

    except Exception as e:
        print(f"❌ 抓取失败：{str(e)}")

if __name__ == "__main__":
    crawl_people_info()