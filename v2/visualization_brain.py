import tkinter
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from stats import *




def apps_per_day_last_week_chart(data):


    dates = data.keys()
    apps = data.values()

    fig, ax = plt.subplots(figsize=(4,4))

    ax.plot(dates, apps, marker='o')
    ax.set_title('Job applications sent out last week')
    ax.set_xlabel('Date')
    ax.set_ylabel('Job applications')
    return fig


def apps_per_cat_chart(data, cats, jobs_per):
    cats = cats.tolist()
    apps = []
    for i in data.values():
        apps.append(len(i))

    fig, ax = plt.subplots(figsize=(4, 4))

    ax.bar(cats, apps)
    ax.set_title(f'Jobs per {jobs_per}')
    ax.set_xlabel('Categories')
    ax.set_ylabel('Job count')
    return fig



if __name__ == '__main__':
    stats = Statistics()
    # data = stats.apps_per_day_last_week()
    data_dict, cat = stats.jobs_per('date_applied')
    # print(data_dict)
    apps_per_cat(data_dict, cat, 'date')
