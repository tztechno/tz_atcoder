from datetime import datetime
current_date = datetime.now()
formatted_date = current_date.strftime("%Y-%m-%d")
print("Today is", formatted_date, ".")
