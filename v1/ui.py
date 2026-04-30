from tkinter import *
from tkinter import ttk
from data_manager import *
from button_func import *


data_manager = DataManager()
data = data_manager.data

# Remove later, leave for testing
print(show_all_jobs(data))

root = Tk()
root.minsize(300,100)
frm = ttk.Frame(root, padding=10)
frm.grid()
title = ttk.Label(frm, text="JOB HUNT HELPER")
title.grid(column=1, row=0)

menu_label = ttk.Label(frm, text="CHOOSE YOUR OPTION")
menu_label.grid(column=1, row=1, padx=10, pady=10)

view_all_button = ttk.Button(frm, text="VIEW ALL")
view_all_button.grid(column=0, row=2, padx=2, pady=2)

add_button = ttk.Button(frm, text="ADD")
add_button.grid(column=1, row=2, padx=2, pady=2)

search_button = ttk.Button(frm, text="SEARCH")
search_button.grid(column=2, row=2, padx=2, pady=2)





root.mainloop()

