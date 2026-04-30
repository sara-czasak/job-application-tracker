import tkinter as tk


def layout_hide_show(button_id, context):
    if button_id == 'view_all':
        add_button = context['add_button']
        view_all_button = context['view_all_button']
        tree = context['tree']
        data = context['data']
        edit_button = context['edit_button']
        if not tree.winfo_viewable():
            if data.empty:
                return 'No job data added yet'
            else:
                rows = data.iterrows()
                for row in rows:
                    tree.insert('', tk.END, values=list(row[1].values))
                    tree.grid(column=0, row=3, columnspan=3, padx=2, pady=2)
                    view_all_button.config(text='HIDE ALL')
                    edit_button.grid(column=1, row=2, padx=2, pady=2)
                    add_button.grid_remove()
                return None
        else:
            edit_button.grid_remove()
            tree.grid_remove()
            view_all_button.config(text='VIEW ALL')
            add_button.grid(column=1, row=2, padx=2, pady=2)
            return None
    else:
        return None