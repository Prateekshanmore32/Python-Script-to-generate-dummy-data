from datetime import date, timedelta
import pandas as pd
import random

Time = []


def daterange(start, end):
    for n in range(int((end - start).days)):
        yield start + timedelta(n)


start_date = date(2021, 1, 1)
end_date = date(2022, 1, 1)
for single_date in daterange(start_date, end_date):
    for time in range(0, 24):
        if time < 10:
            my_time = f"0{time}:00:00"
        else:
            my_time = f"{time}:00:00"
        date_time = single_date.strftime("%Y-%m-%d") + 'T' + my_time
        date_time_object = pd.to_datetime(date_time)
        Time.append(date_time_object)

Temperature = []


def genetate_temp():
    for datetime in Time:
        if datetime.hour < 12:
            Temperature.append(random.randint(23, 27))
        else:
            Temperature.append(random.randint(33, 37))


genetate_temp()

data = {
    "Time": Time,
    "Temperature": Temperature
}

df = pd.DataFrame(data)
dd = df.to_csv('Data2.csv')