import tkinter as tk

def on_key_press(event):
    label.config(text=f"Нажатая клавиша: {event.char}")

root = tk.Tk()
root.title("Нажатая клавиша")
root.geometry("300x400")

label = tk.Label(root, text="Нажатая клавиша:")
label.pack(padx=10, pady=10)

root.bind("<Key>", on_key_press)

root.mainloop()
