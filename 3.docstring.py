def readable_timedelta(days):
    # insert your docstring here
    """Know the number of day(s) and week(s) there is.
    INPUT:
    days: int. The number of days
    weeks: int. The number of weeks 
    OUTPUT:
    readable_timedelta: The week(s) and day(s) there is in a particular number of days""" 
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)