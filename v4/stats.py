from data_manager import DataManager
import datetime as dt


class Statistics(DataManager):
    def __init__(self):
        super(Statistics, self).__init__()
        self.data = self.load_data()


    def apps_per_day(self):
        unique_dates = self.data['date_applied'].unique()
        all_apps = len(self.data)
        avr = all_apps / len(unique_dates)
        return int(avr)


    def jobs_per(self, category):
        unique_category = self.data[category].unique()
        data_dict = {}
        for cat in unique_category:
            data_dict[cat] = self.data[self.data[category] == cat]
        return data_dict, unique_category


    def find_data(self, value):
        return self.data[self.data['date_applied'] == value]


    def apps_in_last_week(self):
        now = dt.datetime.now()

        dates = [(now - dt.timedelta(x)).strftime("%d-%m-%Y") for x in range(7)]
        total_apps = 0
        for date in dates:
            try:
                total_apps += len(self.find_data(date))
            except KeyError:
                pass
        return total_apps


    def apps_per_day_last_week(self):
        now = dt.datetime.now()
        dates = [(now - dt.timedelta(x)).strftime("%d-%m-%Y") for x in range(7)]
        data_dict = {}
        for date in dates[::-1]:
            try:
                count = len(self.find_data(date))
                date = date.split('-')
                date = date[0] + '/' + date[1]
                data_dict[date] = count
            except KeyError:
                count = 0
                data_dict[date] = count
        return data_dict



if __name__ == '__main__':
    statistics = Statistics()
    # print(statistics.apps_per_day_last_week())
    # dict, cat = statistics.jobs_per('job_type')
    # print(cat)
    # for i in dict.values():
    #     print(len(i))

