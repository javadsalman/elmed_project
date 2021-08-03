from datetime import datetime, timedelta

def next_weekday_date(next_weekday):
    today = datetime.today()
    this_weekday = today.isoweekday()
    if this_weekday <= next_weekday:
        return today + timedelta(days=next_weekday-this_weekday)
    else:
        return today + timedelta(days=7+next_weekday-this_weekday)
        
    