import tkinter as tk
import json

def load_user_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def load_home(root,Home):
    root.pack_forget()
    Home.pack()

def show_vaccine_list(event,user_name,Home,root):

    user_data = load_user_data('DataBase/user.json')
    Home.pack_forget()
    # Clear the frame before displaying new content
    for widget in root.winfo_children():
        widget.destroy()  # Clear existing widgets
    frame = tk.Frame(root, bg="lightblue")
    root.pack()
    back_button = tk.Button(root,text='back',bg='green',command=lambda:load_home(root,Home))
    back_button.place(x=0,y=0)
    # Find the user data
    user_info = next((user for user in user_data if user['email'] == user_name), None)

    if user_info:
        # Title
        title_label = tk.Label(frame, text=f"Vaccines taken by {user_info['name']}", font=("Arial", 16))
        title_label.pack(pady=10)

        # Check if the user has taken any vaccines
        if user_info['taken vaccine']:
            for vaccine in user_info['taken vaccine']:
                vaccine_info = f"Vaccine: {vaccine['vaccine']}, Hospital: {vaccine['hospital']}, Doctor: {vaccine['doctor']}, Time: {vaccine['time']}"
                vaccine_label = tk.Label(frame, text=vaccine_info, font=("Arial", 14))
                vaccine_label.pack(pady=5)
        else:
            no_vaccine_label = tk.Label(frame, text="No vaccines taken.", font=("Arial", 14))
            no_vaccine_label.pack(pady=10)
    else:
        error_label = tk.Label(frame, text="User not found.", font=("Arial", 14))
        error_label.pack(pady=10)

    # Pack the frame
    frame.pack(fill='both', expand=True)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("User Vaccine List")
    root.geometry("400x300")

    # Load user data from the JSON file
    user_data = load_user_data('DataBase/user.json')

    # Frame to display vaccine information
    vaccine_frame = tk.Frame(root, bg="lightblue")

    # Example user name to fetch vaccines for (you can change this or implement a login system)
    example_user_name = "John Doe"

    # Show vaccine list for the example user
    show_vaccine_list(example_user_name, user_data, vaccine_frame)

    # Run the application
    root.mainloop()
