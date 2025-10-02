在Windows或者Ubuntu上安裝git

# Git 安裝教程 (Windows & Linux)

Git 是目前最流行的分散式版本控制系統，用於代碼管理和團隊協作。  
以下將介紹如何在 **Windows** 和 **Linux** 系統上安裝 Git。

---

## 🖥 Windows 安裝 Git

1. **下載安裝包**  
   前往 [Git 官網下載頁面](https://git-scm.com/download/win)，會自動下載適合你系統的安裝檔案（`.exe`）。

2. **執行安裝程式**  
   - 雙擊下載的安裝檔。  
   - 安裝過程中保持默認選項即可（建議選擇 **Use Git from Git Bash only** 或 **Git from the command line and also from 3rd-party software**）。  

3. **驗證安裝**  
   打開 **Git Bash** 或 **命令提示字元 (CMD)**，輸入：
   ```bash
   git --version



## 🐧 Ubuntu 安裝 Git
Debian / Ubuntu
sudo apt update
sudo apt install git -y


## 驗證安裝 
   打開 **Git Bash** 或 **命令提示字元 (CMD)**，輸入：
   ```bash
   git --version
   
## ⚙️ 配置 Git

安裝完成後，首次使用需要設定用戶名稱和郵箱，這會記錄在提交紀錄中：

git config --global user.name "你的名字"
git config --global user.email "你的郵箱@example.com"


確認配置是否正確：

git config --list
