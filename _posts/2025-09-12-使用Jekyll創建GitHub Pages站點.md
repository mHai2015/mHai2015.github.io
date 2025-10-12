---
layout: post
title:  "使用Jekyll創建GitHub Pages站點"
date:   2025-09-12 15:50:56 +0800
categories: [GitHub Pages]
---


先决条件
必须安装 Jekyll 和 Git 后才可使用 Jekyll 创建 GitHub Pages 站点。 有关详细信息，请参阅 Jekyll 文档中的安装和“设置 Git”。
建议使用 Bundler 安装和运行 Jekyll。 Bundler 可管理 Ruby gem 依赖项，减少 Jekyll 构建错误和阻止环境相关的漏洞。 要安装 Bundler：

Install dependencies:
sudo apt-get install ruby-full build-essential zlib1g-dev


echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

gem install jekyll bundler

安裝完成后進入項目目錄，使用：
bundle install

啓動Jekyll Server
bundle exec jekyll serve

參考網站：
https://jekyllrb.com/docs/installation/ubuntu/

https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll
