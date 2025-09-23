import os
import re
import time

# 使用時間戳作為版本號
version = str(int(time.time()))

# 要處理的文件夾
target_dir = "./"

# 匹配 <link> 和 <script> 標籤的正則
pattern = re.compile(r'((?:href|src)=["\'])([^"\']+)(["\'])')

for root, _, files in os.walk(target_dir):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # 替換資源 URL，附加 ?v=timestamp
            def replacer(match):
                prefix, url, suffix = match.groups()
                # 忽略外部連結（http/https）
                if url.startswith("http"):
                    return match.group(0)
                # 如果已經有 ?v=，就替換成新版本號
                if "?v=" in url:
                    url = re.sub(r'\?v=\d+', f"?v={version}", url)
                else:
                    url = f"{url}?v={version}"
                return f"{prefix}{url}{suffix}"

            new_content = pattern.sub(replacer, content)

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)

            print(f"已處理: {file_path}")
