# problem2/problem2.py
def date_format(date_str):
    month, day, year = date_str.split('/')
    return f"{year}-{month}-{day}"
