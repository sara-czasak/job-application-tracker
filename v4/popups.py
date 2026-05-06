import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk


# Handle user error feedback
def feedback(message):
    popup = tk.messagebox.showwarning(title="Error", message=message)
    return popup


# Check if entries are correct
def check_if_info_correct(info):
    check = messagebox.askquestion(
        title="Check if everything is correct",
        message=f'Job Name: {info["job_name"]}\nJob Type: {info["job_type"]}\nPublic Transport Stop: {info["transport"]}\nJob Address: {info["job_address"]}\nDate Applied: {info["date"]}\nJob Status: {info["job_status"]}')
    if check == "yes":
        return True
    else:
        return False


# Check if user is sure they want to proceed
def are_you_sure():
    check = tk.messagebox.askquestion("Are you sure?", "Please duble check you want to proceed")
    if check == "yes":
        return True
    else:
        return False


def language_menu(root):
    root.withdraw()
    window = tk.Toplevel()
    window.title("CHOOSE LANGUAGE")
    label = tk.Label(window, text="SELECT LANGUAGE")
    label.pack(padx=5, pady=5)

    language_choice = {'lang': None}

    def wait_for_choice(lang):
        language_choice['lang'] = lang
        window.destroy()
        root.deiconify()

    ang = ttk.Button(window, text='ANG', command=lambda: wait_for_choice('ANG'))
    ang.pack(padx=5, pady=5)
    es = ttk.Button(window, text='ES', command=lambda: wait_for_choice('ES'))
    es.pack(padx=5, pady=5)
    pl = ttk.Button(window, text='PL', command=lambda: wait_for_choice('PL'))
    pl.pack(padx=5, pady=5)

    window.wait_window()
    return language_choice['lang']

