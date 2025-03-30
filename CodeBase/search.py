import tkinter as tk
import json
from hospital_list import *

# Load hospital data from JSON file
def load_hospital_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to extract hospital names from JSON data
def extract_hospital_names(hospital_data):
    return [hospital['hospital_name'] for hospital in hospital_data['hospitals']]

# Function to update the list based on the search query
def update_list(search_entry, result_list, hospital_names, event=None):
    search_query = search_entry.get().lower()  # Get the text from the search bar
    filtered_hospital_names = [hospital for hospital in hospital_names if search_query == hospital.lower()[:len(search_query)]]
    
    # Clear the current list
    result_list.delete(0, tk.END)
    
    # Insert the filtered hospital_names into the list
    for hospital in filtered_hospital_names:
        result_list.insert(tk.END, hospital)
    
    # Show the Listbox if there are matching results
    if filtered_hospital_names:
        result_list.place(x=73, y=128)  # Adjust the position as necessary
    else:
        result_list.place_forget()

# Function to show the listbox when search entry is clicked
def show_listbox(result_list, hospital_names, event=None):
    result_list.place(x=73, y=128)  # Ensure the listbox is visible when the search bar is clicked
    for hospital in hospital_names:
        result_list.insert(tk.END,hospital)
# Function to hide the listbox when clicking outside
def hide_listbox(search_entry, result_list, event=None):
    # Hide the listbox if the click is outside the search box and the listbox
    if event.widget not in [search_entry, result_list]:
        result_list.place_forget()

def on_listbox_click(event, search_entry, hospital_names, result_list, blank_frame, hospital_frame, details_frame):
    # Get the currently selected item from the listbox
    hospital_names = load_hospital_data('DataBase\hospitals.json')
    selection = result_list.curselection()
    if selection:
        # Get the value of the selected item
        selected_value = result_list.get(selection[0])
        # Insert the selected value into the search entry
        search_entry.delete(0, tk.END)  # Clear the search entry
        search_entry.insert(0, selected_value)  # Insert the selected value
        show_hospital_details(None, selected_value, hospital_names, blank_frame, hospital_frame, details_frame)

# Main code
if __name__ == "__main__":
    # Load the hospital data from the JSON file
    file_path = 'DataBase\hospitals.json'
    hospital_data = load_hospital_data(file_path)
    
    # Extract hospital names from the JSON data
    hospital_names = extract_hospital_names(hospital_data)
    
    # Initialize the tkinter window
    root = tk.Tk()
    root.geometry("500x500")
    
    # Search entry
    search_entry = tk.Entry(root, font=("Arial", 14))
    search_entry.place(x=20, y=80)

    # Listbox to display search results
    result_list = tk.Listbox(root, font=("Arial", 14), width=40, height=5)
    
    # Bindings for search entry and listbox
    search_entry.bind("<KeyRelease>", lambda event: update_list(search_entry, result_list, hospital_names, event))
    search_entry.bind("<Button-1>", lambda event: show_listbox(result_list, event))
    result_list.bind("<ButtonRelease-1>", lambda event: on_listbox_click(event, search_entry, hospital_data, result_list, None, None, None))

    # Hide the listbox when clicking outside
    root.bind("<Button-1>", lambda event: hide_listbox(search_entry, result_list, event))
    
    # Start the tkinter loop
    root.mainloop()
