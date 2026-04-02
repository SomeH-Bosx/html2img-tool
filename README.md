# HTML 转图片工具 / HTML to Image Tool

## 目录 / Table of Contents

[TOC]

------

## 中文版文档

### 项目简介

这是一个功能强大的 HTML 转图片工具，支持批量导入 HTML 文件、实时预览、多种打开方式选择、自定义导出设置（格式、宽度、质量）以及深色模式，让你轻松将 HTML 内容转换为高清图片。

### 功能特性

- ✅ **多文件导入**：支持单个或多个 HTML 文件导入，也支持整个文件夹批量导入

- ✅ **实时预览**：点击文件列表即可预览 HTML 内容

- ✅ **多种打开方式**：支持默认浏览器、新标签页、记事本、VS Code 等多种方式打开源文件

- ✅ 

  自定义导出：

  - 格式：PNG / JPG
  - 宽度：自定义图片宽度
  - 质量：0-100 可调节

- ✅ **深色模式**：一键切换深色 / 浅色主题

- ✅ **批量导出**：支持批量导出选中的 HTML 文件

- ✅ **进度显示**：导出过程实时显示进度条

- ✅ **自动图片处理**：自动将 HTML 中的本地图片转换为 Base64 格式，确保图片正常显示

### 环境要求

- Python 3.7 或更高版本
- Windows / macOS / Linux

### 安装步骤

1. **克隆或下载项目**

   ```
   git clone <repository-url>
   cd <project-directory>
   ```

2. **安装依赖**

   ```bash
   pip install -r requirements.txt
   ```

3. **安装 Playwright 浏览器内核**

   ```bash
   playwright install chromium
   ```

### 使用说明

1. **运行工具**

   ```bash
   python html2img_python_ultimate.py
   ```

2. **导入文件**

   - 点击「添加文件」：选择单个或多个 HTML 文件
   - 点击「添加文件夹」：选择包含 HTML 文件的文件夹，批量导入

3. **预览文件**

   - 在文件列表中点击任意文件，即可在预览区查看 HTML 内容

4. **打开源文件**

   - 在「打开方式」下拉菜单中选择打开方式
   - 点击「打开选中文件」，即可用选择的方式打开源文件

5. **设置导出参数**

   - 格式：选择 PNG 或 JPG
   - 宽度：输入图片宽度（默认 1200px）
   - 质量：输入图片质量（0-100，默认 90）

6. **导出图片**

   - 勾选要导出的文件
   - 点击「批量导出」
   - 导出完成后，图片会保存在项目目录下的 `output` 文件夹中

### 常见问题

**Q: 导出的图片在哪里？**

A: 图片统一保存在项目目录下的 `output` 文件夹中，导出完成后会弹窗显示具体路径。

**Q: 本地图片无法显示？**

A: 工具会自动将 HTML 中的本地图片转换为 Base64 格式，确保图片正常显示。

**Q: 如何切换深色模式？**

A: 点击「深色模式」按钮即可一键切换深色 / 浅色主题。

### 许可证

MIT License

------

## English Documentation

### Project Introduction

This is a powerful HTML to Image tool that supports batch importing HTML files, real-time preview, multiple opening methods, custom export settings (format, width, quality), and dark mode, making it easy to convert HTML content into high-definition images.

### Features

- ✅ **Multi-file Import**: Support importing single or multiple HTML files, or batch importing an entire folder

- ✅ **Real-time Preview**: Click on the file list to preview HTML content

- ✅ **Multiple Opening Methods**: Support opening source files with default browser, new tab, Notepad, VS Code, etc.

- ✅ 

  Custom Export:

  - Format: PNG / JPG
  - Width: Custom image width
  - Quality: Adjustable from 0-100

  

- ✅ **Dark Mode**: One-click switch between dark/light themes

- ✅ **Batch Export**: Support batch exporting selected HTML files

- ✅ **Progress Display**: Real-time progress bar during export

- ✅ **Automatic Image Processing**: Automatically convert local images in HTML to Base64 format to ensure normal display

### Requirements

- Python 3.7 or higher
- Windows / macOS / Linux

### Installation Steps

1. **Clone or download the project**

   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Install Playwright browser kernel**

   ```bash
   playwright install chromium
   ```

### Usage Instructions

1. **Run the tool**

   ```bash
   python html2img_python_ultimate.py
   ```

2. **Import files**

   - Click "Add Files": Select single or multiple HTML files
   - Click "Add Folder": Select a folder containing HTML files for batch import

3. **Preview files**

   - Click any file in the file list to view HTML content in the preview area

4. **Open source files**

   - Select the opening method from the "Open With" dropdown menu
   - Click "Open Selected File" to open the source file with the selected method

5. **Set export parameters**

   - Format: Select PNG or JPG
   - Width: Enter image width (default 1200px)
   - Quality: Enter image quality (0-100, default 90)

6. **Export images**

   - Check the files to export
   - Click "Batch Export"
   - After export, images will be saved in the `output` folder under the project directory

### FAQ

**Q: Where are the exported images?**

A: Images are uniformly saved in the `output` folder under the project directory, and the specific path will be displayed in a pop-up after export.

**Q: Local images cannot be displayed?**

A: The tool will automatically convert local images in HTML to Base64 format to ensure normal display.

**Q: How to switch dark mode?**

A: Click the "Dark Mode" button to switch between dark/light themes with one click.

### License

MIT License