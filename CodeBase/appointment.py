import tkinter as tk
from tkinter import messagebox
import json
import os

# Global variables to track if a time slot has been selected and the selected button
time_slot_selected = False
selected_slot_button = None  # To store the reference of the clicked button

def submit_form(appointment_frame, time_slot_frame, hospital_entry, doctor_entry, vaccine_entry, submit_button,email):
    hospital_name = hospital_entry.get()
    doctor_name = doctor_entry.get()
    vaccine_name = vaccine_entry.get()

    if hospital_name and doctor_name and vaccine_name:
        time_slots = fetch_time_slot(hospital_name, doctor_name)
        
        if time_slots != 'Warning':
            time_slot_frame.pack_forget()  # Clear the previous time slot buttons if any
            time_slot_frame.pack(pady=10)  # Pack a new frame to hold time slot buttons
            
            for slot in time_slots:
                time_slot_button = tk.Button(time_slot_frame, text=slot, bg='cyan',fg='blue',font=('Arial',12,'bold'))
                time_slot_button.pack(side=tk.LEFT, padx=5)
                time_slot_button.config(command=lambda b=time_slot_button, s=slot: select_time_slot(b, s, hospital_name, doctor_name, vaccine_name,email))

            # Disable the submit button after one click
            submit_button.config(state=tk.DISABLED)
        else:
            messagebox.showwarning("Error", "Invalid hospital or doctor name.")
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

def select_time_slot(button, slot, hospital_name, doctor_name, vaccine_name,email):
    global time_slot_selected, selected_slot_button

    if time_slot_selected:
        response = messagebox.askyesno("New Appointment", "A time slot has already been selected. Do you want to start a new appointment?")
        if response:
            messagebox.showinfo("New Appointment", "Go back and start a new appointment again.")

    else:
        time_slot_selected = True
        selected_slot_button = button  # Store the clicked button
        disable_other_buttons(button)  # Disable other time slot buttons
        messagebox.showinfo("Time Slot Selected", f"You have selected the time slot: {slot}")

        # Store the appointment data in the JSON file
        store_appointment_data(hospital_name, doctor_name, vaccine_name, slot,email)

def disable_other_buttons(clicked_button):
    for widget in clicked_button.master.winfo_children():
        if isinstance(widget, tk.Button) and widget != clicked_button:
            widget.config(state=tk.DISABLED)

def reset_appointment():
    global time_slot_selected, selected_slot_button
    time_slot_selected = False
    selected_slot_button = None
    messagebox.showinfo("New Appointment", "Go back and start a new appointment again.")

def fetch_time_slot(hospital_name, doctor_name):
    with open('DataBase/hospitals.json', 'r') as file:
        data = json.load(file)
    
    for hospital in data['hospitals']:
        if hospital['hospital_name'] == hospital_name:
            doctors = hospital['doctors']
            if doctor_name in doctors:
                return doctors[doctor_name]['schedule']
    return 'Warning'

def store_appointment_data(hospital_name, doctor_name, vaccine_name, time_slot,email):
    file_path = 'DataBase/user.json'
    # Load existing data from the file if it exists
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            existing_data = json.load(file)

        # Find the user's record and append the new appointment
        user_found = False
        for entry in existing_data:
            if entry["email"] == email:  # Assuming email is the identifier
                user_found = True
                entry["taken vaccine"].append({
                    "vaccine": vaccine_name,
                    "hospital": hospital_name,
                    "doctor": doctor_name,
                    "time": time_slot
                })
                break
        
        if user_found:
            # Write the updated data back to the JSON file
            with open(file_path, 'w') as file:
                json.dump(existing_data, file, indent=4)
        else:
            messagebox.showerror("Error", "User data not found. Cannot store appointment.")
    else:
        messagebox.showerror("Error", "Appointment data file not found.")

def home_loader(Home, root):
    root.pack_forget()
    Home.pack()

def Appointment_page(event, root, Home,email):
    global time_slot_selected, selected_slot_button
    time_slot_selected = False  # Reset on new appointment page load
    selected_slot_button = None  # Reset selected button
    
    Home.pack_forget()
    for widget in root.winfo_children():
        widget.destroy()
    root.pack()
    # Create a new frame to hold the content of the Appointment page
    appointment_frame = tk.Frame(root,bg='#FFD8E3',width=500,height=600)
    appointment_frame.pack_propagate(False)
    appointment_frame.pack()

    # Back button to return to the home page
    back_button = tk.Button(appointment_frame, width=6, height=1, font=('Arial',12,'bold'),bg='orange',fg='yellow', text="Back",command= lambda: home_loader(Home, root))
    back_button.place(x=15, y=15)  # Position it at the top left corner

    # Hospital Name Entry
    hospital_label = tk.Label(appointment_frame,width=20,height=1,bg='#FFD8E3',font=('Arial',12,'bold'),fg='blue', text="Hospital Name:")
    hospital_label.pack(pady=(64,5))
    hospital_entry = tk.Entry(appointment_frame, font=('Arial',14), width=40)
    hospital_entry.pack(pady=15)

    # Doctor Name Entry
    doctor_label = tk.Label(appointment_frame,width=20,height=1,bg='#FFD8E3',font=('Arial',12,'bold'),fg='blue', text="Doctor Name:")
    doctor_label.pack(pady=5)
    doctor_entry = tk.Entry(appointment_frame, font=('Arial',14), width=40)
    doctor_entry.pack(pady=15)

    # Vaccine Name Entry
    vaccine_label = tk.Label(appointment_frame,width=20,height=1,bg='#FFD8E3',font=('Arial',12,'bold'),fg='blue', text="Vaccine Name:")
    vaccine_label.pack(pady=5)
    vaccine_entry = tk.Entry(appointment_frame, font=('Arial',14), width=40)
    vaccine_entry.pack(pady=(15,25))

    # Frame to hold the dynamic time slot buttons
    time_slot_frame = tk.Frame(appointment_frame)
    
    # Submit Button to trigger time slot generation
    submit_button = tk.Button(appointment_frame, width=15,height=2,font=('Arial',12,'bold'),text="Submit", bg='purple',fg='#FFF8F8',command=lambda: submit_form(appointment_frame, time_slot_frame, hospital_entry, doctor_entry, vaccine_entry, submit_button,email))
    submit_button.pack(pady=20)



# # Main window initialization
# if __name__ == '__main__':
#     root = tk.Tk()
#     root.title("Appointment Form")
#     root.geometry("400x400")

#     # Home Frame
#     Home = tk.Frame(root, bg="lightblue")
#     Home.pack(fill='both', expand=True)

#     # Home page contents
#     welcome_label = tk.Label(Home, text="Welcome to the Appointment System", font=("Arial", 16))
#     welcome_label.pack(pady=20)

#     # Appointment page loader button on the Home page
#     appointment_button = tk.Label(Home, text="Book an Appointment", bg="green", fg="white", font=("Arial", 12), cursor="hand2")
#     appointment_button.pack(pady=20)
#     appointment_button.bind('<Button-1>', lambda e: Appointment_page(e, root, Home))

#     # Start the main loop
#     root.mainloop()