---
layout: post
title:  "VMware Workstation虛擬機與Ubuntu系統安裝"
date:   2025-09-12 15:50:56 +0800
categories: [VMware Workstation, Ubuntu]
---

# 虛擬機與 Ubuntu 系統安裝教材

如何在電腦上安裝虛擬機 (VMware Workstation Player / VirtualBox)，並建立 Ubuntu Linux 系統。  
適合初學者學習 Linux 或搭建開發環境。

---

## 1. 前置準備

### 1.1 硬體需求
- **CPU**：支援虛擬化 (Intel VT-x 或 AMD-V)
- **記憶體 (RAM)**：至少 8GB (建議 16GB 以上)
- **硬碟空間**：至少 50GB
- **網路**：可下載 ISO 映像檔

### 1.2 軟體需求
- **虛擬機軟體**（選一個即可）：
  - VMware Workstation Player (免費，Win/Linux)
  - Oracle VirtualBox (免費，跨平台)
  - 下載：[vmware workstation pro 官方網站](https://ubuntu.com/download/desktop)
  - 如果在官方網站下載有困難，可以去往其他渠道下載，比如：[TECHSPOT](https://www.techspot.com/downloads/189-vmware-workstation-for-windows.html) 等等。
- **Ubuntu 映像檔 (ISO)**：
  - 下載：[Ubuntu 官方網站](https://ubuntu.com/download/desktop)
  - 推薦版本：Ubuntu 24.04 LTS

---

## 2. 安裝虛擬機軟體

### 2.1 安裝 VMware Workstation Player
1. 前往 [VMware 官方下載頁](https://www.vmware.com/products/workstation-player.html)。
2. 下載 **VMware Workstation Player (免費版本)**。
3. 執行安裝程式，一路點選 **Next → Accept → Install**。
4. 安裝完成後啟動程式。

### 2.2 安裝 VirtualBox
1. 前往 [VirtualBox 官方下載頁](https://www.virtualbox.org/wiki/Downloads)。
2. 下載對應系統的安裝檔 (Windows / macOS / Linux)。
3. 執行安裝程式，點選 **Next → Next → Install**。
4. 安裝完成後啟動程式。

---

## 3. 建立 Ubuntu 虛擬機

### 3.1 在 VMware 建立虛擬機
1. 開啟 VMware Player → **Create a New Virtual Machine**。
2. 選擇 **Installer disc image file (iso)**，載入剛剛下載的 Ubuntu ISO。
3. 選擇作業系統：**Linux → Ubuntu 64-bit**。
4. 設定名稱，例如：`Ubuntu-24.04`。
5. 設定虛擬硬碟大小：**50GB** (建議使用 Split 或 Single 都可)。
6. 點擊 **Customize Hardware**：
   - **Memory**：4096 MB（至少 4GB，建議 8GB）
   - **Processors**：2 核以上
   - **Network Adapter**：NAT 或 Bridged（建議 NAT）
7. 完成後點擊 **Finish**。

### 3.2 在 VirtualBox 建立虛擬機
1. 開啟 VirtualBox → 點擊 **New**。
2. 輸入名稱：`Ubuntu-24.04`。
3. 類型：**Linux**，版本：**Ubuntu (64-bit)**。
4. 記憶體大小：**4096MB 以上**。
5. 建立虛擬硬碟：
   - 類型：VDI (VirtualBox Disk Image)
   - 存儲方式：Dynamically allocated
   - 大小：50GB
6. 點擊 **Settings → Storage**，載入 Ubuntu ISO 檔案。
7. 點擊 **Start** 啟動虛擬機。

---

## 4. 安裝 Ubuntu 系統

1. 啟動虛擬機後，會進入 Ubuntu 安裝界面。
2. 選擇語言（建議 English，後續可安裝中文套件）。
3. 點擊 **Install Ubuntu**。
4. 鍵盤配置：選擇 **English (US)**。
5. 安裝選項：
   - Normal installation
   - 勾選 Download updates while installing
   - 勾選 Install third-party software
6. 磁碟分割：選擇 **Erase disk and install Ubuntu**（只影響虛擬硬碟，不會影響主機）。
7. 設定時區（例如：Asia/Shanghai）。
8. 建立使用者帳號：
   - Name: `student`
   - Computer name: `ubuntu-vm`
   - Username: `student`
   - Password: 自行設定
9. 點擊 **Install Now**，等待安裝完成。
10. 安裝完成後，點擊 **Restart Now**，進入 Ubuntu 桌面。

---

## 5. 基本配置

### 5.1 更新系統
打開終端機 (Terminal)：
```bash
sudo apt update && sudo apt upgrade -y
