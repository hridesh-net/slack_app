import datetime

tomorrow = datetime.date.today() + datetime.timedelta(days=1)
scheduled_time = datetime.time(hour=9, minute=30)
schedule_timestamp = datetime.datetime.combine(tomorrow, scheduled_time)
sec = schedule_timestamp.timestamp()

print(schedule_timestamp)

print(sec)