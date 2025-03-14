import tkinter as tk

def change_color(color):
    root.configure(bg=color)

def change_size(size):
    root.geometry(size)

root = tk.Tk()
root.title("Меню с горячими клавишами")
root.geometry("500x500")

menu_bar = tk.Menu(root)

color_menu = tk.Menu(menu_bar, tearoff=0)
color_menu.add_command(label="Red", command=lambda: change_color("red"))
color_menu.add_command(label="Green", command=lambda: change_color("green"))
color_menu.add_command(label="Blue", command=lambda: change_color("blue"))
menu_bar.add_cascade(label="Color", menu=color_menu)

size_menu = tk.Menu(menu_bar, tearoff=0)
size_menu.add_command(label="500x500", command=lambda: change_size("500x500"))
size_menu.add_command(label="700x400", command=lambda: change_size("700x400"))
menu_bar.add_cascade(label="Size", menu=size_menu)

root.config(menu=menu_bar)

root.bind("<Control-r>", lambda e: change_color("red")) #Ctrl+R
root.bind("<Control-g>", lambda e: change_color("green")) #Ctrl+G
root.bind("<Control-b>", lambda e: change_color("blue")) #Ctrl+B
root.bind("<Control-q>", lambda e: change_size("500x500")) #Ctrl+Q
root.bind("<Control-w>", lambda e: change_size("700x400")) #Ctrl+W

root.mainloop()