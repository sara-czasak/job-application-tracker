import tkinter as tk
from popups import *


# Change layout to home screen
def back_to_menu(frm, view_all_button, add_button, search_button, view_stats_button):
    children = frm.winfo_children()

    for i in children:
        i.grid_remove()
    view_all_button.grid(column=0, row=2, padx=2, pady=2)
    add_button.grid(column=1, row=2, padx=2, pady=2)
    search_button.grid(column=2, row=2, padx=2, pady=2)
    view_stats_button.grid(column=3, row=2, padx=2, pady=2)


# Handle clearing ui widgets
def clear_layout(items):
    for i in items:
        i.grid_remove()


# Reset entry values
def clear_entries(entries):
    for entry in entries:
        entry.delete(0, tk.END)


def adding_entry_and_cleanup(data_dict, data_manager):
    if data_manager.save_new_job(data_dict):
        to_clean = [i for i in data_dict.values()]
        clear_entries(to_clean)


# Handle entry deletion
def delete_job(tree, data_manager):
    data = data_manager.load_data()
    item_to_delete = tree.focus()
    index = int(tree.index(item_to_delete))
    # Check if an item was selected
    if item_to_delete:
        # Check that user wants to delete entry
        if are_you_sure():
            # Delate entry
            new_data = data_manager.delete_row(index)
            if new_data.empty:
                return 'No job data added yet'
            else:
                rows = new_data.iterrows()
                tree.delete(*tree.get_children())
                for row in rows:
                    tree.insert('', tk.END, values=list(row[1].values))
                tree.grid(column=0, row=3, columnspan=3, padx=2, pady=2)
    else:
        # Inform user about lack of selection
        feedback('Please select a job to delete.')
    return None


# Handle updating data frame
def save_changes_func(context, index):
    update_button = context['update_button']
    job_name = context['job_name']
    job_type = context['job_type']
    transport = context['transport']
    job_address = context['job_address']
    date = context['date']
    job_status = context['job_status']
    data_manager = context['data_manager']
    job_name_label = context['job_name_label']
    job_type_label = context['job_type_label']
    transport_label = context['transport_label']
    job_address_label = context['job_address_label']
    date_label = context['date_label']
    job_status_label = context['job_status_label']
    edit_button = context['edit_button']
    search_button = context['search_button']
    add_button = context['add_button']
    view_all_button = context['view_all_button']
    delete_button = context['delete_button']
    back_to_menu_button = context['back_to_menu_button']
    frm = context['frm']

    data_dict = {
        'job_name': job_name,
        'job_type': job_type,
        'transport': transport,
        'job_address': job_address,
        'date': date,
        'job_status': job_status,
    }

    # Update data frame
    updated = data_manager.update_job(data_dict, index)
    if updated:
        clear_entries([job_name, job_type, transport, job_address, date, job_status])
        search_button.grid(column=2, row=2, padx=2, pady=2)
        view_all_button.grid(column=0, row=2, padx=2, pady=2)
        add_button.grid(column=1, row=2, padx=2, pady=2)
        # Handle removing unneeded widgets and resetting ui to home screen
        clear_layout([add_button, view_all_button])

# Handle getting row/s from data frame
def convert_and_search(context):
    opt = context['opt']
    data_manager = context['data_manager']
    search_bar = context['search_bar']
    tree = context['tree']
    search_button = context['search_button']
    search_by = context['search_by_options']
    find_button = context['find_button']
    add_button = context['add_button']
    back_to_menu_button = context['menu_button']
    edit_button = context['edit_button']
    delete_button = context['delete_button']

    col = ''

    # Convert selected OptionMenu option to accepted value
    if opt.get() == "job name":
        col = 'job_name'
    elif opt.get() == "date":
        col = 'date_applied'
    elif opt.get() == 'type':
        col = 'job_type'
    elif opt.get() == 'bus/tram stop':
        col = 'public_transport'
    elif opt.get() == 'status':
        col = 'job_status'
    else:
        # Inform user that an option needs to be selected
        feedback('Please select an option from the dropdown menu.')

    if col != '':
        # Search for row/s
        value = search_bar.get()
        data = data_manager.find_rows(col, value)

        if data is not None:
            if data.empty:
                # Inform user no entries where found
                feedback('No entries found.')
                return 'No data found'
            else:
                # Remove unneeded widgets
                clear_layout([search_bar, search_by, find_button, search_button, add_button])
                rows = data.iterrows()
                tree.delete(*tree.get_children())

                # Handle displaying row/s found
                for row in rows:
                    tree.insert('', tk.END, values=list(row[1].values))
                tree.grid(column=0, row=3, columnspan=3, padx=2, pady=2)
                back_to_menu_button.grid(column=0, row=2, padx=2, pady=2)
                edit_button.grid(column=1, row=2, padx=2, pady=2)
                delete_button.grid(column=2, row=2, padx=2, pady=2)
                opt.set("SEARCH BY")
                clear_entries([search_bar])
                return None
        else:
            return None
    else:
        return None



# Button functions -> view_all, add, search, edit
def layout_hide_show(button_id,context):

    # VIEW ALL BUTTON
    if button_id == 'view_all':
        add_button = context['add_button']
        view_all_button = context['view_all_button']
        tree = context['tree']
        edit_button = context['edit_button']
        data_manager = context['data_manager']
        search_button = context['search_button']
        delete_button = context['delete_button']
        back_to_menu_button = context['back_to_menu_button']
        view_stats_button = context['view_stats_button']
        data = data_manager.load_data()
        if not tree.winfo_viewable():
            if data.empty:
                # Inform user that there is no data
                feedback('No data found. Please add a job then try again.')
                return 'No job data added yet'
            else:
                # Remove unneeded widgets
                clear_layout([add_button,search_button, view_all_button, view_stats_button])
                rows = data.iterrows()
                tree.delete(*tree.get_children())
                # Display treeview with all available data
                for row in rows:
                    tree.insert('', tk.END, values=list(row[1].values))
                tree.grid(column=0, row=3, columnspan=3, padx=2, pady=2)
                back_to_menu_button.grid(column=0, row=2, padx=2, pady=2)
                edit_button.grid(column=1, row=2, padx=2, pady=2)
                delete_button.grid(column=2, row=2, padx=2, pady=2)
                return None
        else:
            back_to_menu_button.grid(column=0, row=2, padx=2, pady=2)


            return None

    # ADD BUTTON
    elif button_id == 'add_button':
        job_name_label = context['job_name_label']
        job_name_entry = context['job_name_entry']
        job_type_label = context['job_type_label']
        job_type_entry = context['job_type_entry']
        transport_label = context['transport_label']
        transport_entry = context['transport_entry']
        job_address_label = context['job_address_label']
        job_address_entry = context['job_address_entry']
        date_label = context['date_label']
        date_entry = context['date_entry']
        job_status_label = context['job_status_label']
        job_status_entry = context['job_status_entry']
        add_button = context['add_button']
        view_all_button = context['view_all_button']
        search_button = context['search_button']
        add_job_button = context['add_job_button']
        back_to_menu_button = context['back_to_menu_button']
        view_stats_button = context['view_stats_button']
        frm = context['frm']

        # Check if the add ui has been loaded in
        if not job_name_label.winfo_viewable():
            # Clear unneeded widgets
            clear_layout([view_all_button, search_button, add_button, view_stats_button])
            # Set up data entry ui
            job_name_label.grid(column=0, row=3, padx=2, pady=2)
            job_name_entry.grid(column=1, row=3, padx=2, pady=2, columnspan=2)
            job_type_label.grid(column=0, row=4, padx=2, pady=2)
            job_type_entry.grid(column=1, row=4, padx=2, pady=2, columnspan=2)
            transport_label.grid(column=0, row=5, padx=2, pady=2)
            transport_entry.grid(column=1, row=5, padx=2, pady=2, columnspan=2)
            job_address_label.grid(column=0, row=6, padx=2, pady=2)
            job_address_entry.grid(column=1, row=6, padx=2, pady=2, columnspan=2)
            date_label.grid(column=0, row=7, padx=2, pady=2)
            date_entry.grid(column=1, row=7, padx=2, pady=2, columnspan=2)
            job_status_label.grid(column=0, row=8, padx=2, pady=2)
            job_status_entry.grid(column=1, row=8, padx=2, pady=2, columnspan=2)
            back_to_menu_button.grid(column=1, row=2, padx=2, pady=2)

            add_job_button.grid(column=2, row=2, padx=2, pady=2)
            return None
        else:
            # Clear unneeded widgets
            clear_layout([
                job_name_label,
                job_name_entry,
                job_type_label,
                job_type_entry,
                transport_label,
                transport_entry,
                job_address_label,
                job_address_entry,
                date_label,
                date_entry,
                job_status_label,
                job_status_entry,
            ])
            # Reset values in entries
            clear_entries([job_name_entry, job_type_entry, transport_entry, job_address_entry, date_entry,job_status_entry])
            search_button.grid(column=2, row=2, padx=2, pady=2)
            # view_all_button.grid(column=0, row=2, padx=2, pady=2)
            # add_button.config(text='ADD')
            # add_button.grid(column=1, row=2, padx=2, pady=2)
            back_to_menu(frm, view_all_button, add_button, search_button, view_stats_button)
            return None

    # SEARCH BUTTON
    elif button_id == 'search_button':
        add_button = context['add_button']
        view_all_button = context['view_all_button']
        search_bar = context['search_bar']
        search_button = context['search_button']
        find_button = context['find_button']
        search_by_options = context['search_by_options']
        data_manager = context['data_manager']
        opt = context['opt']
        tree = context['tree']
        frm = context['frm']
        back_to_menu_button = context['back_to_menu_button']
        delete_button = context['delete_button']
        edit_button = context['edit_button']
        view_stats_button = context['view_stats_button']

        # Check if search ui loaded
        if not search_bar.winfo_viewable():
            # Clear unneeded widgets
            clear_layout([view_all_button, add_button, view_stats_button])
            # Set up search ui
            search_bar.grid(column=0, row=3, padx=2, pady=2)
            search_by_options.grid(column=2, row=3, padx=2, pady=2)
            back_to_menu_button.grid(column=1, row=2, padx=2, pady=2)
            find_button.grid(column=2, row=2, padx=2, pady=2)
            opt.set("SEARCH BY")
            clear_entries([search_bar])

            # Search for query value
            find_button.config(command=lambda: convert_and_search({
                    'opt': opt,
                    'data_manager': data_manager,
                    'search_bar': search_bar,
                    'search_button': search_button,
                    'tree': tree,
                    'search_by_options': search_by_options,
                    'find_button': find_button,
                    'view_all_button': view_all_button,
                    'edit_button': edit_button,
                    'add_button': add_button,
                    'frm': frm,
                    'menu_button': back_to_menu_button,
                    'delete_button': delete_button,
                    }))
            return None
        else:
            # Clear unneeded widgets
            clear_layout([find_button, search_by_options, search_bar])
            search_button.config(text='SEARCH')
            back_to_menu(frm, view_all_button, add_button, search_button, view_stats_button)
            # search_button.grid(column=2, row=2, padx=2, pady=2)
            # add_button.grid(column=1, row=2, padx=2, pady=2)
            # view_all_button.grid(column=0, row=2, padx=2, pady=2)
            return None

    # EDIT BUTTON
    elif button_id == 'edit_button':
        job_name_label = context['job_name_label']
        job_name_entry = context['job_name_entry']
        job_type_label = context['job_type_label']
        job_type_entry = context['job_type_entry']
        transport_label = context['transport_label']
        transport_entry = context['transport_entry']
        job_address_label = context['job_address_label']
        job_address_entry = context['job_address_entry']
        date_label = context['date_label']
        date_entry = context['date_entry']
        job_status_label = context['job_status_label']
        job_status_entry = context['job_status_entry']
        tree = context['tree']
        view_all_button = context['view_all_button']
        edit_button = context['edit_button']
        search_button = context['search_button']
        add_button = context['add_button']
        update_button = context['update_button']
        data_manager = context['data_manager']
        delete_button = context['delete_button']
        back_to_menu_button = context['back_to_menu_button']
        frm = context['frm']
        view_stats_button = context['view_stats_button']
        data = data_manager.load_data()
        selected_item = tree.focus()
        # Get index of item to be updated
        index = int(tree.index(selected_item))

        # Check if edit ui loaded
        if not job_name_label.winfo_viewable():
            # Check if an item was selected from treeview
            if selected_item:
                # Format data
                job_to_edit = {
                    'job_name': tree.item(selected_item)['values'][0],
                    'job_type': tree.item(selected_item)['values'][1],
                    'public_transport': tree.item(selected_item)['values'][2],
                    'job_address': tree.item(selected_item)['values'][3],
                    'date_applied': tree.item(selected_item)['values'][4],
                    'job_status': tree.item(selected_item)['values'][5],
                }

                # Clear unneeded widgets
                clear_layout([tree, view_all_button, delete_button, edit_button])

                # Set up edit ui
                job_name_label.grid(column=0, row=3, padx=2, pady=2)
                job_name_entry.grid(column=1, row=3, padx=2, pady=2, columnspan=2)
                job_name_entry.insert(tk.END, job_to_edit['job_name'])

                job_type_label.grid(column=0, row=4, padx=2, pady=2)
                job_type_entry.grid(column=1, row=4, padx=2, pady=2, columnspan=2)
                job_type_entry.insert(tk.END, job_to_edit['job_type'])

                transport_label.grid(column=0, row=5, padx=2, pady=2)
                transport_entry.grid(column=1, row=5, padx=2, pady=2, columnspan=2)
                transport_entry.insert(tk.END, job_to_edit['public_transport'])

                job_address_label.grid(column=0, row=6, padx=2, pady=2)
                job_address_entry.grid(column=1, row=6, padx=2, pady=2, columnspan=2)
                job_address_entry.insert(tk.END, job_to_edit['job_address'])

                date_label.grid(column=0, row=7, padx=2, pady=2)
                date_entry.grid(column=1, row=7, padx=2, pady=2, columnspan=2)
                date_entry.insert(tk.END, job_to_edit['date_applied'])

                job_status_label.grid(column=0, row=8, padx=2, pady=2)
                job_status_entry.grid(column=1, row=8, padx=2, pady=2, columnspan=2)
                job_status_entry.insert(tk.END, job_to_edit['job_status'])


                update_button.grid(column=2, row=2, padx=2, pady=2)
                update_button.grid(column=2, row=2, padx=2, pady=2)
                # Update data in data frame
                update_button.config(command=lambda: save_changes_func({
                        'update_button': update_button,
                        'job_name': job_name_entry,
                        'job_name_label': job_name_label,
                        'job_type': job_type_entry,
                        'job_type_label': job_type_label,
                        'transport': transport_entry,
                        'transport_label': transport_label,
                        'job_address': job_address_entry,
                        'job_address_label': job_address_label,
                        'date': date_entry,
                        'date_label': date_label,
                        'job_status': job_status_entry,
                        'job_status_label': job_status_label,
                        'data_manager': data_manager,
                        'edit_button': edit_button,
                        'view_all_button': view_all_button,
                        'add_button': add_button,
                        'search_button': search_button,
                        'delete_button': delete_button,
                        'back_to_menu_button': back_to_menu_button,
                        'frm' : frm
                }, index))
            else:
                # Inform user that nothing was selected
                feedback('Please select a job to edit.')
        else:
            # Clear unneeded widgets
            clear_layout([
                job_name_label,
                job_name_entry,
                job_type_label,
                job_type_entry,
                transport_label,
                transport_entry,
                job_address_label,
                job_address_entry,
                date_label,
                date_entry,
                job_status_label,
                job_status_entry,
                edit_button,
                update_button,
            ])
            # Resetting enty values
            job_name_entry.delete(0, tk.END)
            job_type_entry.delete(0, tk.END)
            transport_entry.delete(0, tk.END)
            job_address_entry.delete(0, tk.END)
            date_entry.delete(0, tk.END)
            job_status_entry.delete(0, tk.END)
            back_to_menu(frm, view_all_button, add_button, search_button, delete_button)
            # search_button.grid(column=2, row=2, padx=2, pady=2)
            # view_all_button.grid(column=0, row=2, padx=2, pady=2)
            # add_button.grid(column=1, row=2, padx=2, pady=2)
            search_button.config(text='SEARCH')
            view_all_button.config(text='VIEW ALL')
            edit_button.config(text='EDIT')
        return None

    elif button_id == 'delete_button':
        tree = context['tree']
        data_manager = context['data_manager']
        data = data_manager.load_data()
        item_to_delete = tree.focus()
        index = int(tree.index(item_to_delete))
        # Check if row selected from treeview
        if item_to_delete:
            # Handle removing row from dataframe
            data_manager.delete_row(index)
        return None
    else:
        return None


