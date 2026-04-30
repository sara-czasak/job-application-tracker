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

