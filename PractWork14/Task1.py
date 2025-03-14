import tkinter as tk

def login():
    login_value = entry_login.get()
    password_value = entry_password.get()
    remember = var_remember.get()
    print(f"Login: {login_value}, Password: {password_value}, Remember: {remember}")

root = tk.Tk()
root.title("Авторизация")
root.geometry("200x300")

label_login = tk.Label(root, text="Логин")
label_login.pack(pady=5)
entry_login = tk.Entry(root)
entry_login.pack(pady=5)

label_password = tk.Label(root, text="Пароль")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

var_remember = tk.IntVar()
checkbox_remember = tk.Checkbutton(root, text="Запомнить пароль", variable=var_remember)
checkbox_remember.pack(pady=5)

button_login = tk.Button(root, text="Авторизоваться", command=login)
button_login.pack(pady=20)

root.mainloop()
