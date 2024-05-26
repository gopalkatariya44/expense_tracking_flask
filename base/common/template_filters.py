from datetime import datetime

import pytz

from base import app


@app.template_filter('utc_to_local_date')
def utc_to_local_date(value):
    utc_timezone = pytz.timezone('UTC')
    local_timezone = pytz.timezone('Asia/Kolkata')
    value_utc = utc_timezone.localize(value)
    value_local = value_utc.astimezone(local_timezone)
    return value_local.strftime('%Y-%m-%d')


@app.template_filter('utc_to_local_time')
def utc_to_local_time(value):
    utc_timezone = pytz.timezone('UTC')
    local_timezone = pytz.timezone('Asia/Kolkata')
    value_utc = utc_timezone.localize(value)
    value_local = value_utc.astimezone(local_timezone)
    return value_local.strftime('%H:%M')


@app.template_filter('float_to_int')
def float_to_int(value):
    if value is int:
        return int(value)
    return value


@app.template_filter('utc_to_str')
def utc_to_local_time(timestamp_str):
    # Convert the timestamp string to a datetime object
    timestamp = datetime.strptime(timestamp_str, '%d %b, %Y %I:%M %p')

    # Calculate the time difference between the current time and the timestamp
    time_difference = datetime.now() - timestamp

    # Convert the time difference to days, seconds, and microseconds
    days = time_difference.days
    seconds = time_difference.seconds
    microseconds = time_difference.microseconds

    # Determine the appropriate time format based on the time difference
    if days > 30:
        months = days // 30
        return f'Updated {months} month{"s" if months != 1 else ""} ago'
    elif days > 0:
        return f'Updated {days} day{"s" if days != 1 else ""} ago'
    elif seconds >= 3600:
        return f'Updated {seconds // 3600} hour{"s" if seconds // 3600 != 1 else ""} ago'
    elif seconds >= 60:
        return f'Updated {seconds // 60} minute{"s" if seconds // 60 != 1 else ""} ago'
    elif seconds > 0:
        return f'Updated {seconds} second{"s" if seconds != 1 else ""} ago'
    else:
        return 'just now'
