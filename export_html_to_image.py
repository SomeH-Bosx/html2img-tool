import base64
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
from playwright.sync_api import sync_playwright
import webbrowser
import subprocess
import os

# ==================== 工具函数 ====================
def img_to_base64(img_path):
    try:
        with open(img_path, "rb") as f:
            data = f.read()
        enc = base64.b64encode(data).decode()
        ext = img_path.suffix.lower().lstrip(".")
        ext = "jpeg" if ext == "jpg" else ext
        return f"data:image/{ext};base64,{enc}"
    except Exception:
        return ""

def fix_html_images(html_path: Path):
    content = html_path.read_text(encoding="utf-8", errors="ignore")
    folder = html_path.parent
    for img in folder.glob("*"):
        suf = img.suffix.lower()
        if suf in (".jpg", ".jpeg", ".png", ".gif", ".svg"):
            b64 = img_to_base64(img)
            content = content.replace(f'src="{img.name}"', f'src="{b64}"')
    return content

# ==================== 导出图片（已修复报错） ====================
def export_image(html_content, out_path, fmt="png", width=1200, quality=90):
    try:
        print("🖼️  导出图片到:", out_path)
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.set_content(html_content)
            page.wait_for_timeout(800)

            # 修复：必须传字典
            page.set_viewport_size({"width": width, "height": 1080})

            page.screenshot(
                path=out_path,
                full_page=True,
                type=fmt,
                quality=quality if fmt == "jpeg" else None
            )
            browser.close()
        return True
    except Exception as e:
        print("导出错误:", e)
        return False

# ==================== 打开方式列表 ====================
def get_open_apps():
    return [
        ("默认浏览器", "browser"),
        ("新标签页预览", "newtab"),
        ("记事本打开", "notepad"),
        ("VS Code 打开", "vscode"),
        ("下载源文件", "download"),
        ("打开文件所在文件夹", "folder"),
    ]

# ==================== 主界面 ====================
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("HTML 转图片 · 最终完美版")
        self.geometry("940x760")
        self.is_dark = False

        self.light = {
            "bg": "#ffffff",
            "card": "#f9fafb",
            "border": "#e5e7eb",
            "text": "#111827",
            "accent": "#2563eb",
            "danger": "#ef4444",
            "gray": "#6b7280"
        }
        self.dark = {
            "bg": "#111827",
            "card": "#1f2937",
            "border": "#374151",
            "text": "#f9fafb",
            "accent": "#3b82f6",
            "danger": "#f87171",
            "gray": "#9ca3af"
        }
        self.theme = self.light

        self.files = []
        self.current = None
        self.app_list = get_open_apps()

        self.style = ttk.Style()
        self.style.configure("Panel.TFrame", background=self.theme["card"])

        # 主容器
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # 标题
        ttk.Label(self.main_frame, text="📷 HTML 转图片 · 完整版", font=("Arial", 16, "bold")).pack(pady=10)

        # ========== 面板1：文件导入 ==========
        self.panel1 = ttk.Frame(self.main_frame, style="Panel.TFrame", padding=15, relief=tk.GROOVE, borderwidth=1)
        self.panel1.pack(fill=tk.X, pady=5)
        ttk.Label(self.panel1, text="文件导入", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="w")
        ttk.Button(self.panel1, text="添加文件", command=self.add_files).grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(self.panel1, text="添加文件夹", command=self.add_folder).grid(row=1, column=1, padx=5)
        ttk.Button(self.panel1, text="删除选中", command=self.delete_selected).grid(row=1, column=2, padx=5)
        self.theme_btn = ttk.Button(self.panel1, text="深色模式", command=self.toggle_theme)
        self.theme_btn.grid(row=1, column=3, padx=5)

        # ========== 面板2：打开方式 ==========
        self.panel2 = ttk.Frame(self.main_frame, style="Panel.TFrame", padding=15, relief=tk.GROOVE, borderwidth=1)
        self.panel2.pack(fill=tk.X, pady=5)
        ttk.Label(self.panel2, text="打开方式", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="w")
        self.app_var = tk.StringVar()
        app_names = [n for n, _ in self.app_list]
        self.app_combo = ttk.Combobox(self.panel2, textvariable=self.app_var, values=app_names, width=22)
        self.app_combo.grid(row=1, column=0, padx=5)
        if app_names:
            self.app_combo.current(0)
        ttk.Button(self.panel2, text="打开选中文件", command=self.open_file).grid(row=1, column=1, padx=5)

        # ========== 面板3：导出设置 ==========
        self.panel3 = ttk.Frame(self.main_frame, style="Panel.TFrame", padding=15, relief=tk.GROOVE, borderwidth=1)
        self.panel3.pack(fill=tk.X, pady=5)
        ttk.Label(self.panel3, text="导出设置", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=6, sticky="w")

        ttk.Label(self.panel3, text="格式:").grid(row=1, column=0)
        self.fmt_var = tk.StringVar(value="png")
        ttk.Combobox(self.panel3, textvariable=self.fmt_var, values=["png", "jpg"], width=5).grid(row=1, column=1, padx=3)

        ttk.Label(self.panel3, text="宽度:").grid(row=1, column=2)
        self.w_var = tk.StringVar(value="1200")
        ttk.Entry(self.panel3, textvariable=self.w_var, width=6).grid(row=1, column=3, padx=3)

        ttk.Label(self.panel3, text="质量:").grid(row=1, column=4)
        self.q_var = tk.StringVar(value="90")
        ttk.Entry(self.panel3, textvariable=self.q_var, width=6).grid(row=1, column=5, padx=3)

        ttk.Button(self.panel3, text="批量导出", command=self.do_export).grid(row=1, column=6, padx=10)

        # ========== 面板4：文件列表 ==========
        self.panel4 = ttk.Frame(self.main_frame, style="Panel.TFrame", padding=15, relief=tk.GROOVE, borderwidth=1)
        self.panel4.pack(fill=tk.BOTH, expand=True, pady=5)
        ttk.Label(self.panel4, text="文件列表（点击预览）", font=("Arial", 12, "bold")).pack(anchor="w")
        self.listbox = tk.Listbox(self.panel4, width=110, height=10, font=("Consolas", 10))
        self.listbox.pack(fill=tk.BOTH, expand=True, pady=5)
        self.listbox.bind("<<ListboxSelect>>", self.on_click)

        # ========== 面板5：预览信息 ==========
        self.panel5 = ttk.Frame(self.main_frame, style="Panel.TFrame", padding=15, relief=tk.GROOVE, borderwidth=1)
        self.panel5.pack(fill=tk.X, pady=5)
        ttk.Label(self.panel5, text="预览信息", font=("Arial", 12, "bold")).pack(anchor="w")
        self.preview = tk.Text(self.panel5, height=4, state="disabled", font=("Consolas", 9))
        self.preview.pack(fill=tk.X, pady=5)

        # ========== 进度条 ==========
        self.pb = ttk.Progressbar(self.main_frame, length=880)
        self.pb.pack(fill=tk.X, pady=2)
        self.pb_lab = ttk.Label(self.main_frame, text="0%")
        self.pb_lab.pack()

        self.apply_theme()

    # ========== 主题 ==========
    def toggle_theme(self):
        self.is_dark = not self.is_dark
        self.theme = self.dark if self.is_dark else self.light
        self.theme_btn.config(text="浅色模式" if self.is_dark else "深色模式")
        self.apply_theme()

    def apply_theme(self):
        self.config(bg=self.theme["bg"])
        self.style.configure("Panel.TFrame", background=self.theme["card"])
        for w in self.main_frame.winfo_children():
            try:
                w.config(background=self.theme["card"], foreground=self.theme["text"])
            except:
                pass

    # ========== 文件操作 ==========
    def add_files(self):
        paths = filedialog.askopenfilenames(filetypes=[("HTML 文件", "*.html;*.htm")])
        for p in paths:
            if not any(f["path"] == p for f in self.files):
                self.files.append({"path": p, "name": Path(p).name, "check": True})
        self.refresh_list()

    def add_folder(self):
        folder = filedialog.askdirectory()
        if not folder:
            return
        paths = list(Path(folder).glob("*.html")) + list(Path(folder).glob("*.htm"))
        for p in paths:
            s = str(p)
            if not any(f["path"] == s for f in self.files):
                self.files.append({"path": s, "name": p.name, "check": True})
        self.refresh_list()

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for f in self.files:
            prefix = "✅ " if f["check"] else "⬜ "
            self.listbox.insert(tk.END, f"{prefix}{f['name']}")

    def on_click(self, e):
        sel = self.listbox.curselection()
        if not sel:
            return
        idx = sel[0]
        self.current = self.files[idx]
        self.current["check"] = not self.current["check"]
        self.refresh_list()
        self.listbox.selection_set(idx)
        self.show_preview()

    def show_preview(self):
        path = self.current["path"]
        info = f"文件: {self.current['name']}\n路径: {path}\n图片已自动转为 Base64"
        self.preview.config(state="normal")
        self.preview.delete(1.0, tk.END)
        self.preview.insert(1.0, info)
        self.preview.config(state="disabled")

    # ========== 打开方式 ==========
    def open_file(self):
        if not self.current:
            messagebox.showwarning("提示", "请先选择一个文件")
            return

        path = self.current["path"]
        app_name = self.app_var.get()
        key = next((k for n, k in self.app_list if n == app_name), None)

        try:
            if key == "browser":
                webbrowser.open(path)
            elif key == "newtab":
                webbrowser.open_new_tab(path)
            elif key == "notepad":
                os.startfile(path, "open")
            elif key == "vscode":
                subprocess.Popen(["code", path], shell=True)
            elif key == "download":
                folder = os.path.dirname(path)
                subprocess.Popen(f'explorer "{folder}"', shell=True)
            elif key == "folder":
                subprocess.Popen(f'explorer /select,"{path}"', shell=True)
        except Exception as e:
            messagebox.showerror("错误", f"打开失败：{str(e)}")

    def delete_selected(self):
        before = len(self.files)
        self.files = [f for f in self.files if not f["check"]]
        after = len(self.files)
        self.refresh_list()
        self.current = None
        messagebox.showinfo("完成", f"已删除 {before - after} 个文件")

    # ========== 导出（统一输出到 output 文件夹） ==========
    def do_export(self):
        selected = [f for f in self.files if f["check"]]
        if not selected:
            messagebox.showwarning("提示", "请勾选要导出的文件")
            return

        fmt = self.fmt_var.get()
        width = int(self.w_var.get() or 1200)
        quality = int(self.q_var.get() or 90)
        total = len(selected)

        output_dir = Path("./output")
        output_dir.mkdir(exist_ok=True)

        for i, f in enumerate(selected):
            html_path = Path(f["path"])
            fixed = fix_html_images(html_path)
            out_path = output_dir / f"{html_path.stem}.{fmt}"
            export_image(fixed, str(out_path), fmt, width, quality)

            self.pb["value"] = (i + 1) / total * 100
            self.pb_lab.config(text=f"{i+1}/{total}")
            self.update()

        messagebox.showinfo("完成", f"✅ 导出成功！\n文件保存在：\n{output_dir.resolve()}")

if __name__ == "__main__":
    App().mainloop()