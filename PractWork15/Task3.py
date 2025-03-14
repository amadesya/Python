import tkinter as tk

def update_coordinates(event):
    label.config(text=f"Координаты мыши: ({event.x}, {event.y})")

root = tk.Tk()
root.title("Координаты мыши")
root.geometry("300x400")

label = tk.Label(root, text="Координаты мыши: (0, 0)")
label.pack(padx=10, pady=10)

root.bind("<Motion>", update_coordinates)

root.mainloop()
