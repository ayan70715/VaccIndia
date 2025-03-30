import tkinter as tk
from PIL import Image,ImageTk
import json

# Load hospital data from JSON file
def load_hospital_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def show_hospital_details(event, hospital_name, hospital_data, blank_frame, hospital_frame, details_frame):
    # Clear the current frame and show the details frame
    for widget in details_frame.winfo_children():
        widget.destroy()  # Clear existing widgets

    # Create a back button for returning to the hospital list
    back_button = tk.Label(details_frame, bg='orange', text="Back", cursor="hand2",width=10,height=2)
    back_button.bind('<Button-1>', lambda e: show_hospital_list(e, hospital_data, blank_frame, hospital_frame, details_frame))
    back_button.place(x=10, y=10)  # Position it at the top left corner
# Create a label to show the hospital details
    title_label = tk.Label(details_frame, bg='#FFD8E3', fg='purple', text=hospital_name, font=("Arial", 25,'bold'),width=35)
    title_label.pack(pady=(35,15))
    details_label = tk.Label(details_frame, bg='purple', fg='#FFF8F8', text=f"List of Available Doctors", font=("Arial", 15,'bold'))
    details_label.pack(pady=(5,15))

    # Get doctors and their available time slots
    for hospital in hospital_data['hospitals']:
        if hospital['hospital_name'] == hospital_name:
            doctors = hospital['doctors']
            break

    # Create labels for doctors and their time slots
    for doctor, info in doctors.items():
        # Load doctor image
        doctor_frame = tk.Frame(details_frame,width=35,height=2)
        doctor_frame.pack_propagate(False)
        doctor_frame.pack(pady=10)
        doctor_image = Image.open(info['image'])
        doctor_image = doctor_image.resize((82,82))
        doctor_image = ImageTk.PhotoImage(doctor_image)

        doctor_label = tk.Label(doctor_frame, image=doctor_image)
        doctor_label.image = doctor_image  # Keep a reference to avoid garbage collection
        doctor_label.grid(row=0, column=0, padx=10)

        # Create a frame for doctor info
        info_frame = tk.Frame(doctor_frame)
        info_frame.grid(row=0, column=1)

        doctor_name_label = tk.Label(info_frame, fg='cyan', text=f"Name: {doctor}", anchor=tk.W, font=("Arial", 14), width=35, height=1, justify="left")
        doctor_name_label.grid(row=0,column=0)

        doctor_experience_label = tk.Label(info_frame, fg='navy blue', text=f"Experience: {info['experience']}",anchor=tk.W, font=("Arial", 14), width=35, height=1)
        doctor_experience_label.grid(row=2,column=0)
        doctor_degree_label = tk.Label(info_frame, fg='navy blue', text=f"Degree: {info['degrees']}",anchor=tk.W, font=("Arial", 14), width=35, height=1)
        doctor_degree_label.grid(row=3,column=0)
        times_label = tk.Label(info_frame, fg='orange', text="Available Slots:", font=("Arial", 12,'bold'), wraplength=300, justify="left")
        times_label.grid(row=4,column=0)
        slot_frame = tk.Frame(info_frame)
        slot_frame.grid(row=5, column=0, padx=10)
        i=0
        for slot in info['schedule']:
            tk.Label(slot_frame, bg='orange',fg='white', text=slot, font=("Arial", 12,'bold')).grid(row=5,column=i,padx = 10)
            i+=1

    # Pack the details frame
    details_frame.pack(fill='both', expand=True)
    blank_frame.pack_forget()
    hospital_frame.pack_forget()  # Hide the hospital frame

def show_hospital_list(event, hospital_data, blank_frame, hospital_frame, details_frame):
    blank_frame.pack_forget()
    # Clear the details frame and show the hospital list
    for widget in hospital_frame.winfo_children():
        widget.destroy()  # Clear existing widgets

    # Create a back button for returning to a blank frame
    back_button = tk.Label(hospital_frame, bg='orange', text="Back", cursor="hand2",width=10,height=2)
    back_button.bind('<Button-1>', lambda e: show_prev(e, blank_frame, hospital_frame, details_frame))
    back_button.place(x=10, y=10)  # Position it at the top left corner

    title_label = tk.Label(hospital_frame, bg='purple', fg='#FFF8F8', text='List of Hospitals', font=("Arial", 25,'bold'),width=35)
    title_label.pack(pady=(35,15))

    space = tk.Label(hospital_frame, bg='#FFF8F8', height=1)
    space.pack()

    # Create labels for each hospital
    for hospital in hospital_data['hospitals']:
        create_hospital_label(hospital['hospital_name'], hospital['image'], hospital_data, blank_frame, hospital_frame, details_frame)

    # Pack the hospital frame
    hospital_frame.pack(fill='both', expand=True)
    details_frame.pack_forget()  # Hide the details frame

def create_hospital_label(hospital_name, hospital_image_path, hospital_data, blank_frame, hospital_frame, details_frame):
    hospital_image = Image.open(hospital_image_path)
    hospital_image = hospital_image.resize((73,73))
    hospital_image = ImageTk.PhotoImage(hospital_image)
    frame = tk.Frame(hospital_frame,bg='#FFD8E3')
    frame.pack(pady=5)
    profile = tk.Label(frame, bd=0,image=hospital_image)
    profile.grid(row=0,column=0)
    label = tk.Label(frame, bg='#FFD8E3', text=hospital_name, font=("Arial", 14), fg="blue", cursor="hand2", compound="top")
    label.image = hospital_image  # Keep a reference to avoid garbage collection
    label.config(width=35, height=3)
    label.grid(row=0,column=1)
    label.bind("<Button-1>", lambda e: show_hospital_details(e, hospital_name, hospital_data, blank_frame, hospital_frame, details_frame))

def show_prev(event, blank_frame, hospital_frame, details_frame):
    hospital_frame.pack_forget()
    details_frame.pack_forget()  # Hide details frame
    blank_frame.pack(fill='both', expand=True)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Hospital List")
    root.geometry("600x400")  # Adjusted window size for better visibility

    # Load hospital data from JSON file
    hospital_data = load_hospital_data('DataBase/hospitals.json')

    # Blank Frame
    blank_frame = tk.Frame(root, bg="black")
    blank_frame.pack(fill='both', expand=True)

    # Hospital Frame
    hospital_frame = tk.Frame(root, bg="blue")

    # Details Frame
    details_frame = tk.Frame(root, bg="blue")

    # Initially show the hospital list
    show_hospital_list('<Button-1>', hospital_data, blank_frame, hospital_frame, details_frame)

    # Run the application
    root.mainloop()
