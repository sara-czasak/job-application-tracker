import tkinter as tk
from tkinter import messagebox


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


# def choose_language():
#     language = tk.messagebox.askquestion(
#         title="Choose language", options='English, Spanish, Polish'
#     )
#     return language