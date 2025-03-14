import tkinter as tk
from tkinter import filedialog

def save_file():
    text = text_widget.get("1.0", tk.END)
    file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file:
        file.write(text)
        file.close()

def close_window(event):
    root.quit()

root = tk.Tk()
root.title("Приложение для сохранения текста")
root.geometry("800x800")

text_widget = tk.Text(root, wrap=tk.WORD)
text_widget.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

save_button = tk.Button(root, text="Сохранить", command=save_file)
save_button.pack(pady=5)

root.bind("<Control-s>", lambda e: save_file())  # Ctrl+S
root.bind("<Escape>", close_window)  # Esc

root.mainloop()
