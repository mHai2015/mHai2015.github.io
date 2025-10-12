---
layout: post
title:  "在Github上配置ssh"
date:   2025-09-12 15:50:56 +0800
categories: [ssh]
---

在本地電腦上生成SSH金鑰
ssh-keygen -t rsa -b 4096 -C "你的郵箱"
一路回車，會生成兩個文件（默認位置在 ~/.ssh/）：

id_rsa（私鑰，請勿泄露）

id_rsa.pub（公鑰，需要添加到 GitHub）