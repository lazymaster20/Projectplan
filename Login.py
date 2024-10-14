import tkinter as tk
from tkinter import messagebox

page = tk.Tk()
page.title("login form")
page.geometry("500x800")
page.configure(bg='#444444')
def login():
    username = "aru"
    password = "12345"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login successful", message='you successfully logged in')
    else:
        messagebox.showerror(title="Error", message='Invalid login')


frame=tk.Frame(bg='#333333')

login_label=tk.Label(frame, text="Login", bg='#333333', fg='#FFFFFF', font=('Arial', 30))
username_label=tk.Label(frame, text="User Name", bg='#333333', fg='#FFFFFF', font=('Arial', 16))
username_entry=tk.Entry(frame, font=('Arial', 16))
password_entry=tk.Entry(frame, show="*", font=('Arial', 16))
password_label=tk.Label(frame, text="Password", bg='#333333', fg='#FFFFFF', font=('Arial', 16))
login_button=tk.Button(frame, text="Login", bg='#FF3333', fg='#FFFFFF', font=('Arial', 16), command=login)

login_label.grid(row=0, column=0, columnspan=2, pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3,column=0,columnspan=2, pady=30)

frame.pack()
page.mainloop()
