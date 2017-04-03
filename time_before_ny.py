import datetime


def time_before_ny():
    today = datetime.date.today()

    wanted_day = datetime.date(
        year=today.year + 1,
        month=1,
        day=1,
    )

    return wanted_day - today
