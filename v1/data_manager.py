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
        if self.check_if_data(self, new_job_data):
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


    def update_job(self, job_to_edit, index):
        if self.check_if_data(job_to_edit):
            if not index:
                print('Nothing to update')
                return None
            else:
                col_names = self.data.columns.values.tolist()
                print(index)


                self.data.at[index, col_names[0]] = job_to_edit['job_name'].get()
                self.data.at[index, col_names[1]] = job_to_edit['job_type'].get()
                self.data.at[index, col_names[2]] = job_to_edit['transport'].get()
                self.data.at[index, col_names[3]] = job_to_edit['job_address'].get()
                self.data.at[index, col_names[4]] = job_to_edit['date'].get()
                self.data.at[index, col_names[0]] = job_to_edit['job_status'].get()

                self.data.to_csv('job_data.csv', index=False)
                job_to_edit['job_name'].delete(0, tk.END)
                job_to_edit['job_type'].delete(0, tk.END)
                job_to_edit['transport'].delete(0, tk.END)
                job_to_edit['job_address'].delete(0, tk.END)
                job_to_edit['date'].delete(0, tk.END)
                job_to_edit['job_status'].delete(0, tk.END)
                return None
            return None


    def check_if_data(self, job):
        if job['job_name'].get() != '' and job['job_type'].get() != '' and job['transport'].get() != '' and job['job_address'].get() != '' and job['date'].get() != '' and job['job_status'].get() != '':
            return True
        else:
            return False