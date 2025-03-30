from home_elements import *
from sign_elements import *
from search import *
from window import *





Home.pack(fill=tk.BOTH,expand=True)

profile.bind('<Button-1>',lambda e:show_login_frame(Home,search_entry))
login_button.config(command=lambda : login(Home))
log_button.config(command=lambda :show_login_frame(Home,search_entry))
signup_button.config(command=lambda :show_signup_frame(Home))
sign_button.config(command=lambda :signup(Home))
back_login.config(command=lambda:log_to_home(Home))
back_signup.config(command = lambda:sign_to_home(Home))

root.bind('<Button-1>', lambda e:hide_listbox(search_entry,result_list,e))
# Run the application
root.mainloop()