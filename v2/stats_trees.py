import tkinter as tk
from tkinter import ttk



def grow_tree(frm, categories, data):
    tree = ttk.Treeview(frm, show='tree')
    for cat in categories:
        parent_id = tree.insert('', 'end', text=cat)
        for _, row in data[cat].iterrows():
            tree.insert(parent_id, 'end', values=list(row.values()))
    return tree