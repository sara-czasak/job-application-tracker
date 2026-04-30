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



view_all_button = ttk.Button(frm, text="VIEW ALL", command=lambda: layout_hide_show('view_all', {'data': data, 'tree': tree, 'view_all_button': view_all_button, 'add_button': add_button, 'edit_button': edit_button}))
view_all_button.grid(column=0, row=2, padx=2, pady=2)

add_button = ttk.Button(frm, text="ADD")
add_button.grid(column=1, row=2, padx=2, pady=2)

search_button = ttk.Button(frm, text="SEARCH")
search_button.grid(column=2, row=2, padx=2, pady=2)

edit_button = ttk.Button(frm, text="EDIT")
edit_button.grid(column=1, row=2, padx=2, pady=2)
edit_button.grid_remove()

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


root.mainloop()

