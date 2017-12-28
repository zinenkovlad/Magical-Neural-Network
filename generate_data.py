import random
import numpy as np
import pandas as pd


def convert_to_zodiac(day, month):
    if (month == 3 and day > 20) or (month == 4 and day < 21):
        return "Aries"
    elif (month == 4 and day > 20) or (month == 5 and day < 21):
        return "Taurus"
    elif (month == 5 and day > 20) or (month == 6 and day < 22):
        return "Gemini"
    elif (month == 6 and day > 21) or (month == 7 and day < 23):
        return "Cancer"
    elif (month == 7 and day > 22) or (month == 8 and day < 24):
        return "Leo"
    elif (month == 8 and day > 23) or (month == 9 and day < 24):
        return "Virgo"
    elif (month == 9 and day > 23) or (month == 10 and day < 24):
        return "Libra"
    elif (month == 10 and day > 23) or (month == 11 and day < 23):
        return "Scorpio"
    elif (month == 11 and day > 22) or (month == 12 and day < 22):
        return "Sagittarius"
    elif (month == 12 and day > 21) or (month == 1 and day < 21):
        return "Capricorn"
    elif (month == 1 and day > 20) or (month == 2 and day < 19):
        return "Aquarius"
    elif (month == 2 and day > 18) or (month == 3 and day < 21):
        return "Pisces"


if __name__ == "__main__":
    n_records = 500
    zodiacs = np.zeros((n_records, 3), dtype=object)
    for i in range(n_records):
        day, month = random.randint(1, 31), random.randint(1, 12)
        zodiacs[i, :] = day, month, convert_to_zodiac(day, month)
    pd.DataFrame(zodiacs, columns=['day', 'month', 'zodiac']).to_csv('zodiacs.csv')
