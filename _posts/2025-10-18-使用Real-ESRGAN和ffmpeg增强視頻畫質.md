---
layout: post
title:  "使用Real-ESRGAN和ffmpeg增强視頻畫質"
date:   2025-09-12 15:50:56 +0800
categories: [AI, ffmpeg]
---

Ubuntu 22.04+ 的新機制 (PEP 668)，目的是保護系統 Python，不允許直接用 pip 往系統環境裡裝包。使用虛擬環境 或 conda，更乾淨安全。

# 安裝虛擬環境模組
```bash
sudo apt install python3-venv -y
```
# 在 Real-ESRGAN 目錄下創建虛擬環境
```bash
python3.9 -m venv venv
```
# 啟用虛擬環境
```bash
source venv/bin/activate
```
# 激活后，`python` 应该可用了：
```bash
python --version
```
# 在虛擬環境內安裝依賴
```bash
pip install -r requirements.txt
```

# 退出虛擬環境
```bash
deactivate
```

在虛擬環境裡直接執行：
# 卸載現有套件：
```bash
pip uninstall -y torch torchvision torchaudio
```
# 安裝兼容版本
#  A: 針對 NVIDIA GPU（推薦 CUDA 11.3）
```bash
pip install torch==1.10.1+cu113 torchvision==0.11.2+cu113 -f https://download.pytorch.org/whl/torch_stable.html
```

#  B: 針對無 GPU 或 CPU 運行
```bash
pip install torch==1.10.1 torchvision==0.11.2
```

# 在 venv 中安装依赖（不会触发 PEP 668）
```bash
pip install -r requirements.txt
```

# 安装 package（等同于 setup.py develop）
```bash
pip install -e .
```
# 或者你原来的命令也可以：
```bash
python setup.py develop
```

解決方案：降級 NumPy 版本
# 1. 卸載現有的 NumPy
```bash
pip uninstall numpy -y
```
# 2. 安裝一個兼容的舊版本 (例如 1.26.4)
```bash
pip install numpy==1.26.4
```

# 手動下載模型
```bash
wget https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth
```


# 人臉增强
```bash
python3.9 inference_realesrgan.py -n RealESRGAN_x4plus -i tmp_frames/frames -o out_frames --face_enhance
```
