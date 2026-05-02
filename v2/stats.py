from v2.data_manager import DataManager
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
        dict = {}
        for cat in unique_category:
            dict[cat] = self.data[self.data[category] == cat]
        return dict, unique_category


    def find_data(self, value):
        data = self.data[self.data[value]]
        return data


    def apps_in_last_week(self):
        now = dt.datetime.now()

        dates = [(now - dt.timedelta(x)).strftime("%d-%m-%Y") for x in range(7)]
        print(dates)
        total_apps = 0
        for date in dates:
            try:
                total_apps += len(self.find_data(date))
            except KeyError:
                pass
        return total_apps


if __name__ == '__main__':
    statistics = Statistics()
    statistics.apps_in_last_week()

