import tkinter
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from stats import *


def apps_per_day_last_week_chart(data_dict):
    plt.figure(figsize=(4,4))

    dates = data_dict.keys()
    apps = data_dict.values()

    plt.plot(dates, apps, marker='o')
    plt.title('Job applications sent out last week')
    plt.xlabel('Date')
    plt.ylabel('Job applications')
    plt.show()











if __name__ == '__main__':
    stats = Statistics()
    data = stats.apps_per_day_last_week()
    apps_per_day_last_week_chart(data)
