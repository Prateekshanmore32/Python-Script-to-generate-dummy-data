from Time import Time
import random

Temperature = []


def genetate_temp():
    for datetime in Time:
        if datetime.hour < 12:
            Temperature.append(random.randint(23, 27))
        else:
            Temperature.append(random.randint(33, 37))
    return Temperature
