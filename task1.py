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

import os

def create_file(file_path):
    try:
        with open(file_path, 'w') as file:
            file.write('')  # Пустой файл
        print(f'Файл {file_path} успешно создан.')
    except Exception as e:
        print(f'Ошибка при создании файла: {e}')


def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f'Файл {file_path} удален.')
    except Exception as e:
        print(f'Ошибка при удалении файла: {e}')

def rename_file(old_path, new_path):
    try:
        os.rename(old_path, new_path)
        print(f'Файл {old_path} переименован в {new_path}.')
    except Exception as e:
        print(f'Ошибка при переименовании файла: {e}')


import glob
import time
from datetime import datetime

# Поиск файлов по маске
def search_files_by_mask(directory, mask):
    return glob.glob(os.path.join(directory, mask))

# Поиск файлов по расширению
def search_files_by_extension(directory, extension):
    return glob.glob(os.path.join(directory, f"*.{extension}"))

# Поиск файлов по дате
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

# Поиск файлов по размеру
def search_files_by_size(directory, min_size, max_size):
    result = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            if min_size <= file_size <= max_size:
                result.append(file_path)
    return result


