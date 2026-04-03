# 🖼️ HTML 转图片工具 / HTML to Image Tool
一款功能完整、开箱即用的 HTML 转高清图片工具，提供本地 Python 客户端与在线网页双版本，支持批量转换、自定义导出、实时预览与深色模式。

[![GitHub Stars](https://img.shields.io/github/stars/SomeH-Bosx/html2img-tool?style=flat-square)](https://github.com/SomeH-Bosx/html2img-tool/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](https://github.com/SomeH-Bosx/html2img-tool/blob/main/LICENSE)
[![GitHub Pages](https://img.shields.io/badge/Demo-Online-blue?style=flat-square)](https://someh-bosx.github.io/html2img-tool/)

---

## 📋 目录 / Table of Contents
- [项目简介](sslocal://flow/file_open?url=%23%E9%A1%B9%E7%9B%AE%E7%AE%80%E4%BB%8B&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)
- [核心功能](sslocal://flow/file_open?url=%23%E6%A0%B8%E5%BF%83%E5%8A%9F%E8%83%BD&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)
- [在线体验](sslocal://flow/file_open?url=%23%E5%9C%A8%E7%BA%BF%E4%BD%93%E9%AA%8C&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)
- [项目截图](sslocal://flow/file_open?url=%23%E9%A1%B9%E7%9B%AE%E6%88%AA%E5%9B%BE&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)
- [本地运行](sslocal://flow/file_open?url=%23%E6%9C%AC%E5%9C%B0%E8%BF%90%E8%A1%8C&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)
- [打包为 EXE](sslocal://flow/file_open?url=%23%E6%89%93%E5%8C%85%E4%B8%BA-exe&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)
- [贡献指南](sslocal://flow/file_open?url=%23%E8%B4%A1%E7%8C%AE%E6%8C%87%E5%8D%97&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)
- [许可证](sslocal://flow/file_open?url=%23%E8%AE%B8%E5%8F%AF%E8%AF%81&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)

---

## 📖 项目简介
本项目实现了 HTML 页面一键转图片功能，分为两个版本：
- **在线网页版**：纯前端 JavaScript 实现，部署于 GitHub Pages，无需安装，浏览器直接使用
- **本地桌面版**：基于 Python + Tkinter + Playwright，支持批量 HTML 导入、自定义尺寸质量、深色模式

工具可自动处理本地图片资源，适合前端开发者、设计师、学生课程设计与日常快速转换使用。

---

## ✨ 核心功能
- 批量导入 HTML 文件 / 文件夹
- 自定义导出格式：PNG / JPG
- 自定义图片宽度与质量
- 实时预览 HTML 内容
- 深色模式 / 浅色模式切换
- 多种方式打开源文件（浏览器、VS Code、记事本）
- 自动将本地图片转为 Base64
- 在线直接使用，无需环境依赖

---

## 🚀 在线体验
直接访问即可使用：
👉 **https://someh-bosx.github.io/html2img-tool/**

---

## 📸 项目截图
### 在线网页版界面
![网页版界面](assets/screenshot-web.png)

### 本地桌面版界面
![桌面版界面](assets/screenshot_desktop.png)


---

## 💻 本地运行
### 环境要求
- Python 3.7 ~ 3.11
- Windows / macOS / Linux 全平台支持

### 安装依赖
```bash
pip install -r requirements.txt
playwright install chromium
