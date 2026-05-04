from button_func import *
from stats_ui import *
from tkinter import ttk
from tkinter import *
from styleing import *



# Load in pandas data frame
data_manager = DataManager()
data = data_manager.data

# Set up window and frame
root = Tk()
root.minsize(250,70)
root.title("JOB HUNT HELPER")
frm = ttk.Frame(root, padding=10)
frm.grid()

style = StyleWidgets(frm)


# Handle showing data in treeview
view_all_button = ttk.Button(frm, text="VIEW ALL", command=lambda: layout_hide_show('view_all',{
    'tree': tree,
    'view_all_button': view_all_button,
    'add_button': add_button,
    'edit_button': edit_button,
    'data_manager': data_manager,
    'search_button': search_button,
    'delete_button': delete_button,
    'back_to_menu_button': back_to_menu_button,
    'view_stats_button': view_stats_button,
}))
view_all_button.grid(column=0, row=2, padx=2, pady=2)

# Handle changing layout to add screen
add_button = ttk.Button(frm, text="ADD", command=lambda: layout_hide_show('add_button',{
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
    'back_to_menu_button': back_to_menu_button,
    'view_stats_button': view_stats_button,
    'frm': frm,
}))
add_button.grid(column=1, row=2, padx=2, pady=2)

# Handle adding new row to data frame
add_job_button = ttk.Button(frm, text='SAVE', command=lambda: adding_entry_and_cleanup({
    'job_name': job_name_entry,
    'job_type': job_type_entry,
    'transport': transport_entry,
    'job_address': job_address_entry,
    'date': date_entry,
    'job_status': job_status_entry,
}, data_manager))
add_job_button.grid(column=2, row=2, padx=2, pady=2)
add_job_button.grid_remove()

# Handle changing layout to search screen
search_button = ttk.Button(frm, text="SEARCH", command=lambda: layout_hide_show('search_button',{
    'view_all_button': view_all_button,
    'add_button': add_button,
    'search_bar': search_bar,
    'search_button': search_button,
    'find_button': find_button,
    'search_by_options': search_by_options,
    'opt': opt,
    'data_manager': data_manager,
    'tree': tree,
    'edit_button': edit_button,
    'frm': frm,
    'back_to_menu_button': back_to_menu_button,
    'delete_button': delete_button,
    'view_stats_button': view_stats_button,
}))
search_button.grid(column=2, row=2, padx=2, pady=2)

# Handle changing layout to edit screen
edit_button = ttk.Button(frm, text="EDIT", command=lambda: layout_hide_show('edit_button',{
    'tree': tree,
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
    'edit_button': edit_button,
    'search_button': search_button,
    'add_button': add_button,
    'update_button': update_button,
    'data_manager': data_manager,
    'delete_button': delete_button,
    'back_to_menu_button' : back_to_menu_button,
    'frm':frm,
    'view_stats_button': view_stats_button,
}))
edit_button.grid(column=1, row=2, padx=2, pady=2)
edit_button.grid_remove()

# Handle finding row/s in data frame
find_button = ttk.Button(frm, text="FIND")
find_button.grid(column=2, row=2, padx=2, pady=2)
find_button.grid_remove()

# Handle saving updated row to data frame
update_button = ttk.Button(frm, text="SAVE CHANGES")
update_button.grid(column=2, row=2, padx=2, pady=2)
update_button.grid_remove()

# Handle removing item from data frame
delete_button = ttk.Button(frm, text="DELETE", command=lambda: delete_job(tree, data_manager))
delete_button.grid(column=2, row=2, padx=2, pady=2)
delete_button.grid_remove()

# Handle changing layout back to home screen
back_to_menu_button = ttk.Button(frm, text="MENU", command=lambda: back_to_menu(frm, view_all_button, add_button, search_button, view_stats_button))
back_to_menu_button.grid(column=1, row=2, padx=2, pady=2)
back_to_menu_button.grid_remove()


# VIEW ALL JOBS UI -> treeview
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
tree.column('job_status', width=100)
tree.grid(column=0, row=3, columnspan=3, padx=2, pady=2)
tree._is_main_tree = True
tree.grid_remove()


# ADD/EDIT UI -> labels and entries
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


# SEARCH UI -> entry and option menu
search_bar = ttk.Entry(frm, width=25)
search_bar.grid(column=1, row=3, padx=2, pady=2, columnspan=2)
search_bar.grid_remove()

search_by = ["job name", "date", "status", "type", "bus/tram stop"]
opt = StringVar(value="SEARCH BY")
search_by_options = OptionMenu(frm, opt, *search_by)
search_by_options.grid(column=1, row=3, padx=2, pady=2)
search_by_options.grid_remove()

search_by_options.configure(font=('Verdana', 10))


# WORKING ON THIS:
# View statistics button
view_stats_button = ttk.Button(frm, text="VIEW STATS", command=lambda: layout_hide_show('view_stats_button',{
    'add_button': add_button,
    'search_button': search_button,
    'view_all_button': view_all_button,
    'view_stats_button': view_stats_button,
    'back_to_menu_button': back_to_menu_button,
    'average_per_day_button': average_per_day_button,
    'jobs_per_status_button': jobs_per_status_button,
    'jobs_per_type_button': jobs_per_type_button,
    'jobs_per_date_button': jobs_per_date_button,
    'apps_sent_last_week_button': apps_sent_last_week_button,
    'frm': frm,

}))
view_stats_button.grid(column=3, row=2, padx=2, pady=2)


# Widgets for view stats
average_per_day_button = ttk.Button(frm, text='AVERAGE APPS PER DAY', command=lambda: show_statistics('average_per_day_button',{
    'frm': frm,
    'chart_button': chart_button,
    'table_button': table_button,
}))
average_per_day_button.grid(column=1, row=2, padx=2, pady=2)
average_per_day_button.grid_remove()


jobs_per_status_button = ttk.Button(frm, text='JOBS PER STATUS', command=lambda: show_statistics('jobs_per_status_button',{
    'frm': frm,
    'chart_button': chart_button,
    'table_button': table_button,
}))
jobs_per_status_button.grid(column=1, row=3, padx=2, pady=2)
jobs_per_status_button.grid_remove()


jobs_per_type_button = ttk.Button(frm, text='JOBS PER TYPE', command=lambda: show_statistics('jobs_per_type_button',{
    'frm': frm,
    'chart_button': chart_button,
'table_button': table_button,
}))
jobs_per_type_button.grid(column=1, row=3, padx=2, pady=2)
jobs_per_type_button.grid_remove()


jobs_per_date_button = ttk.Button(frm, text='JOBS PER DATE', command=lambda: show_statistics('jobs_per_date_button',{
    'frm': frm,
    'chart_button': chart_button,
'table_button': table_button,
}))
jobs_per_date_button.grid(column=1, row=3, padx=2, pady=2)
jobs_per_date_button.grid_remove()


apps_sent_last_week_button = ttk.Button(frm, text='APPLICATIONS IN PAST WEEK', command=lambda: show_statistics('apps_sent_last_week_button',{
    'frm': frm,
    'chart_button': chart_button,
    'table_button': table_button,
}))
apps_sent_last_week_button.grid(column=1, row=3, padx=2, pady=2)
apps_sent_last_week_button.grid_remove()


# Chart button
chart_button = ttk.Button(frm, text='SHOW CHART')
chart_button.grid(column=1, row=4, padx=2, pady=2)
chart_button.grid_remove()


table_button = ttk.Button(frm, text='SHOW TABLE')
chart_button.grid(column=1, row=4, padx=2, pady=2)
chart_button.grid_remove()


style.my_theme()

root.mainloop()