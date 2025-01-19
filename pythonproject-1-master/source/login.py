

from tkinter import *
#from functools import partial
from tkinter import *
from functools import partial
from tkinter import messagebox
import sqlite3
from tkinter import *
from movieimagge import *
from radio import onClickLogin
#from functools import partial

conn=sqlite3.connect('user.db')
c=conn.cursor()


def login_user(screen):
    username_info = username.get()
    password_info = password.get()

    # Fetch the password from the database
    c.execute('''SELECT passwd FROM user WHERE name = ?''', (username_info,))
    a = c.fetchone()

    if a is None:
        # Handle case when the username is not found in the database
        messagebox.showinfo('ERROR', 'User not found')
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        return

    # `a` is a tuple; extract the password
    stored_password = a[0]

    # Check if the entered password matches the stored password
    if password_info == stored_password:
        Label(screen1, text="LOGIN success", fg="green", font=("calibri", 11)).pack()

        # Fetch email from the database
        c.execute('''SELECT mail FROM user WHERE name = ?''', (username_info,))
        b = c.fetchone()  # Fetch the first email row
        if b:
            email = b[0]
            onClickLogin(username_info, email)
    else:
        messagebox.showinfo('ERROR', 'Credentials Do Not Match')
        username_entry.delete(0, END)
        password_entry.delete(0, END)

def login_screen(screen):
	
    global screen1
    screen1=Toplevel(screen)
    screen1.title("LOGIN PAGE")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username=StringVar()
    password=StringVar()

    Label(screen1,text="Please enter details below").pack()
    Label(screen1,text="").pack()
    
    Label(screen1,text="Username").pack()
    username_entry=Entry(screen1,textvariable=username)
    username_entry.pack()
    #Entry(screen1,textvariable=username).pack()
    
    Label(screen1,text="Password").pack()
    #password_entry=Entry(screen1,textvariable=password)
    password_entry=Entry(screen1,textvariable=password,show='*')
    password_entry.pack()
    Label(screen1,text="").pack()
    
    Button(screen1,text="LOGIN",width=10,height=1,command=lambda:login_user(screen1)).pack()