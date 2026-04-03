# 🖼️ HTML 转图片工具 / HTML to Image Tool
一款功能完整、开箱即用的 HTML 转高清图片工具，提供本地 Python 客户端与在线网页双版本。

[![GitHub Stars](https://img.shields.io/github/stars/SomeH-Bosx/html2img-tool?style=flat-square)](https://github.com/SomeH-Bosx/html2img-tool/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](https://github.com/SomeH-Bosx/html2img-tool/blob/main/LICENSE)
[![GitHub Pages](https://img.shields.io/badge/Demo-Online-blue?style=flat-square)](https://someh-bosx.github.io/html2img-tool/)

---

## 📋 目录
- [项目简介](#项目简介)
- [核心功能](#核心功能)
- [在线体验](#在线体验)
- [项目截图](#项目截图)
- [本地运行](#本地运行)
- [打包为EXE](#打包为exe)
- [贡献指南](#贡献指南)
- [许可证](#许可证)

---

## 项目简介
本项目实现 HTML 页面一键转图片功能，分为两个版本：
- **在线网页版**：纯前端 JavaScript 实现，GitHub Pages 部署，浏览器直接使用
- **本地桌面版**：Python + Tkinter + Playwright 开发，支持批量、自定义导出

---

## 核心功能
- 批量导入 HTML 文件 / 文件夹
- 自定义导出格式：PNG / JPG
- 自定义图片宽度与质量
- 实时预览 HTML 内容
- 深色模式 / 浅色模式切换
- 多种方式打开源文件
- 自动将本地图片转为 Base64

---

## 在线体验
直接访问使用：
👉 https://someh-bosx.github.io/html2img-tool/

---

## 项目截图
![网页版界面](assets/screenshot-web.png)
![桌面版界面](assets/screenshot_desktop.png)

---

## 本地运行
### 环境要求
- Python 3.7 ~ 3.11
- Windows / macOS / Linux

```bash
pip install -r requirements.txt
playwright install chromium
python export_html_to_image.py
