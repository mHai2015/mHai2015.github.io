---
layout: post
title:  "如何在Windows10上安裝Linux子系統WSL"
date:   2025-09-12 15:50:56 +0800
categories: [WSL]
---

以管理員模式啓動PowerShell, 輸入wsl --install命令，等待結束後重新啓動電腦。
wsl --install

參考網站：https://learn.microsoft.com/en-us/windows/wsl/install


查看可用的 Linux 發行版
wsl --list --online

3. 安裝指定的 Linux 發行版 (例如 Ubuntu)
wsl --install -d Ubuntu

 檢查已安裝的發行版
 wsl --list --verbose


查看已安裝的發行版：
wsl --list


要卸載 Ubuntu：
wsl --unregister Ubuntu


先關閉所有 WSL 發行版，並確認沒有在運行：
wsl --shutdown

停用 WSL 功能：
dism.exe /online /disable-feature /featurename:Microsoft-Windows-Subsystem-Linux

停用虛擬機平台（若你也不需要）：
dism.exe /online /disable-feature /featurename:VirtualMachinePlatform

⚠️ 小提示：

如果只是換一個 Linux 發行版，通常只需要用 wsl --unregister <發行版名>，不用整個卸載 WSL 功能。

完整刪除 WSL 會把所有 Linux 發行版與資料清空。


