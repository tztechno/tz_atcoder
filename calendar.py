import calendar
from datetime import datetime
current_date = datetime.now()
year = current_date.year
month = current_date.month
cal = calendar.month(year, month)
print(cal)
