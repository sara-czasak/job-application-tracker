from tkinter import ttk, font



class StyleWidgets:
    def __init__(self, frm):
        self.frm = frm
        self.style_buttons()


    def style_buttons(self):
        style = ttk.Style()
        style.configure('TButton', font=('Verdana', 10))
        style.map('TButton', foreground=[('pressed', 'blue'), ('!pressed', 'black')],
                  background=[('pressed', 'blue'), ('!pressed', 'white')])

        children = self.frm.winfo_children()
        for i in children:
            if isinstance(i, ttk.Button):
                pass

