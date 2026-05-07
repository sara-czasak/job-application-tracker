from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from visualization_brain import *
from tkinter import ttk
# from tkinter import *
import tkinter
from stats_trees import *


# stats = Statistics(lang_center)


def label_maker(text, frm):
    label = ttk.Label(frm, text=text, anchor='e')
    label.grid(column=1, row=0, padx=2, pady=2)
    label.grid_remove()
    return label

def clean_up(frm, lang_center, button = None, table_button=None):
    children = frm.winfo_children()
    for i in children:
        if isinstance(i, ttk.Button):
            pass
        elif isinstance(i, tkinter.Canvas):
            i.destroy()
            if button is not None:
                button.config(text=lang_center.translate("SHOW CHART"))
        elif isinstance(i, ttk.Treeview):
            if not getattr(i, '_is_main_tree', False):
                i.destroy()
        else:
            i.grid_remove()



def percentage_calculator(total, part):
    return f'{((part / total) * 100):.2f}%'


def create_destroy_chart(*func_params, frm, func, button, table_button, lang_center):
    for child in frm.winfo_children():
        if isinstance(child, tkinter.Canvas):
            child.destroy()
            button.config(text=lang_center.translate(lang_center.translate("SHOW CHART")))
            return
    for child in frm.winfo_children():
        if isinstance(child, tkinter.ttk.Treeview):
            if not getattr(child, '_is_main_tree', False):
                child.destroy()
                table_button.config(text=lang_center.translate("SHOW TABLE"))


    fig = func(*func_params)
    canvas = FigureCanvasTkAgg(fig, master=frm)
    canvas.draw()
    canvas.get_tk_widget().grid(column=4, row=0, padx=2, pady=2, columnspan=3, rowspan=10)
    button.config(text=lang_center.translate("HIDE CHART"))


def create_destroy_tree(*params, frm, button, chart_button, lang_center):
    for child in frm.winfo_children():
        if isinstance(child, tkinter.ttk.Treeview):
            if not getattr(child, '_is_main_tree', False):
                child.destroy()
                button.config(text=lang_center.translate("SHOW TABLE"))
                return
    for child in frm.winfo_children():
        if isinstance(child, tkinter.Canvas):
            child.destroy()
            chart_button.config(text=lang_center.translate("SHOW CHART"))

    tree = grow_tree(frm, *params)
    tree.grid(column=4, row=0, padx=2, pady=2, columnspan=3, rowspan=10)
    button.config(text=lang_center.translate("HIDE TABLE"))


def show_statistics(button_id, context):
    lang_center = context['lang_center']
    stats = Statistics(lang_center)
    stats.data = stats.load_data()
    total_rows = len(stats.data)

    if button_id == 'average_per_day_button':
        frm = context['frm']
        chart_button = context['chart_button']
        table_button = context['table_button']
        lang_center = context['lang_center']
        clean_up(frm, lang_center)
        chart_button.grid_remove()
        chart_button.config(text=lang_center.translate("SHOW CHART"))
        table_button.grid_remove()
        table_button.config(text=lang_center.translate("SHOW TABLE"))

        average_apps_per_day_label = label_maker(lang_center.translate("Average Apps per Day:",), frm)
        average_apps_per_day_label.grid(column=0, row=5, padx=2, pady=2)
        per_day_average = stats.apps_per_day()
        average_apps_per_day_stat = label_maker(f'{lang_center.translate("Amount: ")}{per_day_average}\n{lang_center.translate("Percent: ")}{percentage_calculator(total_rows, per_day_average)}', frm)
        average_apps_per_day_stat.grid(column=1, row=5, padx=2, pady=2)
        return None

    elif button_id == 'jobs_per_status_button':
        frm = context['frm']
        chart_button = context['chart_button']
        table_button = context['table_button']
        lang_center = context['lang_center']
        clean_up(frm,lang_center, chart_button)

        jobs_per_status_label = label_maker(lang_center.translate("Jobs per Status:"), frm)
        jobs_per_status_label.grid(column=0, row=5, padx=2, pady=2)
        jobs, category = stats.jobs_per('job_status')
        row_num = 7
        for index, cat in enumerate(category):
            per_status = len(jobs[cat])
            label_maker(f'{cat}:\n\t{lang_center.translate("Amount: ")}{per_status}\n\t{lang_center.translate("Percent: ")}{percentage_calculator(total_rows, per_status)}', frm).grid(column=1, row=(index + 6), padx=2, pady=2)
            row_num += index


        chart_button.grid(column=0, row=6, padx=2, pady=2)
        chart_button.config(
            command=lambda: create_destroy_chart(jobs, category, 'status', frm=frm, func=apps_per_cat_chart, button=chart_button, table_button=table_button, lang_center=lang_center))

        table_button.grid(column=0, row=7, padx=2, pady=2)
        table_button.config(command=lambda c=category, j=jobs: create_destroy_tree(c, j, frm=frm, button=table_button, chart_button=chart_button, lang_center=lang_center))
        return None

    elif button_id == 'jobs_per_type_button':
        frm = context['frm']
        chart_button = context['chart_button']
        table_button = context['table_button']

        clean_up(frm,lang_center, chart_button, table_button)

        jobs_per_type_label = label_maker(lang_center.translate("Jobs per Type:"), frm)
        jobs_per_type_label.grid(column=0, row=5, padx=2, pady=2)
        jobs, category = stats.jobs_per('job_type')
        row_num = 6
        for index, cat in enumerate(category):
            per_type = len(jobs[cat])
            label_maker(f'{cat}:\n\t{lang_center.translate("Amount: ")}{per_type}\n\t{lang_center.translate("Percent: ")}{percentage_calculator(total_rows, per_type)}', frm).grid(column=1, row=(index + 6), padx=2, pady=2)
            row_num += index


        chart_button.grid(column=0, row=6, padx=2, pady=2)
        chart_button.config(
            command=lambda: create_destroy_chart(jobs, category, 'type', frm=frm, func=apps_per_cat_chart, button=chart_button, table_button=table_button, lang_center=lang_center))

        table_button.grid(column=0, row=7, padx=2, pady=2)
        table_button.config(command=lambda c=category, j=jobs: create_destroy_tree(c, j, frm=frm, button=table_button,chart_button=chart_button, lang_center=lang_center))
        return None

    elif button_id == 'jobs_per_date_button':
        frm = context['frm']
        chart_button = context['chart_button']
        table_button = context['table_button']

        chart_button.config(text=lang_center.translate("SHOW CHART"))
        table_button.config(text=lang_center.translate("SHOW TABLE"))

        clean_up(frm,lang_center, chart_button)

        jobs_per_type_label = label_maker("Jobs per Date:", frm)
        jobs_per_type_label.grid(column=0, row=5, padx=2, pady=2)
        jobs, category = stats.jobs_per('date_applied')
        row_num = 6
        for index, cat in enumerate(category):
            per_date = len(jobs[cat])
            label_maker(f'{cat}:\n\t{lang_center.translate("Amount: ")}{per_date}\n\t{lang_center.translate("Percent: ")}{percentage_calculator(total_rows, per_date)}', frm).grid(column=1, row=(index + 6), padx=2, pady=2)
            row_num += index

        chart_button.grid(column=0, row=6, padx=2, pady=2)
        chart_button.config(
            command=lambda: create_destroy_chart(jobs, category, 'date', frm=frm, func=apps_per_cat_chart, button=chart_button, table_button=table_button, lang_center=lang_center))

        table_button.grid(column=0, row=7, padx=2, pady=2)
        table_button.config(command=lambda c=category, j=jobs: create_destroy_tree(c, j, frm=frm, button=table_button,chart_button=chart_button, lang_center=lang_center))
        return None


    elif button_id == 'apps_sent_last_week_button':
        frm = context['frm']
        chart_button = context['chart_button']
        table_button = context['table_button']
        table_button.grid_remove()
        table_button.config(text=lang_center.translate('SHOW TABLE'))

        clean_up(frm, lang_center, chart_button)

        week = stats.apps_in_last_week()
        apps_last_week_label = label_maker(lang_center.translate("Apps sent out last week:"), frm)
        apps_last_week_label.grid(column=0, row=5, padx=2, pady=2)
        apps_last_week_stat = label_maker(f'{lang_center.translate("Amount: ")}{week}\n{lang_center.translate("Percent: ")}{percentage_calculator(total_rows, week)}', frm)
        apps_last_week_stat.grid(column=1, row=5, padx=2, pady=2)

        data = stats.apps_per_day_last_week()
        chart_button.grid(column=0, row=6, padx=2, pady=2)

        chart_button.config(command=lambda: create_destroy_chart(data, frm=frm, func=apps_per_day_last_week_chart, button=chart_button, table_button=table_button, lang_center=lang_center))

        return None

    return None
