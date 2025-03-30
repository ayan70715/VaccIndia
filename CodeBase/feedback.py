import tkinter as tk
from tkinter import messagebox

def submit_feedback(feedback_entry):
    feedback = feedback_entry.get("1.0", tk.END).strip()
    with open('DataBase/feedback.txt','a') as file:
        file.write(f'\n{feedback}')
    if not feedback:
        messagebox.showwarning("Warning", "Please enter your feedback!")
        feedback_entry.delete("1.0", tk.END)
        return
    # Clear the feedback form after submission
    feedback_entry.delete("1.0", tk.END)
    messagebox.showinfo("Success", "Feedback submitted successfully!")

def go_back(Home,feedback_frame):
    feedback_frame.pack_forget()
    Home.pack(fill='both', expand=True)

def show_feedback_form(event,root,Home):
    for widget in root.winfo_children():
        widget.destroy()
    Home.pack_forget()
    root.pack()
    feedback_frame = tk.Frame(root, width=100, bg="#FFD8E3")

    feedback_label = tk.Label(feedback_frame, width=40,text="Your Feedback:", font=("Arial", 20,'bold'),bg='#FFD8E3',fg='purple')
    feedback_label.pack(pady=(35,15))

    feedback_entry = tk.Text(feedback_frame, width=70, height=15)
    feedback_entry.pack(pady=10)

    # Submit Button
    submit_button = tk.Button(feedback_frame, text="Submit", width=10,font=("Arial", 14,'bold'),bg='purple',fg="#FFD8E3",command=lambda:submit_feedback(feedback_entry))
    submit_button.pack(pady=(73,15))

    # Back Button
    back_button = tk.Button(feedback_frame, text="Back", width=10, font=("Arial", 14,'bold'),bg='orange',fg='yellow',command=lambda:go_back(Home,root))
    back_button.pack(pady=5)
    Home.pack_forget()
    
    feedback_frame.pack(pady=73)

    root.mainloop()