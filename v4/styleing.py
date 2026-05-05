from tkinter import ttk, font



class StyleWidgets:
    def __init__(self, frm):
        self.frm = frm
        self.my_theme()


    def my_theme(self):
        style = ttk.Style()
        style.configure('TButton', font=('Verdana', 10))
        style.map('TButton', foreground=[('pressed', 'blue'), ('!pressed', 'black')],
                  background=[('pressed', 'blue'), ('!pressed', 'white')])
        style.configure('TLabel', font=('Verdana', 10))
        style.configure('TEntry', font=('Verdana', 10))
        style.configure('Treeview', font=('Verdana', 8))




