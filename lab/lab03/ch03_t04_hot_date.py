from datetime import datetime

now = datetime.now()
current_month = now.month
current_year = now.year
current_day = now.day
print('%02d/%02d/%04d' % (now.month, now.day, now.year))
