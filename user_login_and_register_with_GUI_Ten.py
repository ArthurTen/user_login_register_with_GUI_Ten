import sqlite3
import customtkinter
import tkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

app = customtkinter.CTk()
app.title('Тен Авторизация')
app.geometry('400x430')
app.resizable(False, False)

def create_table():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

create_table()

def save_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (username, password)
        VALUES (?, ?)
    ''', (username, password))
    conn.commit()
    conn.close()
    result_label.configure(text='Пользователь успешно сохранен!')

def login_user():
    username = login_entry.get("1.0", tkinter.END).strip()  
    password = passwd_entry.get("1.0", tkinter.END).strip()
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        result_label1.configure(text=f'Добро пожаловать, {user[1]}!') 
        print(f'Добро пожаловать, {user[1]}!')
    else:
        result_label1.configure(text='Неправильный логин или пароль!')       
        
result_label1=customtkinter.CTkLabel(master=app, text='')
result_label1.place(relx=0.30, rely=0.8)

login_entry = customtkinter.CTkTextbox(master=app, height=30, width=120)
login_entry.place(relx=0.37, rely=0.2)

passwd_entry = customtkinter.CTkTextbox(master=app, height=30, width=120)
passwd_entry.place(relx=0.37, rely=0.37)

def register_user():
    username = new_login_entry.get("1.0", tkinter.END).strip()  
    password = new_password_entry.get("1.0", tkinter.END).strip() 
    if username and password:
        save_user(username, password)
        new_login_entry.delete("1.0", tkinter.END)  
        new_password_entry.delete("1.0", tkinter.END)  
    else:
        result_label.configure(text='Заполните все поля!')

label1 = customtkinter.CTkLabel(master=app, height=15, width=120, text="Введите логин").place(relx=0.37, rely=0.15)
label2 = customtkinter.CTkLabel(master=app, height=15, width=120, text="Введите пароль").place(relx=0.37, rely=0.32)

signin_button = customtkinter.CTkButton(master=app, height=30, width=120, text='Войти', command=login_user).place(relx=0.37, rely=0.47)


def clear_function():
    login_entry.delete("1.0", tkinter.END)
    passwd_entry.delete("1.0", tkinter.END)

clear_button = customtkinter.CTkButton(master=app, height=30, width=90, text='Очистить', command=clear_function)
clear_button.place(relx=0.75, rely=0.47)

def open_signup_window():
    app1 = customtkinter.CTk()
    app1.title('Пройти регистрацию')
    app1.geometry('400x430')
    app1.resizable(False, False)
    
    global new_login_entry
    global new_password_entry
    global result_label
    
    new_login_entry = customtkinter.CTkTextbox(master=app1, height=30, width=120)
    new_login_entry.place(relx=0.37, rely=0.2)
    new_password_entry = customtkinter.CTkTextbox(master=app1, height=30, width=120)
    new_password_entry.place(relx=0.37, rely=0.37)
    
    result_label = customtkinter.CTkLabel(master=app1, text='')
    result_label.place(relx=0.37, rely=0.67)
    
    label3 = customtkinter.CTkLabel(master=app1, height=15, width=120, text="Введите новый логин").place(relx=0.35, rely=0.15)
    label4 = customtkinter.CTkLabel(master=app1, height=15, width=120, text="Введите новый пароль").place(relx=0.35, rely=0.32)

    signup_button = customtkinter.CTkButton(master=app1, height=30, width=120, text='Сохранить пользователя', command=register_user)
    signup_button.place(relx=0.31, rely=0.6)
    
    app1.mainloop()
    
signup_open_window = customtkinter.CTkButton(master=app, height=30, width=120, text='Зарегистрироваться', command=open_signup_window)
signup_open_window.place(relx=0.35, rely=0.6)

app.mainloop()