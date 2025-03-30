import tkinter as tk
import json

def load_user_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def load_home(root, Home):
    root.pack_forget()
    Home.pack()

def show_vaccine_details(vaccine, Home, root1,root2):
    # Clear the frame before displaying new content
    root1.pack_forget()
    for widget in root2.winfo_children():
        widget.destroy()  # Clear existing widgets
    root2.pack()
    # Create a new frame for vaccine details
    frame = tk.Frame(root2, bg="#FFD8E3",width=60,height=20)
    frame.pack(fill='both', expand=True)


    # Back button to return to the vaccine list
    back_button = tk.Button(frame, text='Back', bg='orange',fg='yellow',width=10,height=1,font=("Arial", 12,'bold'), command=lambda: load_home(root2, root1))
    back_button.pack(pady=5, anchor='w')


    # Display vaccine details
    vaccine_label = tk.Label(frame, bg='purple', fg='#FFF8F8',text=f"Vaccine: {vaccine['vaccine']}", font=("Arial", 20,'bold'))
    vaccine_label.pack(pady=10)

    space = tk.Label(frame,bg="#FFD8E3", width=73,height=3)
    space.pack()

    hospital_label = tk.Label(frame, bg='#FFD8E3', fg='cyan', text=f"Hospital: {vaccine['hospital']}", font=("Arial", 14))
    hospital_label.pack(pady=5)
    doctor_label = tk.Label(frame, bg='#FFD8E3', fg='cyan', text=f"Doctor: {vaccine['doctor']}", font=("Arial", 14))
    doctor_label.pack(pady=5)

    time_label = tk.Label(frame, bg='#FFD8E3', fg='navy blue', text=f"Time: {vaccine['time']}", font=("Arial", 14))
    time_label.pack(pady=5)

    space1 = tk.Label(frame,bg="#FFD8E3", width=73,height=3)
    space1.pack()

def show_vaccine_list(event, user_name, Home, root1,root2):
    user_data = load_user_data('DataBase/user.json')
    Home.pack_forget()

    # Clear the frame before displaying new content
    for widget in root1.winfo_children():
        widget.destroy()  # Clear existing widgets
    root1.pack(pady=35)

    # Back button to go back to the previous screen
    back_button = tk.Button(root1, text='Back', width=10,bg='orange',fg='yellow',font=('Arial',12,'bold'), command=lambda: load_home(root1, Home))
    back_button.pack(pady=5, anchor='w')

    #Top Frame
    frame = tk.Frame(root1, bg='#FFD8E3',width=650,height=60,pady=30)
    frame.pack_propagate(False)
    frame.pack(pady=(25,46))


    # Find the user data
    user_info = next((user for user in user_data if user['email'] == user_name), None)

    if user_info:
        # Title
        title_label = tk.Label(frame, text=f"Vaccines taken by {user_info['name']}",width=25,height=2,bg='purple',fg='#FFF8F8',font=("Arial", 20, 'bold'))
        title_label.place(x=105,y=-32)

        # Check if the user has taken any vaccines
        if user_info['taken vaccine']:
            for vaccine in user_info['taken vaccine']:
                # Create a clickable label for each vaccine
                vaccine_label = tk.Label(root1, text=vaccine['vaccine'], width=25,height=2,font=("Arial", 17),bg='#FFF8F8', fg="blue", cursor="hand2")
                vaccine_label.pack(pady=5)

                # Bind the click event to show details for the specific vaccine
                vaccine_label.bind("<Button-1>", lambda event, v=vaccine: show_vaccine_details(v, Home, root1,root2))
        else:
            no_vaccine_label = tk.Label(root1, text="No vaccines taken.",bg='#FFF8F8', fg="blue", width=60,font=("Arial", 14))
            no_vaccine_label.pack(pady=10)
