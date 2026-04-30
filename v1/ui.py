from tkinter import *
from tkinter import ttk
from data_manager import *
from button_func import *


data_manager = DataManager()
data = data_manager.data


root = Tk()
root.minsize(250,70)
root.title("JOB HUNT HELPER")
frm = ttk.Frame(root, padding=10)
frm.grid()


view_all_button = ttk.Button(frm, text="VIEW ALL", command=lambda: layout_hide_show('view_all', {
    'data': data,
    'tree': tree,
    'view_all_button': view_all_button,
    'add_button': add_button,
    'edit_button': edit_button
}))
view_all_button.grid(column=0, row=2, padx=2, pady=2)

add_button = ttk.Button(frm, text="ADD", command=lambda: layout_hide_show('add_button', {
    'job_name_label': job_name_label,
    'job_name_entry': job_name_entry,
    'job_type_label': job_type_label,
    'job_type_entry': job_type_entry,
    'transport_label': transport_label,
    'transport_entry': transport_entry,
    'job_address_label': job_address_label,
    'job_address_entry': job_address_entry,
    'date_label': date_label,
    'date_entry': date_entry,
    'job_status_label': job_status_label,
    'job_status_entry' : job_status_entry,
    'view_all_button': view_all_button,
    'search_button': search_button,
    'add_button': add_button,
    'add_job_button': add_job_button,
}))
add_button.grid(column=1, row=2, padx=2, pady=2)

add_job_button = ttk.Button(frm, text='SAVE')
add_job_button.grid(column=2, row=2, padx=2, pady=2)
add_job_button.grid_remove()

search_button = ttk.Button(frm, text="SEARCH", command=lambda: layout_hide_show('search_button', {
    'view_all_button': view_all_button,
    'add_button': add_button,
    'search_bar': search_bar,
    'search_button': search_button,
    'find_button': find_button,
    'search_by_options': search_by_options,
}))
search_button.grid(column=2, row=2, padx=2, pady=2)

edit_button = ttk.Button(frm, text="EDIT")
edit_button.grid(column=1, row=2, padx=2, pady=2)
edit_button.grid_remove()

find_button = ttk.Button(frm, text="FIND")
find_button.grid(column=2, row=2, padx=2, pady=2)
find_button.grid_remove()


# DISPLAY ALL JOBS
tree = ttk.Treeview(frm, columns=['job_name', 'job_type', 'public_transport', 'job_address', 'date_applied',
                                          'job_status'], show='headings')
tree.heading('job_name', text='Job Name')
tree.column('job_name', width=100)
tree.heading('job_type', text='Job Type')
tree.column('job_type', width=100)
tree.heading('public_transport', text='Public Transport')
tree.column('public_transport', width=100)
tree.heading('job_address', text='Job Address')
tree.column('job_address', width=100)
tree.heading('date_applied', text='Date Applied')
tree.column('date_applied', width=100)
tree.heading('job_status', text='Job Status')
tree.column('job_status', width=150)
tree.grid(column=0, row=3, columnspan=3, padx=2, pady=2)
tree.grid_remove()


# ADD LAYOUT ELEMENTS
job_name_label = ttk.Label(frm, text="Job Name:", anchor='e')
job_name_label.grid(column=0, row=3, padx=2, pady=2)
job_name_label.grid_remove()
job_name_entry = ttk.Entry(frm, width=50)
job_name_entry.grid(column=1, row=3, padx=2, pady=2, columnspan=2)
job_name_entry.grid_remove()

job_type_label = ttk.Label(frm, text="Job Type:", anchor='e')
job_type_label.grid(column=0, row=4, padx=2, pady=2)
job_type_label.grid_remove()
job_type_entry = ttk.Entry(frm, width=50)
job_type_entry.grid(column=1, row=4, padx=2, pady=2, columnspan=2)
job_type_entry.grid_remove()

transport_label = ttk.Label(frm, text="Tram/Bus stop:", anchor='e')
transport_label.grid(column=0, row=5, padx=2, pady=2)
transport_label.grid_remove()
transport_entry = ttk.Entry(frm, width=50)
transport_entry.grid(column=1, row=5, padx=2, pady=2, columnspan=2)
transport_entry.grid_remove()

job_address_label = ttk.Label(frm, text="Job Address:", anchor='e')
job_address_label.grid(column=0, row=6, padx=2, pady=2)
job_address_label.grid_remove()
job_address_entry = ttk.Entry(frm, width=50)
job_address_entry.grid(column=1, row=6, padx=2, pady=2, columnspan=2)
job_address_entry.grid_remove()

date_label = ttk.Label(frm, text="Date (DD-MM-YYYY):", anchor='e')
date_label.grid(column=0, row=7, padx=2, pady=2)
date_label.grid_remove()
date_entry = ttk.Entry(frm, width=50)
date_entry.grid(column=1, row=7, padx=2, pady=2, columnspan=2)
date_entry.grid_remove()

job_status_label = ttk.Label(frm, text="Job Status:", anchor='e')
job_status_label.grid(column=0, row=8, padx=2, pady=2)
job_status_label.grid_remove()
job_status_entry = ttk.Entry(frm, width=50)
job_status_entry.grid(column=1, row=8, padx=2, pady=2, columnspan=2)
job_status_entry.grid_remove()


# SEARCH UI
search_bar = ttk.Entry(frm, width=25)
search_bar.grid(column=1, row=3, padx=2, pady=2, columnspan=2)
search_bar.grid_remove()

# Dropdown options
days = ["job name", "date", "status", "type", "bus/tram stop"]

# Selected option variable
opt = StringVar(value="job name")

# Dropdown menu
search_by_options = OptionMenu(frm, opt, *days)
search_by_options.grid(column=1, row=3, padx=2, pady=2)
search_by_options.grid_remove()


root.mainloop()