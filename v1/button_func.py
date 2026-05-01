import tkinter as tk


def clear_layout(items):
    for i in items:
        i.grid_remove()

def layout_hide_show(button_id,context):

    # VIEW ALL BUTTON
    if button_id == 'view_all':
        add_button = context['add_button']
        view_all_button = context['view_all_button']
        tree = context['tree']
        edit_button = context['edit_button']
        data_manager = context['data_manager']
        search_button = context['search_button']
        data = data_manager.load_data()
        if not tree.winfo_viewable():
            if data.empty:
                return 'No job data added yet'
            else:
                clear_layout([add_button,search_button])
                rows = data.iterrows()
                tree.delete(*tree.get_children())
                for row in rows:
                    tree.insert('', tk.END, values=list(row[1].values))
                tree.grid(column=0, row=3, columnspan=3, padx=2, pady=2)
                view_all_button.config(text='HIDE ALL')
                edit_button.grid(column=1, row=2, padx=2, pady=2)
                return None
        else:
            clear_layout([edit_button, tree])
            search_button.grid(column=2, row=2, padx=2, pady=2)
            view_all_button.config(text='VIEW ALL')
            add_button.grid(column=1, row=2, padx=2, pady=2)
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
        if not job_name_label.winfo_viewable():
            clear_layout([view_all_button, search_button])
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
            add_button.config(text='GO BACK')
            add_job_button.grid(column=2, row=2, padx=2, pady=2)
            return None
        else:
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
            job_name_entry.delete(0, tk.END)
            job_type_entry.delete(0, tk.END)
            transport_entry.delete(0, tk.END)
            job_address_entry.delete(0, tk.END)
            date_entry.delete(0, tk.END)
            job_status_entry.delete(0, tk.END)
            search_button.grid(column=2, row=2, padx=2, pady=2)
            view_all_button.grid(column=0, row=2, padx=2, pady=2)
            add_button.config(text='ADD')
            return None

    # SEARCH BUTTON
    elif button_id == 'search_button':
        add_button = context['add_button']
        view_all_button = context['view_all_button']
        search_bar = context['search_bar']
        search_button = context['search_button']
        find_button = context['find_button']
        search_by_options = context['search_by_options']
        opt = context['opt']
        if not search_bar.winfo_viewable():
            clear_layout([view_all_button, add_button])
            search_bar.grid(column=0, row=3, padx=2, pady=2)
            search_by_options.grid(column=2, row=3, padx=2, pady=2)
            search_button.config(text='GO BACK')
            search_button.grid(column=1, row=2, padx=2, pady=2)
            find_button.grid(column=2, row=2, padx=2, pady=2)
            return None
        else:
            clear_layout([find_button, search_by_options,search_bar])
            search_button.config(text='SEARCH')
            search_button.grid(column=2, row=2, padx=2, pady=2)
            opt.set("SEARCH BY")
            search_bar.delete(0, tk.END)
            add_button.grid(column=1, row=2, padx=2, pady=2)
            view_all_button.grid(column=0, row=2, padx=2, pady=2)
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
        data = data_manager.load_data()
        selected_item = tree.focus()
        job_to_edit = {}
        if not job_name_label.winfo_viewable():
            if selected_item:
                job_to_edit = {
                    'job_name': tree.item(selected_item)['values'][0],
                    'job_type': tree.item(selected_item)['values'][1],
                    'public_transport': tree.item(selected_item)['values'][2],
                    'job_address': tree.item(selected_item)['values'][3],
                    'date_applied': tree.item(selected_item)['values'][4],
                    'job_status': tree.item(selected_item)['values'][5],
                }
            clear_layout([tree, view_all_button])
            edit_button.config(text='GO BACK')
            job_name_label.grid(column=0, row=3, padx=2, pady=2)
            job_name_entry.grid(column=1, row=3, padx=2, pady=2, columnspan=2)

            # PREPOPULATE ENTRY FIELDS WITH DATA FROM SELECTED ITEM
            job_name_entry.insert(tk.END, job_to_edit['job_name'])


            # Get index of item to be updated as str
            index = str(data.index[data['job_name'] == job_to_edit['job_name']].tolist())
            print(index)

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
            update_button.config(command=lambda: data_manager.update_job({
                'job_name': job_name_entry,
                'job_type': job_type_entry,
                'transport': transport_entry,
                'job_address': job_address_entry,
                'date': date_entry,
                'job_status': job_status_entry,
            }, index))
        else:
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
                edit_button
            ])
            job_name_entry.delete(0, tk.END)
            job_type_entry.delete(0, tk.END)
            transport_entry.delete(0, tk.END)
            job_address_entry.delete(0, tk.END)
            date_entry.delete(0, tk.END)
            job_status_entry.delete(0, tk.END)
            search_button.grid(column=2, row=2, padx=2, pady=2)
            view_all_button.grid(column=0, row=2, padx=2, pady=2)
            add_button.grid(column=1, row=2, padx=2, pady=2)
            search_button.config(text='SEARCH')
        return None
    else:
        return None
