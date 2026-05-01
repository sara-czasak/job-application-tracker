import tkinter as tk


def back_to_menu(frm, view_all_button, add_button, search_button):
    children = frm.winfo_children()
    for i in children:
        i.grid_remove()
    view_all_button.grid(column=0, row=2, padx=2, pady=2)
    add_button.grid(column=1, row=2, padx=2, pady=2)
    search_button.grid(column=2, row=2, padx=2, pady=2)

def clear_layout(items):
    for i in items:
        i.grid_remove()


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

    updated = data_manager.update_job({
        'job_name': job_name,
        'job_type': job_type,
        'transport': transport,
        'job_address': job_address,
        'date': date,
        'job_status': job_status,
    }, index)
    if updated:
        clear_layout([
            job_name_label,
            job_name,
            job_type_label,
            job_type,
            transport_label,
            transport,
            job_address_label,
            job_address,
            date_label,
            date,
            job_status_label,
            job_status,
            edit_button,
            update_button,
        ])
        job_name.delete(0, tk.END)
        job_type.delete(0, tk.END)
        transport.delete(0, tk.END)
        job_address.delete(0, tk.END)
        date.delete(0, tk.END)
        job_status.delete(0, tk.END)
        search_button.grid(column=2, row=2, padx=2, pady=2)
        view_all_button.grid(column=0, row=2, padx=2, pady=2)
        add_button.grid(column=1, row=2, padx=2, pady=2)
        search_button.config(text='SEARCH')
        view_all_button.config(text='VIEW ALL')
        edit_button.config(text='EDIT')


def convert_and_search(context):
    opt = context['opt']
    data_manager = context['data_manager']
    search_bar = context['search_bar']
    tree = context['tree']
    search_button = context['search_button']
    search_by = context['search_by_options']
    find_button = context['find_button']
    view_all_button = context['view_all_button']
    edit_button = context['edit_button']
    add_button = context['add_button']
    frm = context['frm']
    back_to_menu_button = context['menu_button']

    if opt.get() == "job name":
        opt = 'job_name'
    elif opt.get() == "date":
        opt = 'date_applied'
    elif opt.get() == 'type':
        opt = 'job_type'
    elif opt.get() == 'bus/tram stop':
        opt = 'public_transport'
    elif opt.get() == 'status':
        opt = 'job_status'
    else:
        opt = ''

    rows = ''

    if opt != '':
        data = data_manager.find_rows(opt, search_bar.get())

        if data is not None:
            if data.empty:
                return 'No data found'
            else:
                clear_layout([search_bar, search_by, find_button, search_button, add_button])
                rows = data.iterrows()
                tree.delete(*tree.get_children())
                for row in rows:
                    tree.insert('', tk.END, values=list(row[1].values))
                tree.grid(column=0, row=3, columnspan=3, padx=2, pady=2)
                back_to_menu_button.grid(column=1, row=2, padx=2, pady=2)
                return None
        return None
    return None




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
        data = data_manager.load_data()
        if not tree.winfo_viewable():
            if data.empty:
                return 'No job data added yet'
            else:
                clear_layout([add_button,search_button, view_all_button])
                rows = data.iterrows()
                tree.delete(*tree.get_children())
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
        if not job_name_label.winfo_viewable():
            clear_layout([view_all_button, search_button, add_button])
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
            add_button.grid(column=1, row=2, padx=2, pady=2)
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

        if not search_bar.winfo_viewable():
            clear_layout([view_all_button, add_button])
            search_bar.grid(column=0, row=3, padx=2, pady=2)
            search_by_options.grid(column=2, row=3, padx=2, pady=2)
            back_to_menu_button.grid(column=1, row=2, padx=2, pady=2)
            find_button.grid(column=2, row=2, padx=2, pady=2)

            find_button.config(command=lambda: convert_and_search({
                    'opt': opt,
                    'data_manager': data_manager,
                    'search_bar': search_bar,
                    'search_button': search_button,
                    'tree': tree,
                    'search_by_options': search_by_options,
                    'find_button': find_button,
                    'view_all_button': view_all_button,
                    'edit_button': add_button,
                    'add_button': add_button,
                    'frm': frm,
                    'menu_button': back_to_menu_button,
                    }))
            return None
        else:
            clear_layout([find_button, search_by_options, search_bar])
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
        # Get index of item to be updated
        index = int(tree.index(selected_item))
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
                edit_button,
                update_button,
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
            view_all_button.config(text='VIEW ALL')
            edit_button.config(text='EDIT')
        return None

    elif button_id == 'delete_button':
        tree = context['tree']
        data_manager = context['data_manager']
        data = data_manager.load_data()
        item_to_delete = tree.focus()
        index = int(tree.index(item_to_delete))
        if item_to_delete:
            data_manager.delete_row(index)
        return None
    else:
        return None


def delete_job(tree, data_manager):
    data = data_manager.load_data()
    item_to_delete = tree.focus()
    index = int(tree.index(item_to_delete))
    if item_to_delete:
        new_data = data_manager.delete_row(index)
        if new_data.empty:
            return 'No job data added yet'
        else:
            rows = new_data.iterrows()
            tree.delete(*tree.get_children())
            for row in rows:
                tree.insert('', tk.END, values=list(row[1].values))
            tree.grid(column=0, row=3, columnspan=3, padx=2, pady=2)
    return None
