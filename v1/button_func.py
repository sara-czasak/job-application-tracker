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
