import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD


def path_get():

    def on_drop(event):
        nonlocal file_path
        file_path = event.data
        file_path_label.config(text=f"文件路径: {file_path}")
        # print(file_path)

    root = TkinterDnD.Tk()

    root.title("文件路径获取")

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack()

    file_path_label = tk.Label(frame, text="拖拽文件到此处")
    file_path_label.pack()

    frame.drop_target_register(DND_FILES)
    frame.dnd_bind('<<Drop>>', on_drop)

    file_path = None

    root.mainloop()
    return file_path

