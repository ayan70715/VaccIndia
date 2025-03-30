import tkinter as tk
from tkinter import font
from PIL import Image,ImageTk
from window import *
from home_functions import *
from sign_elements import *
from search import *
from hospital_list import *
from appointment import *
from taken_list import *
from feedback import *





with open('DataBase/validate.txt','r') as file:
    data = file.readlines()
n = len(data)
email = ''
Home = tk.Frame(root,bg="#FFF8F8")
# Top Bar
Top_Frame = tk.Frame(Home,bg="red",height=1,width=1000)
Top_Frame.pack(fill=tk.X)

more = Image.open(r"C:\Users\AYAN JANA\Downloads\more_options.png")
more = more.resize((75,105))
more = ImageTk.PhotoImage(more)

more_options = tk.Label(Top_Frame,bd=0,image = more)
more_options.grid(row=0, column=0)

head_img = Image.open(r"IconBase\Heading.png")
head_img = head_img.resize((1400,105))
head_img = ImageTk.PhotoImage(head_img)
title_label = tk.Label(Top_Frame,bd=0,image=head_img)
title_label.grid(row=0, column=1)


prof = Image.open(r"C:\Users\AYAN JANA\Downloads\profile.png")
prof = prof.resize((75,105))
prof = ImageTk.PhotoImage(prof)

profile = tk.Label(Top_Frame,bd=0,image=prof)
profile.grid(row=0, column=2)


    # Search Bar Frame

search_frame = tk.Canvas(Home, bg='#FFF8F8',highlightthickness=0,width=730, height=60)
search_frame.place(x=397,y=130)

img_path = r"C:\Users\AYAN JANA\Documents\MyCodingDirectory\Python Folder\Vaccine\IconBase\Search.png"
img = Image.open(img_path)
tk_image = ImageTk.PhotoImage(img)

search_frame.create_image(0, 0, anchor=tk.NW, image=tk_image)

def on_entry_click(event):
    if search_entry.get() == placeholder:
        search_entry.config(fg='black',bg='#ECE6F0',state='normal')
        search_entry.delete(0, "end")
def on_focus_out(event):
    if search_entry.get() == '':
        search_entry.insert(0, placeholder)  
        search_entry.config(fg='grey',state='disabled',bg='#ECE6F0')

placeholder = 'Search Hospitals'
search_entry = tk.Entry(Home,bg='#ECE6F0',textvariable='search', bd=0, highlightthickness=0,width=60, font=("Arial", 14))
search_entry.insert(0, placeholder)
search_entry.config(fg='grey')
search_entry.bind("<Button-1>", on_entry_click)
Home.bind("<Button-1>", on_focus_out)   

entry_window = search_frame.create_window(17, 16, anchor=tk.NW, window=search_entry)


# search_frame = tk.Frame(Home, bg="#FFF8F8")
# search_frame.pack(pady=10)

    # Search Box

file_path = 'DataBase/hospitals.json'
hospital_data = load_hospital_data(file_path)
    
hospital_names = extract_hospital_names(hospital_data)

search_entry.bind('<KeyRelease>', lambda e:update_list(search_entry, result_list,hospital_names))
search_entry.bind('<FocusIn>', lambda e:show_listbox(result_list,hospital_names,e))
    #Search List
result_list = tk.Listbox(Home, font=("Arial", 12), width=34, height=10)
result_list.bind('<Button-1>',lambda e:on_listbox_click(e,search_entry, hospital_names,result_list,Home,hospital_frame,details_frame))

    # Search Button

# search_button = tk.Label(search_frame, text="Search Hospitals", bg="#d3d3d3", font=("Arial", 12))
# search_button.grid(row=0, column=1, padx=10)
# search_button.bind('<Button-1>',lambda e:show_hospital_details(e,search_entry.get(),hospital_data,Home,hospital_frame,details_frame)
# )

    # Tagline
tag_img = Image.open(r"C:\Users\AYAN JANA\Downloads\Button.png")
tag_img = ImageTk.PhotoImage(tag_img)
Tag = tk.Label(Home, bd=0, image=tag_img)
Tag.pack(pady=(100,0))

    # Buttons Frame for the four options
button_frame = tk.Frame(Home, bg="#FFF8F8")
button_frame.pack()

    # Helper function to create buttons
def create_button(path):
    img = Image.open(path)
    img = ImageTk.PhotoImage(img)
    button = tk.Label(button_frame, image=img)
    button.image = img
    return button

    # Buttons
def load_appointment(e):
    with open('DataBase/validate.txt','r') as file:
        data = file.readlines()
    if n==len(data):
        show_login_frame(Home,search_entry)
    else:
        email = data[-1].strip()
        Appointment_page(e,form,Home,email)

appointment = create_button(r"IconBase\appointment.png")
appointment.grid(row=0, column=0, padx=20, pady=20)
appointment.bind('<Button-1>',load_appointment)
form = tk.Frame(root,pady=35,width=500,height=500,bg="#FFF8F8")
back_button = tk.Label(root, bg='orange',text="Back")
back_button.bind('<Button-1>',lambda e:home_loader(e,Home,root))


hospitals = create_button(r"IconBase\hospitals.png")
hospitals.grid(row=0, column=1, padx=20, pady=20)
hospitals.bind('<Button-1>',lambda e:show_hospital_list(e,hospital_data,Home,hospital_frame,details_frame))

hospital_frame = tk.Frame(root, bg="#FFF8F8")
details_frame = tk.Frame(root, bg="#FFF8F8")


feedback_form = tk.Frame(root,width=100,bg="#FFF8F8")
feedback = create_button(r"IconBase\vaccines.png")
feedback.grid(row=1, column=0, padx=20, pady=20)
feedback.bind('<Button-1>',lambda e:show_feedback_form(e,feedback_form,Home))

def load_prevvac(e):
    with open('DataBase/validate.txt','r') as file:
        data = file.readlines()
    if n==len(data):
        show_login_frame(Home,search_entry)
    else:
        email = data[-1].strip()
        show_vaccine_list(e,email,Home,taken_vac,vac_details)
taken_vac = tk.Frame(root,bg="#FFD8E3",width=200,height=100)
vac_details = tk.Frame(root,bg="#FFF8F8",width=200,height=100)
previous_vaccines = create_button(r"IconBase\previous_vaccines.png")
previous_vaccines.grid(row=1, column=1, padx=20, pady=20)
previous_vaccines.bind('<Button-1>',lambda e:load_prevvac(e))