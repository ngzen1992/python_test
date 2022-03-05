from datetime import datetime, timedelta
import time
import calendar

datetime_object = None
new_datetime = None

def add_time(start, duration, start_day = None):
    datetime_object = datetime.strptime(start, '%I:%M %p')
    new_datetime = datetime_object + timedelta(hours=int(duration.split(':')[0]), minutes=int(duration.split(':')[1]))
    added_day = new_datetime.day - 1

    if (start_day is not None):
        if (added_day > 1):
            return datetime.strftime(new_datetime, '%-I:%M %p') + ', ' + add_day(start_day, added_day) + ' (' + str(added_day) + ' days later)'
        elif (added_day == 1):
            end_date = datetime.strptime(start_day, '%A') + timedelta(days=added_day)
            return datetime.strftime(new_datetime, '%-I:%M %p') + ', ' + add_day(start_day, added_day) + ' (next day)'
        else:
            return datetime.strftime(new_datetime, '%-I:%M %p') + ', ' + start_day
    else:
        if (added_day > 1):
            return datetime.strftime(new_datetime, '%-I:%M %p') + ' (' + str(added_day) + ' days later)'
        elif (added_day == 1):
            return datetime.strftime(new_datetime, '%-I:%M %p') + ' (next day)'
        else:
            return datetime.strftime(new_datetime, '%-I:%M %p')

def add_day(weekday, add_day):
    days = dict(zip(calendar.day_name, range(7))); 
    weekday_as_int = days[weekday.capitalize()]
    weekday_added_as_int = weekday_as_int + add_day
    while(weekday_added_as_int > 6):
        weekday_added_as_int = weekday_added_as_int - 7
    return calendar.day_name[weekday_added_as_int]

# print(add_time("3:00 PM", "3:10"))
# print(add_time("11:30 AM", "2:32", "Monday"))
# print(add_time("11:43 AM", "00:20"))
# print(add_time("10:10 PM", "3:30"))
# print(add_time("11:43 PM", "24:20", "tueSday"))
# print(add_time("6:30 PM", "205:12"))
print(add_time("2:59 AM", "24:00", "Saturday"))
print(add_time("11:59 PM", "24:05", "Wednesday"))