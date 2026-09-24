from datetime import datetime

now = datetime.now()
current_month = now.month
current_day

print('%02d:%02d:%04d' % (now.hour, now.minute, now.second))
