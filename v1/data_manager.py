import pandas as pd


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
        if new_job_data['job_name'] != '' and new_job_data['job_type'] != '' and new_job_data['transport'] != '' and new_job_data['job_address'] != '' and new_job_data['date'] != '' and new_job_data['job_status']!= '':
            new_job = pd.DataFrame([{
                'job_name': new_job_data['job_name'],
                'job_type': new_job_data['job_type'],
                'public_transport': new_job_data['transport'],
                'job_address': new_job_data['job_address'],
                'date_applied': new_job_data['date'],
                'job_status': new_job_data['job_status']
            }])
            self.data = pd.concat([self.data, new_job], ignore_index=True)
            self.data.to_csv('job_data.csv', index=False)
