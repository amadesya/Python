import os
from tkinter import *
from tkinter import ttk, messagebox, filedialog, simpledialog
from datetime import datetime
import glob

# Функция сортировки
def sort_treeview(treeview, column, reverse=False):
    """Сортировка столбцов в Treeview."""
    items = list(treeview.get_children())
    items.sort(key=lambda x: treeview.item(x, "values")[column], reverse=reverse)
    
    for index, item in enumerate(items):
        treeview.move(item, '', index)
    
    return not reverse  # Возвращаем обратный порядок сортировки

# Обработчики кликов по заголовкам
def on_treeview_column_click(event, treeview, column):
    """Обработчик кликов по заголовкам столбцов."""
    global reverse_order
    reverse_order = sort_treeview(treeview, column, reverse=reverse_order)

def search_files():
    directory = filename_entry.get()
    if os.path.isdir(directory):
        files = os.listdir(directory)
        update_file_list(directory, files)
    else:
        update_file_list("", [])

def update_file_list(directory, files):
    for item in tree.get_children():
        tree.delete(item)
    for file in files:
        file_name = os.path.splitext(file)[0]
        file_path = os.path.join(directory, file)
        file_info = os.stat(file_path)
        file_size = file_info.st_size
        file_mtime = datetime.fromtimestamp(file_info.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
        file_extension = os.path.splitext(file)[1]
        tree.insert('', 'end', text=file, values=(file_name, file_extension, file_size, file_mtime))

def create_file():
    directory = filedialog.askdirectory(title="Выберите папку для создания файла")
    if directory:
        file_name = simpledialog.askstring("Создать файл", "Введите имя файла:")
        if file_name:
            file_path = os.path.join(directory, file_name)
            try:
                with open(file_path, 'w') as f:
                    f.write("")
                messagebox.showinfo("Успех", f"Файл '{file_name}' успешно создан в папке {directory}.")
                search_files()
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
            search_files()
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
    else:
        messagebox.showwarning("Предупреждение", "Выберите файл для удаления.")

def search_files_by_mask(directory, mask):
    return glob.glob(os.path.join(directory, mask))

def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)

root = Tk()
root.title("Файловый менеджер")
root.geometry("1000x600")

filename_entry = Entry(root, width=50)
filename_entry.grid(column=1, row=1, columnspan=3)

search_button = Button(root, text="🔍 Поиск", command=search_files)
search_button.grid(column=4, row=1)

create_button = Button(root, text="Создать файл", command=create_file)
create_button.grid(column=5, row=1)

delete_button = Button(root, text="Удалить файл", command=delete_file)
delete_button.grid(column=6, row=1)

context_menu = Menu(root, tearoff=0)
context_menu.add_command(label="Создать файл", command=create_file)
context_menu.add_command(label="Удалить файл", command=delete_file)

# Инициализация Treeview
tree = ttk.Treeview(root, columns=("Имя файла", "Расширение", "Размер (байт)", "Дата изменения"), show='headings')

# Определение заголовков
tree.heading("Имя файла", text="Имя файла", command=lambda: on_treeview_column_click(event=None, treeview=tree, column=0))
tree.heading("Расширение", text="Расширение", command=lambda: on_treeview_column_click(event=None, treeview=tree, column=1))
tree.heading("Размер (байт)", text="Размер (байт)", command=lambda: on_treeview_column_click(event=None, treeview=tree, column=2))
tree.heading("Дата изменения", text="Дата изменения", command=lambda: on_treeview_column_click(event=None, treeview=tree, column=3))

# Размещение Treeview
tree.grid(column=1, row=3, columnspan=5, sticky='nsew')

# Привязка контекстного меню
tree.bind("<Button-3>", show_context_menu)

root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(1, weight=1)

# Инициализация переменной для отслеживания порядка сортировки
reverse_order = False

root.mainloop()
