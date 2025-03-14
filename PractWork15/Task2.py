import tkinter as tk

def on_focus_in(event):
    label.config(text=f"Активное поле: {event.widget._name}")

def on_right_click(event):
    print(f"Правый клик на {event.widget._name}")

root = tk.Tk()
root.title("Приложение с полями ввода")
root.geometry("400x400")

label = tk.Label(root, text="Активное поле: None")
label.pack(pady=10)

entry1 = tk.Entry(root, name="Поле 1")
entry1.pack(pady=5)
entry2 = tk.Entry(root, name="Поле 2")
entry2.pack(pady=5)
entry3 = tk.Entry(root, name="Поле 3")
entry3.pack(pady=5)

entry1.bind("<FocusIn>", on_focus_in)
entry2.bind("<FocusIn>", on_focus_in)
entry3.bind("<FocusIn>", on_focus_in)

root.bind_class("Entry", "<Button-3>", on_right_click)

root.mainloop()
