import os
import threading
import win32com.client as win32
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinterdnd2 import DND_FILES, TkinterDnD

SUPPORTED_EXT = (".xlsx", ".xls", ".docx", ".doc")

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Office → PDF Converter")
        self.root.geometry("950x650")

        self.files = []
        self.output_folder = ""
        self.is_running = False

        self.create_ui()

    # ---------------- UI ----------------
    def create_ui(self):

        tk.Label(self.root, text="Office → PDF Converter",
                 font=("Segoe UI", 18, "bold")).pack(pady=10)

        frame = tk.Frame(self.root)
        frame.pack(fill=tk.BOTH, expand=True)

        self.listbox = tk.Listbox(frame, selectmode=tk.EXTENDED)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.preview = tk.Listbox(frame)
        self.preview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.listbox.bind("<Double-Button-1>", self.open_file)
        self.listbox.bind("<Button-3>", self.show_context_menu)

        self.listbox.drop_target_register(DND_FILES)
        self.listbox.dnd_bind("<<Drop>>", self.drop_files)

        self.menu = tk.Menu(self.root, tearoff=0)
        self.menu.add_command(label="삭제", command=self.delete_selected)

        # 버튼
        btn = tk.Frame(self.root)
        btn.pack(pady=5)

        ttk.Button(btn, text="📂 파일 추가", command=self.add_files).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn, text="📁 폴더 추가", command=self.add_folder).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn, text="🗑 선택 삭제", command=self.delete_selected).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn, text="🧹 전체 삭제", command=self.clear_all).pack(side=tk.LEFT, padx=5)

        # 옵션
        opt = tk.LabelFrame(self.root, text="옵션")
        opt.pack(fill=tk.X, padx=10, pady=10)

        tk.Label(opt, text="접두어").grid(row=0, column=0)
        self.prefix = tk.Entry(opt)
        self.prefix.grid(row=0, column=1)

        tk.Label(opt, text="접미어").grid(row=1, column=0)
        self.suffix = tk.Entry(opt)
        self.suffix.grid(row=1, column=1)

        self.prefix.bind("<KeyRelease>", self.update_preview)
        self.suffix.bind("<KeyRelease>", self.update_preview)

        self.overwrite = tk.BooleanVar()
        tk.Checkbutton(opt, text="덮어쓰기 허용", variable=self.overwrite).grid(row=2, column=0)

        self.auto_open = tk.BooleanVar(value=True)
        tk.Checkbutton(opt, text="완료 후 폴더 열기", variable=self.auto_open).grid(row=2, column=1)

        # 경로 표시
        self.path_label = tk.Label(self.root, text="저장 폴더 선택 필요", fg="blue")
        self.path_label.pack(pady=5)

        ttk.Button(self.root, text="📁 저장 폴더 선택", command=self.select_output).pack()
        ttk.Button(self.root, text="📂 변환 폴더 열기", command=self.open_folder).pack()

        # 진행바
        self.progress = ttk.Progressbar(self.root, length=700)
        self.progress.pack(pady=10)

        self.status = tk.Label(self.root, text="⏸ 변환 대기 중")
        self.status.pack()

        action = tk.Frame(self.root)
        action.pack()

        ttk.Button(action, text="🚀 변환 시작", command=self.start_thread).pack(side=tk.LEFT, padx=5)
        ttk.Button(action, text="⛔ 중단", command=self.stop).pack(side=tk.LEFT, padx=5)

    # ✅ 우클릭
    def show_context_menu(self, event):
        index = self.listbox.nearest(event.y)

        if index not in self.listbox.curselection():
            self.listbox.selection_clear(0, tk.END)
            self.listbox.selection_set(index)

        self.menu.post(event.x_root, event.y_root)

    # ---------------- 파일 추가 ----------------
    def add_files(self):
        files = filedialog.askopenfilenames(
            filetypes=[("Office files", "*.xlsx *.xls *.docx *.doc")]
        )
        for f in files:
            self.add_file(f)

    # ✅ ✅ ✅ ✅ ✅ 핵심 (완전 수정)
    def add_folder(self):
        folder = filedialog.askdirectory()
        if not folder:
            return

        count = 0

        for root_dir, _, files in os.walk(folder):
            for f in files:
                if f.lower().endswith(SUPPORTED_EXT):
                    self.add_file(os.path.join(root_dir, f))
                    count += 1

        messagebox.showinfo("안내", f"{count}개의 파일이 추가되었습니다")

    def add_file(self, path):
        if path not in self.files:
            self.files.append(path)
            self.listbox.insert(tk.END, os.path.basename(path))
        self.update_preview()

    def drop_files(self, event):
        items = self.root.tk.splitlist(event.data)
        for item in items:
            if os.path.isdir(item):
                for root_dir, _, files in os.walk(item):
                    for f in files:
                        if f.lower().endswith(SUPPORTED_EXT):
                            self.add_file(os.path.join(root_dir, f))
            else:
                self.add_file(item)
        self.update_preview()

    # ---------------- 삭제 ----------------
    def delete_selected(self):
        for i in reversed(self.listbox.curselection()):
            self.listbox.delete(i)
            self.files.pop(i)
        self.update_preview()

    def clear_all(self):
        self.files.clear()
        self.listbox.delete(0, tk.END)
        self.preview.delete(0, tk.END)

    # ---------------- Preview ----------------
    def update_preview(self, event=None):
        self.preview.delete(0, tk.END)
        for path in self.files:
            name = os.path.splitext(os.path.basename(path))[0]
            new_name = self.prefix.get() + name + self.suffix.get()
            self.preview.insert(tk.END, new_name + ".pdf")

    def open_file(self, event):
        if self.listbox.curselection():
            os.startfile(self.files[self.listbox.curselection()[0]])

    # ---------------- 경로 ----------------
    def select_output(self):
        folder = filedialog.askdirectory(initialdir=self.output_folder or os.getcwd())
        if folder:
            self.output_folder = folder
            self.path_label.config(text=folder)

    def open_folder(self):
        if self.output_folder and os.path.exists(self.output_folder):
            os.startfile(self.output_folder)

    def stop(self):
        self.is_running = False

    # ---------------- Thread ----------------
    def start_thread(self):
        threading.Thread(target=self.convert).start()

    # ---------------- 변환 ----------------
    def convert(self):

        if not self.files or not self.output_folder:
            messagebox.showwarning("경고", "파일 또는 폴더 선택 필요")
            return

        excel = win32.DispatchEx("Excel.Application")
        word = win32.DispatchEx("Word.Application")

        excel.Visible = False
        word.Visible = False
        excel.DisplayAlerts = False
        word.DisplayAlerts = False

        for path in self.files:
            ext = path.lower().split(".")[-1]

            name = os.path.splitext(os.path.basename(path))[0]
            name = self.prefix.get() + name + self.suffix.get()
            pdf = os.path.join(self.output_folder, name + ".pdf")

            if ext in ["xlsx","xls"]:
                wb = excel.Workbooks.Open(path)
                wb.ExportAsFixedFormat(0, pdf)
                wb.Close(False)

            elif ext in ["doc","docx"]:
                doc = word.Documents.Open(path)
                doc.SaveAs(pdf, FileFormat=17)
                doc.Close(False)

        excel.Quit()
        word.Quit()

        messagebox.showinfo("완료", "변환 완료")


root = TkinterDnD.Tk()
app = App(root)
root.mainloop()
