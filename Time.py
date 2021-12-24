from datetime import date, timedelta
import pandas as pd

Time = []


def date_range(start, end):
    for n in range(int((end - start).days)):
        yield start + timedelta(n)


def generate_time():
    start_date = date(2021, 1, 1)
    end_date = date(2022, 1, 1)
    for single_date in date_range(start_date, end_date):
        for time in range(0, 24):
            if time < 10:
                my_time = f"0{time}:00:00"
            else:
                my_time = f"{time}:00:00"
            date_time = single_date.strftime("%Y-%m-%d") + 'T' + my_time
            date_time_object = pd.to_datetime(date_time)
            Time.append(date_time_object)

    return Time
