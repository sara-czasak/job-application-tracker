import datetime
from func import *


jobs_to_save = []
today = datetime.date.today().strftime("%d-%m-%Y")


options = input("Please select:\n1 to add new jobs\n2 to see a list of all jobs or\n3 to check jobs you applied for by date: ")

if options == '1':
    job_data = False
    while not job_data:
        job = []
        new_entry = input("Would you like to add a job? (y/n): ")
        if new_entry.lower().startswith('n'):
            job_data = True
        else:
            job.append(today)

            category = get_info('category (e.g.: Retail, Food Industry, Customer Service)')
            job.append(category)

            job_name = get_info("workplace name (e.g.: Awitex, Orange Polska)")
            job.append(job_name)

            job_address = get_info(f"address for {job_name} (e.g.: Karmelicka 10)")
            job.append(job_address)

            transportation = get_info('transportation stops near by (e.g. Teatr Bagatela)')
            job.append(transportation)

            status = get_info("status (e.g.: Waiting to hear back, interview set for DD-MM-YYYY)")
            job.append(status)

            jobs_to_save.append(job)
            job = []

    save_data(jobs_to_save)

elif options == '2':
    jobs = get_all_jobs()
    print("JOB NAME | JOB CATEGORY | DATE APPLIED | JOB ADDRESS | TRANSPORTATION | STATUS")
    for job in jobs:
        print(f'{job[2]} | {job[1]} | {job[0]} | {job[3]} | {job[4]} | {job[5]}')

elif options == '3':
    date = get_info('the date you would like to check (DD-MM-YYYY)')
    jobs = get_jobs_by_date(date)
    for job in jobs:
        print(f'\nJOB NAME: {job[2]}\nDATE WHEN APPLIED: {job[0]}\nJOB CATEGORY: {job[1]}\nJOB ADDRESS: {job[3]}\nTRANSPORTATION STOPS: {job[4]}\nSTATUS: {job[5]}\n\n')
