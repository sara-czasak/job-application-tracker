import pandas as pd
import tkinter as tk
from popups import *
from datetime import datetime


class DataManager:
    def __init__(self):
        self.data = self.load_data()

    # Load in data frame
    def load_data(self):
        # Check if the csv file exists
        try:
            data = pd.read_csv('./job_data.csv')
            return data
        except FileNotFoundError:
            # If csv file doesn't exist create data frame
            df = pd.DataFrame(columns=['job_name', 'job_type', 'public_transport', 'job_address', 'date_applied', 'job_status'])
            return df


    # Save new job to data frame
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
            # Save updated data
            self.data.to_csv('job_data.csv', index=False)
            return True
        else:
            return False


    # Update data frame
    def update_job(self, job_to_edit, index):
        # Check if data exists
        if self.check_if_data(job_to_edit):
            if index is None:
                print('Nothing to update')
                return False
            else:
                col_names = self.data.columns.values.tolist()
                print(col_names[0], col_names[1], col_names[2], col_names[3], col_names[4], col_names[5])
                print(job_to_edit['job_name'].get(), job_to_edit['job_type'].get(), job_to_edit['transport'].get(), job_to_edit['job_address'].get(), job_to_edit['date'].get(), job_to_edit['job_status'].get())
                # Add new data to data frame
                self.data.at[index, col_names[0]] = job_to_edit['job_name'].get()
                self.data.at[index, col_names[1]] = job_to_edit['job_type'].get()
                self.data.at[index, col_names[2]] = job_to_edit['transport'].get()
                self.data.at[index, col_names[3]] = job_to_edit['job_address'].get()
                self.data.at[index, col_names[4]] = job_to_edit['date'].get()
                self.data.at[index, col_names[5]] = job_to_edit['job_status'].get()

                # Save updated data frame
                self.data.to_csv('job_data.csv', index=False)
                return True
        else:
            return False


    # Check if data exists
    def check_if_data(self, job):
        # Check if fields exist
        if job['job_name'].get() != '' and job['job_type'].get() != '' and job['job_address'].get() != '' and job['date'].get() != '' and job['job_status'].get() != '':
            # Format data
            data_dict = {
                'job_name': job['job_name'].get(),
                'job_type': job['job_type'].get(),
                'transport': job['transport'].get(),
                'job_address': job['job_address'].get(),
                'date': job['date'].get(),
                'job_status': job['job_status'].get()
            }
            print(data_dict)
            # Ask user if entered information is correct
            if check_if_info_correct(data_dict):
                return True
            else:
                return False
        else:
            # Inform user that they need to fill out all but one field
            feedback('Only Tram/Bus stop field can be left empty.')
            return False


    # Search through data frame
    def find_rows(self, col_name, value):
        try:
            try:
                # If query is a string convert both column value and query value to lower case
                rows = self.data[self.data[col_name].str.lower() == value.lower()]
            except KeyError:
                # Account for user searching for numerical values that cannot change case
                rows = self.data[self.data[col_name] == value]
            return rows
        except KeyError:
            # Handle user query not found
            print('No data found')
            return None

    # Delete row from data frame
    def delete_row(self, index):
        # Check if index is correct
        if index is None:
            print('Nothing to delete')
            return None
        # Remove row from data frame, reset index, save back to csv file
        self.data = self.data.drop(index)
        self.data = self.data.reset_index(drop=True)
        self.data.to_csv('job_data.csv', index=False)
        return self.data


    def check_if_date(self, date):
        date_format = "%d-%m-%Y"
        try:
            res = bool(datetime.strptime(date, date_format))
            return res
        except ValueError:
            res = False
            return res

