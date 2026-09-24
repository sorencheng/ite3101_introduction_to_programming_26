from datetime import datetime

now = datetime.now()
current_hour = now.hour
current_minute = now.minute
current_second = now.second
print('%02d:%02d:%02d' % (now))
