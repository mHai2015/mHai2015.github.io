---
layout: post
title:  "Real-ESRGAN"
date:   2025-09-12 15:50:56 +0800
categories: [AI, ffmpeg]
---

Ubuntu 22.04+ 的新機制 (PEP 668)，目的是保護系統 Python，不允許直接用 pip 往系統環境裡裝包。
使用虛擬環境 或 conda，更乾淨安全。

# 安裝虛擬環境模組
sudo apt install python3-venv -y

# 在 Real-ESRGAN 目錄下創建虛擬環境
python3.9 -m venv venv

# 啟用虛擬環境
source venv/bin/activate

# 激活后，`python` 应该可用了：
python --version

# 在虛擬環境內安裝依賴
pip install -r requirements.txt


# 退出虛擬環境
deactivate


在虛擬環境裡直接執行：
# 卸載現有套件：
pip uninstall -y torch torchvision torchaudio
# 安裝兼容版本
#  A: 針對 NVIDIA GPU（推薦 CUDA 11.3）
pip install torch==1.10.1+cu113 torchvision==0.11.2+cu113 -f https://download.pytorch.org/whl/torch_stable.html
#  B: 針對無 GPU 或 CPU 運行
pip install torch==1.10.1 torchvision==0.11.2
# 在 venv 中安装依赖（不会触发 PEP 668）
pip install -r requirements.txt
# 安装 package（等同于 setup.py develop）
pip install -e .
# 或者你原来的命令也可以：
# python setup.py develop


解決方案：降級 NumPy 版本
# 1. 卸載現有的 NumPy
pip uninstall numpy -y

# 2. 安裝一個兼容的舊版本 (例如 1.26.4)
pip install numpy==1.26.4


wget https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth


python3.9 inference_realesrgan.py -n RealESRGAN_x4plus -i inputs -o results

ffmpeg -i "Three cute teenage girlfriends decided to go for a swim.mp4" -vsync 0 frames/frame_%06d.png


ffmpeg -ss 00:07:40 -to 00:07:42 -i input.mp4 -r 1 frames_%04d.png
ffmpeg -ss 00:07:40 -to 00:07:42 -i input.mp4 -vsync 0 frame_%06d.png


ffmpeg -framerate 20 -i results/frame_%06d_out.png -i tmp_frames/173110723.mp4 -map 0:v:0 -map 1:a:0 -c:v libx264 -crf 18 -c:a copy upscaled_vlog_4K.mp4



ffmpeg -i tmp_frames/input.mp4 -qscale:v 1 -qmin 1 -qmax 1 -vsync 0 tmp_frames/frames/frame%08d.png

ffmpeg -framerate 20 -i frames/frame%06d.png \
       -filter:v "minterpolate=fps=30" \
       -qscale:v 1 interpolated_frames/interpolated_frame%06d.png

# 人臉增强
python3.9 inference_realesrgan.py -n RealESRGAN_x4plus -i tmp_frames/frames -o out_frames --face_enhance


python3.9 inference_realesrgan.py -n RealESRGAN_x4plus -i tmp_frames/interpolated_frames -o upscaled_frames

ffmpeg -framerate 30 -i upscaled_frames/interpolated_frame%06d_out.png \
       -i tmp_frames/input.mp4 \
       -map 0:v:0 -map 1:a:0 \
       -c:v libx264 -crf 18 -c:a copy \
       results/final_vlog_30fps_upscaled.mp4


ffmpeg -framerate 30 -i upscaled_frames/interpolated_frame%06d_out.png \
       -i tmp_frames/input.mp4 \
       -map 0:v:0 -map 1:a:0 \
       -c:v libx264 \
       -crf 18 \
       -pix_fmt yuv420p \
       -preset medium \
       -c:a copy \
       results/final_compatible_video.mp4

python3.9 inference_realesrgan.py -n RealESRGAN_x4plus -i inputs -o results