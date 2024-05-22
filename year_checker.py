def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False

def leap_year_list(start, stop):
    years = []
    for year in range(start, stop):
        if is_leap_year(year):
            years.append(year)
    return years