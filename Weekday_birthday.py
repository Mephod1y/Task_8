from datetime import datetime,timedelta
users = [{"name": "Max", "birthday": datetime(year=2022, month=11, day=2)},
         {"name": "Tanya", "birthday": datetime(year=2022, month=11, day=2)},
         {"name":"Petro", "birthday": datetime(year=2022, month=10, day=30)},
         {"name":"Stepan", "birthday": datetime(year=2022, month=11, day=5)}]
dates = []
date = datetime.now()

def get_birthday(users):
    if datetime.date(date).weekday() == 0:
        for i in range(-2, 5):
            dates.append(f"{datetime.date(date + timedelta(i))}")
    elif datetime.date(date).weekday() in range(1, 5):
        for i in range(1, 8):
            dates.append(f"{datetime.date(date + timedelta(i))}")
    elif datetime.date(date).weekday() == 5:
        for i in range(1, 7):
            dates.append(f"{datetime.date(date + timedelta(i))}")
    else:
        for i in range(-1, 6):
            dates.append(f"{datetime.date(date + timedelta(i))}")

    res = {"Monday":[],"Tuesday":[],"Wednesday":[],"Thursday":[],"Friday":[],"Saturday":[],"Sunday":[]}

    for user in users:
        birth = datetime.date(datetime(year=user.get('birthday').year, month=user.get('birthday').month, day=user.get('birthday').day)).strftime("%Y-%m-%d")
        if birth in dates:
            weekday = datetime.date(datetime(year=user.get('birthday').year, month=user.get('birthday').month,
                                             day=user.get('birthday').day)).strftime("%A")
            if weekday in ['Saturday', 'Sunday']:
                weekday = 'Monday'
            res.get(weekday).append(user.get('name'))

    for key, value in res.items():
        if value:
            print(f"{key}: {', '.join(value)}")

print(get_birthday(users))
