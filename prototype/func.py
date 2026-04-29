

def get_info(field):
    done = False
    while not done:
        entry = input(f"Please enter {field}: ")
        check_if_correct = input(f"You entered {entry}. Type y to confirm: ").lower()
        if check_if_correct.startswith('y'):
            done = True
            return entry
    return None



def save_data(jobs_to_save):
    with open('jobs.csv', 'a') as file:
        for job in jobs_to_save:
            file.write(f'\n{job[0]},{job[1]},{job[2]},{job[3]},{job[4]},{job[5]}')



def get_jobs_by_date(date):
    jobs_by_date = []
    with open('jobs.csv', 'r') as file:
        data = file.readlines()
        for i in data:
            i = i.strip().split(',')
            if i[0] == date:
                jobs_by_date.append(i)
    return jobs_by_date


def get_all_jobs():
    jobs = []
    with open('jobs.csv', 'r') as file:
        data = file.readlines()
        for job in data:
            job = job.strip().split(',')
            jobs.append(job)
    return jobs

