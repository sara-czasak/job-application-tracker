import tkinter as tk
from tkinter import messagebox


def feedback(message):
    popup = tk.messagebox.showwarning(title="Error", message=message)
    return popup


def check_if_info_correct(info):
    check = messagebox.askquestion(
        title="Check if everything is correct",
        message=f'Job Name: {info["job_name"]}\nJob Type: {info["job_type"]}\nPublic Transport Stop: {info["transport"]}\nJob Address: {info["job_address"]}\nDate Applied: {info["date"]}\nJob Status: {info["job_status"]}')
    if check == "yes":
        return True
    else:
        return False


def are_you_sure():
    check = tk.messagebox.askquestion("Are you sure?", "Please duble check you want to proceed")
    if check == "yes":
        return True
    else:
        return False

