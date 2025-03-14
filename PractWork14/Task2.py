import tkinter as tk

def register():
    login_value = entry_login.get()
    password_value = entry_password.get()
    about_value = text_about.get("1.0", "end-1c")
    gender_value = gender_var.get()
    continent_value = continent_var.get()
    print(f"Login: {login_value}, Password: {password_value}, About: {about_value}, Gender: {gender_value}, Continent: {continent_value}")

root = tk.Tk()
root.title("Регистрация")
root.geometry("400x600")
root.configure(bg="lightblue")

label_login = tk.Label(root, text="Логин", bg="lightblue")
label_login.pack(pady=5)
entry_login = tk.Entry(root)
entry_login.pack(pady=5)

label_password = tk.Label(root, text="Пароль", bg="lightblue")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)


label_about = tk.Label(root, text="О себе", bg="lightblue")
label_about.pack(pady=5)
text_about = tk.Text(root, height=4, width=30)
text_about.pack(pady=5)

gender_var = tk.StringVar()
label_gender = tk.Label(root, text="Пол", bg="lightblue")
label_gender.pack(pady=5)
radio_male = tk.Radiobutton(root, text="Мужчина", variable=gender_var, value="Мужчина", bg="lightblue")
radio_female = tk.Radiobutton(root, text="Женщина", variable=gender_var, value="Женщина", bg="lightblue")
radio_male.pack()
radio_female.pack()

label_continent = tk.Label(root, text="Материк", bg="lightblue")
label_continent.pack(pady=5)
continent_var = tk.StringVar()
continent_list = tk.OptionMenu(root, continent_var, "Азия", "Европа", "Америка", "Африка", "Австралия")
continent_list.pack(pady=5)

button_register = tk.Button(root, text="Зарегистрироваться", command=register)
button_register.pack(pady=20)

root.mainloop()
