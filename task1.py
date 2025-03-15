import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    return filedialog.askopenfilename()

def open_directory_dialog():
    return filedialog.askdirectory()

def on_create_file():
    file_path = filedialog.asksaveasfilename()
    if file_path:
        create_file(file_path)

def on_delete_file():
    file_path = open_file_dialog()
    if file_path:
        delete_file(file_path)

def on_rename_file():
    old_path = open_file_dialog()
    if old_path:
        new_path = filedialog.asksaveasfilename()
        if new_path:
            rename_file(old_path, new_path)

def on_search_files():
    directory = open_directory_dialog()
    if directory:
        mask = input("Введите маску для поиска: ")
        files = search_files_by_mask(directory, mask)
        print(f'Найдено файлов: {len(files)}')
        for file in files:
            print(file)

def create_gui():
    root = tk.Tk()
    root.title("Файловый менеджер")

    tk.Button(root, text="Создать файл", command=on_create_file).pack()
    tk.Button(root, text="Удалить файл", command=on_delete_file).pack()
    tk.Button(root, text="Переименовать файл", command=on_rename_file).pack()
    tk.Button(root, text="Поиск файлов", command=on_search_files).pack()

    root.mainloop()

if __name__ == "__main__":
    create_gui()
