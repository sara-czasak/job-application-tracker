import pandas as pd
import tkinter as tk


class DataManager:
    def __init__(self):
        self.data = self.load_data()

    def load_data(self):
        try:
            data = pd.read_csv('job_data.csv')
            return data
        except FileNotFoundError:
            df = pd.DataFrame(columns=['job_name', 'job_type', 'public_transport', 'job_address', 'date_applied', 'job_status'])
            return df


    def save_new_job(self, new_job_data):
        if self.check_if_data(new_job_data):
            new_job = pd.DataFrame([{
                'job_name': new_job_data['job_name'].get(),
                'job_type': new_job_data['job_type'].get(),
                'public_transport': new_job_data['transport'].get(),
                'job_address': new_job_data['job_address'].get(),
                'date_applied': new_job_data['date'].get(),
                'job_status': new_job_data['job_status'].get()
            }])
            self.data = pd.concat([self.data, new_job], ignore_index=True)
            self.data.to_csv('job_data.csv', index=False)
            new_job_data['job_name'].delete(0, tk.END)
            new_job_data['job_type'].delete(0, tk.END)
            new_job_data['transport'].delete(0, tk.END)
            new_job_data['job_address'].delete(0, tk.END)
            new_job_data['date'].delete(0, tk.END)
            new_job_data['job_status'].delete(0, tk.END)


    def update_job(self, job_to_edit):
        if self.check_if_data(job_to_edit):
            print(job_to_edit['job_name'].get())


    def check_if_data(self, job):
        if job['job_name'].get() != '' and job['job_type'].get() != '' and job['transport'].get() != '' and job['job_address'].get() != '' and job['date'].get() != '' and job['job_status'].get() != '':
            return True
        else:
            return False