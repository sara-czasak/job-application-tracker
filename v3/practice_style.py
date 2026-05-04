import tkinter as tk
from styleing import *
from tkinter import ttk, font

root = tk.Tk()
root.minsize(250,70)
root.title("JOB HUNT HELPER")
root.geometry("250x250")
frm = ttk.Frame(root, padding=10)
frm.pack()

print(font.families())
style = ttk.Style()
# style.theme_use('classic')

style.configure('new.TButton', foreground='green', font=('Javanese Text', 20))
style.map('new.TButton', foreground=[
    ('pressed', 'red'),
    ('disabled', 'yellow'),
    ('!disabled', 'blue'),
],
          background=[
              ('pressed', 'red'),
              ('disabled', 'yellow'),
              ('!disabled', 'blue'),
          ])


# style = StyleWidgets(frm)

button1 = ttk.Button(root, text="Button 1", style='new.TButton')
button1.pack()
button2 = ttk.Button(root, text="Button 2")
button2.pack()
label1 = ttk.Label(frm, text="Label 1")
label1.pack()
label2 = ttk.Label(frm, text="Label 2")
label2.pack()






# style.style_buttons()
root.mainloop()