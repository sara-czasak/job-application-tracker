import pandas as pd
import tkinter as tk
import tkinter.ttk as ttk


# SHOW ALL BUTTON
def show_all(data, tree):
    if data.empty:
        return 'No job data added yet'
    else:
        rows = data.iterrows()
        for row in rows:
            tree.insert('', tk.END, values=list(row[1].values))
        return None


def layout_hide_show(button_id, context):
    if button_id == 'view_all':
        print('1. button pressed')
        view_all_button = context['view_all_button']
        tree = context['tree']
        data = context['data']
        if not tree.winfo_viewable():
            print('2. button pressed')
            if data.empty:
                print('3. button pressed')
                return 'No job data added yet'
            else:
                print('4. button pressed')
                rows = data.iterrows()
                for row in rows:
                    tree.insert('', tk.END, values=list(row[1].values))
                    tree.grid(column=0, row=3, columnspan=3, padx=2, pady=2)
                    view_all_button.config(text='HIDE ALL')
                return None
        else:
            tree.grid_remove()
            view_all_button.config(text='VIEW ALL')
            return None
    else:
        return None