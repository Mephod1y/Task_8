from datetime import datetime,timedelta
weekdays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
users = {"Max": "2022-11-02", "Tanya": "2022-11-01", "Petro": "2022-10-30", "Stepan": "2022-10-29"}
dates = {}
# date = datetime(year=2022, month=10, day=30)
date = datetime.now()
if datetime.date(date).weekday() == 0:
    for i in range(-2,5):
        dates[weekdays[(datetime.date(date) + timedelta(i)).weekday()]] = f"{datetime.date(date) + timedelta(i)}"
elif datetime.date(date).weekday() in range(1,5):
    for i in range(1,8):
        dates[weekdays[(datetime.date(date) + timedelta(i)).weekday()]] = f"{datetime.date(date) + timedelta(i)}"
elif datetime.date(date).weekday() == 5:
    for i in range(1, 7):
        dates[weekdays[(datetime.date(date) + timedelta(i)).weekday()]] = f"{datetime.date(date) + timedelta(i)}"
else:
    for i in range(-1, 6):
        dates[weekdays[(datetime.date(date) + timedelta(i)).weekday()]] = f"{datetime.date(date) + timedelta(i)}"

res = {"Monday":[],"Tuesday":[],"Wednesday":[],"Thursday":[],"Friday":[],"Saturday":[],"Sunday":[]}
for day,date in dates.items():
    for name,birth in users.items():
        if birth == date:
            res[day].append(name)
sun = res["Sunday"]
sat = res["Saturday"]
for n in sun:
    res["Monday"].append(n)
for n in sat:
    res["Monday"].append(n)
del res["Sunday"]
del res["Saturday"]
result = {}
for key in res:
    if len(res[key]) > 0:
        result[key] = res[key]
print(result)