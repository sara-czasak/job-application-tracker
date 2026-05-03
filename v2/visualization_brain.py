import tkinter
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from stats import *


plt.figure(figsize=(4,4))

def apps_per_day_last_week_chart(data_dict):


    dates = data_dict.keys()
    apps = data_dict.values()

    plt.plot(dates, apps, marker='o')
    plt.title('Job applications sent out last week')
    plt.xlabel('Date')
    plt.ylabel('Job applications')
    plt.show()


def apps_per_cat(data, cats, jobs_per):
    cats = cats.tolist()
    apps = []
    for i in data.values():
        apps.append(len(i))

    plt.bar(cats, apps)
    plt.title(f'Jobs per {jobs_per}')
    plt.xlabel('Categories')
    plt.ylabel('Job count')
    plt.show()












if __name__ == '__main__':
    stats = Statistics()
    # data = stats.apps_per_day_last_week()
    data_dict, cat = stats.jobs_per('date_applied')
    # print(data_dict)
    apps_per_cat(data_dict, cat, 'date')
