import tkinter as tk

def update_label():
    label_text.set(f"Логин: {login_var.get()}, Пол: {gender_var.get()}, Запомнить пароль: {remember_var.get()}")

root = tk.Tk()
root.title("Связывание виджетов")
root.geometry("400x400")

login_var = tk.StringVar()
gender_var = tk.StringVar()
remember_var = tk.IntVar()

label_login = tk.Label(root, text="Логин")
label_login.pack(pady=5)
entry_login = tk.Entry(root, textvariable=login_var)
entry_login.pack(pady=5)

label_gender = tk.Label(root, text="Пол")
label_gender.pack(pady=5)
radio_male = tk.Radiobutton(root, text="Мужчина", variable=gender_var, value="Мужчина")
radio_female = tk.Radiobutton(root, text="Женщина", variable=gender_var, value="Женщина")
radio_male.pack()
radio_female.pack()

checkbox_remember = tk.Checkbutton(root, text="Запомнить пароль", variable=remember_var)
checkbox_remember.pack(pady=5)

button_update = tk.Button(root, text="Обновить", command=update_label)
button_update.pack(pady=10)

label_text = tk.StringVar()
label = tk.Label(root, textvariable=label_text)
label.pack(pady=10)

root.mainloop()
