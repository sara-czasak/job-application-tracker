


def show_all_jobs(data):
    if data.empty:
        return 'No jobs added yet'
    else:
        return data.to_dict().values()