import tkinter as tk
from tkinter import font
from tkinter import messagebox
from PIL import Image,ImageTk
from window import *
import json
import os
import re



    
def login_or_signup(email, password,Home):
    file_path = 'DataBase/user.json'
    with open(file_path, 'r') as file:
        existing_data = json.load(file)

        for entry in existing_data:
            if entry["email"] == email:
                if entry["password"] == password:
                    messagebox.showinfo('Message',"Login successful!")
                    with open('DataBase/validate.txt','a') as file:
                        file.write(f'\n{email}')
                    login_frame.pack_forget()
                    Home.pack()
                    return
                else:
                    messagebox.showinfo('Warning',"Incorrect password. Please try again.")
                    return
        else:
            messagebox.showinfo('Warning',"New here?Please Sign up!")


def signup(Home):
    name = signup_name.get()
    age = signup_age.get()
    phone = signup_phone.get()
    email = signup_email.get()
    password = signup_password.get()

    # Check for empty fields
    if not name or not age or not phone or not email or not password:
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return

    # Validate age
    if not age.isdigit():
        messagebox.showwarning("Input Error", "Age must be a number.")
        return

    # Validate phone number
    if not phone.isdigit() or len(phone) != 10:
        messagebox.showwarning("Input Error", "Phone number must be a 10-digit number.")
        return

    # Validate email format
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(email_pattern, email):
        messagebox.showwarning("Input Error", "Please enter a valid email address.")
        return

    # Load existing user data to check for duplicate emails
    file_path = 'DataBase/user.json'
    
    if not os.path.exists(file_path):
        # If the file doesn't exist, create an empty list for user data
        existing_data = []
    else:
        with open(file_path, 'r') as file:
            existing_data = json.load(file)

    # Check for duplicate email
    for user in existing_data:
        if user['email'] == email:
            messagebox.showwarning("Signup Error", "This email is already registered. Please use a different email.")
            return  # Exit the function without saving new data

    # Create new user data
    new_user_data = {
        "name": name,
        "age": int(age),  # Assuming age is an integer
        "phone": phone,
        "email": email,
        "password": password,
        "taken vaccine": []  # Initialize with an empty list
    }

    # Append new user data to existing data
    existing_data.append(new_user_data)

    # Save updated user data to the JSON file
    with open(file_path, 'w') as file:
        json.dump(existing_data, file, indent=4)
    
    messagebox.showinfo('message', "Sign up successful! You can now log in.")

def show_login_frame(Home,search_entry):
    search_entry.delete(0,tk.END)
    Home.pack_forget()
    signup_frame.pack_forget()
    login_frame.pack_propagate(False)
    login_frame.pack(pady=20)

def show_signup_frame(Home):
    login_frame.pack_forget()
    signup_frame.pack_propagate(False)
    signup_frame.pack(pady=20)

def login(Home):
    email = login_email.get()
    password = login_password.get()
    login_or_signup(email,password,Home)

def log_to_home(Home):
    login_frame.pack_forget()
    Home.pack()

def sign_to_home(Home):
    signup_frame.pack_forget()
    Home.pack()

login_frame = tk.Frame(root, height=500, width=400, bg='#FFD8E3')
signup_frame = tk.Frame(root,height=80,width=200,bg='#FFD8E3')

# Login Frame
back_login = tk.Button(login_frame,text='Back',font=("Arial", 12, 'bold'),bg='orange',fg='yellow',width=8)
back_login.place(x=10,y=10)
tk.Label(login_frame, text="Login", font=("Arial", 24), bg='#FFD8E3', fg='purple').grid(row=0, column=1, pady=(20, 35))

tk.Label(login_frame, text="Email :", bg='#FFD8E3', fg='navy blue', font=("Arial", 14)).grid(row=1, column=0, padx=40, pady=10)
login_email = tk.Entry(login_frame, font=("Arial", 17),width=17)
login_email.grid(row=1, column=1, padx=10, pady=10)
tk.Label(login_frame,bg='#FFD8E3',width=10).grid(row=1,column=2)

tk.Label(login_frame, text="Password :", bg='#FFD8E3', fg='navy blue', font=("Arial", 14)).grid(row=2, column=0, padx=40, pady=10)
login_password = tk.Entry(login_frame, show='*', font=("Arial", 17),width=17)
login_password.grid(row=2, column=1, padx=10, pady=10)
tk.Label(login_frame,bg='#FFD8E3',width=10).grid(row=2,column=2)

login_button = tk.Button(login_frame, text="Login", font=("Arial", 14), bg='purple', fg='white', width=15)
login_button.grid(row=3, column=1, pady=(46,10))

signup_button = tk.Button(login_frame, text="Go to Sign Up", font=("Arial", 14), bg='purple', fg='white', width=15)
signup_button.grid(row=4, column=1,pady=(5,37))

    # Signup Frame
back_signup = tk.Button(signup_frame,text='Back',font=("Arial", 12, 'bold'),bg='orange',fg='yellow',width=8)
back_signup.place(x=10,y=10)

tk.Label(signup_frame, text="Sign Up", font=("Arial", 25),bg='#FFD8E3', fg='purple').grid(row=0, column=1,pady=35)
tk.Label(signup_frame, text="Name(child)", font=("Arial", 14), bg='#FFD8E3',fg='purple',anchor=tk.W).grid(row=1, column=0,padx=(55,0))
signup_name = tk.Entry(signup_frame, font=("Arial", 14),width=25)
signup_name.grid(row=1, column=1,pady=10)
tk.Label(signup_frame,bg='#FFD8E3',width=15).grid(row=1,column=2)

tk.Label(signup_frame, text="Age(child)", font=("Arial", 14), bg='#FFD8E3',fg='purple',anchor=tk.W).grid(row=2, column=0,padx=(55,0))
signup_age = tk.Entry(signup_frame, font=("Arial", 14),width=25)
signup_age.grid(row=2, column=1,pady=10)
tk.Label(signup_frame,bg='#FFD8E3',width=15).grid(row=2,column=2)

tk.Label(signup_frame, text="Phone No.", font=("Arial", 14), bg='#FFD8E3',fg='purple',anchor=tk.W).grid(row=3, column=0,padx=(55,0))
signup_phone = tk.Entry(signup_frame, font=("Arial", 14),width=25)
signup_phone.grid(row=3, column=1,pady=10)
tk.Label(signup_frame,bg='#FFD8E3',width=15).grid(row=3,column=2)

tk.Label(signup_frame, text="Email", font=("Arial", 14), bg='#FFD8E3',fg='purple',anchor=tk.W).grid(row=4, column=0,padx=(55,0))
signup_email = tk.Entry(signup_frame, font=("Arial", 14),width=25)
signup_email.grid(row=4, column=1,pady=10)
tk.Label(signup_frame,bg='#FFD8E3',width=15).grid(row=4,column=2)

tk.Label(signup_frame, text="Password", font=("Arial", 14), bg='#FFD8E3',fg='purple',anchor=tk.W).grid(row=5, column=0,padx=(55,0))
signup_password = tk.Entry(signup_frame, font=("Arial", 14),width=25)
signup_password.grid(row=5, column=1,pady=10)
tk.Label(signup_frame,bg='#FFD8E3',width=15).grid(row=5,column=2)

sign_button = tk.Button(signup_frame, text="Sign Up",font=("Arial", 14), fg='navy blue', bg='cyan')
sign_button.grid(row=6, column=1, pady=(20,10))

log_button = tk.Button(signup_frame, text="Go to Login", font=("Arial", 14), fg='navy blue', bg='cyan')
log_button.grid(row=7, column=1,pady=(5,30))
