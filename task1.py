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


import os
from tkinter import *
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime

def search_files():
    search_term = filename_entry.get()
    if os.path.isdir(search_term):
        files = os.listdir(search_term)
        update_file_list(search_term, files)
    else:
        update_file_list("", [])

def update_file_list(directory, files):
    for item in tree.get_children():
        tree.delete(item)
    for file in files:
        file_path = os.path.join(directory, file)
        file_info = os.stat(file_path)
        file_size = file_info.st_size
        file_mtime = datetime.fromtimestamp(file_info.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
        file_extension = os.path.splitext(file)[1]
        tree.insert('', 'end', text=file, values=(file_extension, file_size, file_mtime))

def create_file():
    file_name = simpledialog.askstring("Создать файл", "Введите имя файла:")
    if file_name:
        try:
            with open(file_name, 'w') as f:
                f.write("")  # Создаем пустой файл
            messagebox.showinfo("Успех", f"Файл '{file_name}' успешно создан.")
            search_files()  # Обновляем список файлов
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

def delete_file():
    selected_item = tree.selection()
    if selected_item:
        file_name = tree.item(selected_item, 'text')
        directory = filename_entry.get()
        file_path = os.path.join(directory, file_name)
        try:
            os.remove(file_path)
            messagebox.showinfo("Успех", f"Файл '{file_name}' успешно удален.")
            search_files()  # Обновляем список файлов
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
    else:
        messagebox.showwarning("Предупреждение", "Выберите файл для удаления.")

def copy_text(event=None):
    root.clipboard_clear()
    root.clipboard_append(filename_entry.get())

def paste_text(event=None):
    filename_entry.delete(0, END)
    filename_entry.insert(0, root.clipboard_get())

def select_all(event=None):
    filename_entry.select_range(0, END)
    filename_entry.icursor(END)

def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)

root = Tk()
root.title("Файловый менеджер")
root.geometry("1000x1000")

back_button = Button(root, text="↶")
back_button.grid(column=1, row=1)

forward_button = Button(root, text="↷")
forward_button.grid(column=2, row=1)

filename_entry = Entry(root, width=50)
filename_entry.grid(column=3, row=1, columnspan=3)

search_button = Button(root, text="🔍", command=search_files)
search_button.grid(column=6, row=1)

create_button = Button(root, text="Создать файл", command=create_file)
create_button.grid(column=7, row=1)

delete_button = Button(root, text="Удалить файл", command=delete_file)
delete_button.grid(column=8, row=1)

context_menu = Menu(root, tearoff=0)
context_menu.add_command(label="Копировать", command=copy_text)
context_menu.add_command(label="Вставить", command=paste_text)

filename_entry.bind("<Button-3>", show_context_menu)
filename_entry.bind("<Control-c>", copy_text)
filename_entry.bind("<Control-v>", paste_text)
filename_entry.bind("<Control-a>", select_all)

tree = ttk.Treeview(root, columns=("Расширение", "Размер (байт)", "Дата изменения"), show='headings')
tree.heading("#1", text="Имя файла")
tree.heading("Расширение", text="Расширение")
tree.heading("Размер (байт)", text="Размер (байт)")
tree.heading("Дата изменения", text="Дата изменения")
tree.grid(column=1, row=3, columnspan=6, sticky='nsew')

root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()
