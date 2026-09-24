from datetime import datetime

now = datetime.now()
current_month = now.month
current_day = now.day
current_year = now.year
current_hour = now.hour
current_minute = now.minute
current_second = now.second


print('%02d%02d/%04d % (now.month, now.day, now.year))
print('%02d%02d:%02d' % (now.hour, now.minute, now.second))
