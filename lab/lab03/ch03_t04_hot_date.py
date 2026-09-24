from datetime import datetime

now = datetime.now()
current_year = now.year

print('%02d-%-02d-%04d' % (now))