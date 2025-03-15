import os
from tkinter import *
from tkinter import ttk, messagebox, filedialog, simpledialog
from datetime import datetime
import glob

# Функция для поиска файлов в директории
def search_files():
    directory = filename_entry.get()  # Получаем путь из поля ввода
    if os.path.isdir(directory):
        files = os.listdir(directory)
        update_file_list(directory, files)
    else:
        update_file_list("", [])

# Обновление списка файлов в дереве
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

# Создание нового файла
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

# Удаление файла
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

# Функция для поиска файлов по маске
def search_files_by_mask(directory, mask):
    return glob.glob(os.path.join(directory, mask))

# Функция для создания контекстного меню
def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)

# Настройка интерфейса
root = Tk()
root.title("Файловый менеджер")
root.geometry("1000x600")

# Поле для ввода пути директории
filename_entry = Entry(root, width=50)
filename_entry.grid(column=1, row=1, columnspan=3)

# Кнопки
search_button = Button(root, text="🔍 Поиск", command=search_files)
search_button.grid(column=4, row=1)

create_button = Button(root, text="Создать файл", command=create_file)
create_button.grid(column=5, row=1)

delete_button = Button(root, text="Удалить файл", command=delete_file)
delete_button.grid(column=6, row=1)

# Контекстное меню
context_menu = Menu(root, tearoff=0)
context_menu.add_command(label="Копировать")
context_menu.add_command(label="Вставить")

# Настроим деревья для отображения файлов
tree = ttk.Treeview(root, columns=("Расширение", "Размер (байт)", "Дата изменения"), show='headings')
tree.heading("#1", text="Имя файла")
tree.heading("Расширение", text="Расширение")
tree.heading("Размер (байт)", text="Размер (байт)")
tree.heading("Дата изменения", text="Дата изменения")
tree.grid(column=1, row=3, columnspan=5, sticky='nsew')

# Обновление списка файлов при запуске
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()
