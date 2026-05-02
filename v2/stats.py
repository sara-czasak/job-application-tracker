from v2.data_manager import DataManager


class Statistics(DataManager):
    def __init__(self):
        super(Statistics, self).__init__()
        self.data = self.load_data()


    def apps_per_day(self):
        unique_dates = self.data['date_applied'].unique()
        all_apps = len(self.data)
        avr = all_apps / len(unique_dates)
        return int(avr)


    # WIP METHOD
    def jobs_per_status(self):
        unique_status = self.data['job_status'].unique()
        jobs = []
        for status in unique_status:
            self.find_rows('job_status', status)



if __name__ == '__main__':
    statistics = Statistics()
    statistics.jobs_per_status()