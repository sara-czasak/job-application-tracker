from tkinter import *
from tkinter import ttk
from stats import *


stats = Statistics()


def label_maker(text, frm):
    label = ttk.Label(frm, text=text, anchor='e')
    label.grid(column=1, row=0, padx=2, pady=2)
    label.grid_remove()
    return label

def clean_up(frm):
    children = frm.winfo_children()
    for i in children:
        if isinstance(i, ttk.Button):
            pass
        else:
            i.grid_remove()


def percentage_calculator(total, part):
    return f'{((part / total) * 100):.2f}%'


def show_statistics(button_id, context):
    total_rows = len(stats.load_data())

    if button_id == 'average_per_day_button':
        frm = context['frm']
        clean_up(frm)

        average_apps_per_day_label = label_maker("Average Apps per Day:", frm)
        average_apps_per_day_label.grid(column=0, row=5, padx=2, pady=2)
        per_day_average = stats.apps_per_day()
        average_apps_per_day_stat = label_maker(f'Amount: {per_day_average}\nPercent: {percentage_calculator(total_rows, per_day_average)}', frm)
        average_apps_per_day_stat.grid(column=1, row=5, padx=2, pady=2)
        return None

    elif button_id == 'jobs_per_status_button':
        frm = context['frm']
        clean_up(frm)

        jobs_per_status_label = label_maker("Jobs per Status:", frm)
        jobs_per_status_label.grid(column=0, row=5, padx=2, pady=2)
        jobs, category = stats.jobs_per('job_status')
        for index, cat in enumerate(category):
            per_status = len(jobs[cat])
            label_maker(f'{cat}:\n\tAmount: {per_status}\n\tPercent: {percentage_calculator(total_rows, per_status)}', frm).grid(column=1, row=(index + 6), padx=2, pady=2)
        return None

    elif button_id == 'jobs_per_type_button':
        frm = context['frm']
        clean_up(frm)

        jobs_per_type_label = label_maker("Jobs per Type:", frm)
        jobs_per_type_label.grid(column=0, row=5, padx=2, pady=2)
        jobs, category = stats.jobs_per('job_type')
        for index, cat in enumerate(category):
            per_type = len(jobs[cat])
            label_maker(f'{cat}:\n\tAmount: {per_type}\n\tPercent: {percentage_calculator(total_rows, per_type)}', frm).grid(column=1, row=(index + 6), padx=2, pady=2)
        return None

    elif button_id == 'jobs_per_date_button':
        frm = context['frm']
        clean_up(frm)

        jobs_per_type_label = label_maker("Jobs per Date:", frm)
        jobs_per_type_label.grid(column=0, row=5, padx=2, pady=2)
        jobs, category = stats.jobs_per('date_applied')
        for index, cat in enumerate(category):
            per_date = len(jobs[cat])
            label_maker(f'{cat}:\n\tAmount: {per_date}\n\tPercent: {percentage_calculator(total_rows, per_date)}', frm).grid(column=1, row=(index + 6), padx=2, pady=2)
        return None


    elif button_id == 'apps_sent_last_week_button':
        frm = context['frm']
        clean_up(frm)

        week = stats.apps_in_last_week()
        apps_last_week_label = label_maker("Apps sent out last week:", frm)
        apps_last_week_label.grid(column=0, row=5, padx=2, pady=2)
        apps_last_week_stat = label_maker(f'Amount: {week}\nPercent: {percentage_calculator(total_rows, week)}', frm)
        apps_last_week_stat.grid(column=1, row=5, padx=2, pady=2)
        return None

    return None
