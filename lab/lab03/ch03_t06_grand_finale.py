from datetime import datetime

now = datetime.now()
current_month = now.month
current_day = now.day
current_year = now.year
current_hour = now.hour
current_minute 

print('%02d:%02d:%04d' % (now.hour, now.minute, now.second))
