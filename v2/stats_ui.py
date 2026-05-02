from tkinter import *
from tkinter import ttk
from stats import *


stats = Statistics()


def label_maker(text, frm):
    label = ttk.Label(frm, text=text, anchor='e')
    label.grid(column=1, row=0, padx=2, pady=2)
    label.grid_remove()
    return label


def destroy_labels(labels):
    for label in labels:
        label.destroy()


def show_statistics(button_id, context):
    if button_id == 'average_per_day_button':
        frm = context['frm']

        average_apps_per_day_label = label_maker("Average Apps per Day:", frm)
        average_apps_per_day_label.grid(column=0, row=5, padx=2, pady=2)
        average_apps_per_day_stat = label_maker(stats.apps_per_day(), frm)
        average_apps_per_day_stat.grid(column=1, row=5, padx=2, pady=2)
        return None

    elif button_id == 'jobs_per_status_button':
        frm = context['frm']

        jobs_per_status_label = label_maker("Jobs per Status:", frm)
        jobs_per_status_label.grid(column=0, row=5, padx=2, pady=2)
        jobs, category = stats.jobs_per('job_status')
        for index, cat in enumerate(category):
            label_maker(f'{cat}: {len(jobs[cat])}', frm).grid(column=1, row=(index + 6), padx=2, pady=2)
        return None

    elif button_id == 'jobs_per_type_button':
        frm = context['frm']

        jobs_per_type_label = label_maker("Jobs per Type:", frm)
        jobs_per_type_label.grid(column=0, row=5, padx=2, pady=2)
        jobs, category = stats.jobs_per('job_type')
        for index, cat in enumerate(category):
            label_maker(f'{cat}: {len(jobs[cat])}', frm).grid(column=1, row=(index + 6), padx=2, pady=2)
        return None

    elif button_id == 'jobs_per_date_button':
        frm = context['frm']

        jobs_per_type_label = label_maker("Jobs per Date:", frm)
        jobs_per_type_label.grid(column=0, row=5, padx=2, pady=2)
        jobs, category = stats.jobs_per('date_applied')
        for index, cat in enumerate(category):
            label_maker(f'{cat}: {len(jobs[cat])}', frm).grid(column=1, row=(index + 6), padx=2, pady=2)
        return None

    return None
