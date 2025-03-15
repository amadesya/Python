import os
import tkinter as tk
from tkinter import filedialog, messagebox
import glob
from datetime import datetime

def open_file_dialog():
    return filedialog.askopenfilename()

def open_directory_dialog():
    return filedialog.askdirectory()

def on_create_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[
            ("Text files", "*.txt"),
            ("Python files", "*.py"),
            ("HTML files", "*.html"),
            ("CSS files", "*.css"),
            ("JavaScript files", "*.js"),
            ("Markdown files", "*.md"),
            ("CSV files", "*.csv"),
            ("Image files", "*.png;*.jpg;*.jpeg;*.gif"),
            ("All files", "*.*")
        ]
    )
    if file_path:
        create_file(file_path)

def on_delete_file():
    file_path = open_file_dialog().askopenfilename(title="Удалить")
    if file_path:
        delete_file(file_path)

def on_rename_file():
    old_path = open_file_dialog()
    if old_path:
        new_path = filedialog.asksaveasfilename(defaultextension=os.path.splitext(old_path)[1], filetypes=[("All files", "*.*")])
        if new_path:
            rename_file(old_path, new_path)

def on_search_files():
    directory = open_directory_dialog()
    if directory:
        mask = input("Введите маску для поиска (например, *.txt): ")
        files = search_files_by_mask(directory, mask)
        if files:
            messagebox.showinfo("Результаты поиска", f'Найдено файлов: {len(files)}\n' + "\n".join(files))
        else:
            messagebox.showinfo("Результаты поиска", "Файлы не найдены.")

def create_gui():
    root = tk.Tk()
    root.title("Файловый менеджер")

    tk.Button(root, text="Создать файл", command=on_create_file).pack(pady=5)
    tk.Button(root, text="Удалить файл", command=on_delete_file).pack(pady=5)
    tk.Button(root, text="Переименовать файл", command=on_rename_file).pack(pady=5)
    tk.Button(root, text="Поиск файлов", command=on_search_files).pack(pady=5)

    root.mainloop()

def create_file(file_path):
    try:
        with open(file_path, 'w') as file:
            file.write('')  # Пустой файл
        messagebox.showinfo("Создание файла", f'Файл {file_path} успешно создан.')
    except Exception as e:
        messagebox.showerror("Ошибка", f'Ошибка при создании файла: {e}')

def delete_file(file_path):
    try:
        os.remove(file_path)
        messagebox.showinfo("Удаление файла", f'Файл {file_path} удален.')
    except Exception as e:
        messagebox.showerror("Ошибка", f'Ошибка при удалении файла: {e}')

def rename_file(old_path, new_path):
    try:
        os.rename(old_path, new_path)
        messagebox.showinfo("Переименование файла", f'Файл {old_path} переименован в {new_path}.')
    except Exception as e:
        messagebox.showerror("Ошибка", f'Ошибка при переименовании файла: {e}')

def search_files_by_mask(directory, mask):
    return glob.glob(os.path.join(directory, mask))

def search_files_by_extension(directory, extension):
    return glob.glob(os.path.join(directory, f"*.{extension}"))

def search_files_by_date(directory, start_date, end_date):
    result = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_timestamp = os.path.getmtime(file_path)
            file_date = datetime.fromtimestamp(file_timestamp)
            if start_date <= file_date <= end_date:
                result.append(file_path)
    return result

def search_files_by_size(directory, min_size, max_size):
    result = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            if min_size <= file_size <= max_size:
                result.append(file_path)
    return result

if __name__ == "__main__":
    create_gui()
