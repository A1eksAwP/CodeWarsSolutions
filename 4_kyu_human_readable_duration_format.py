# https://www.codewars.com/kata/52742f58faf5485cae000b9a/

def format_duration(seconds):
    """
    Note that spaces are important.
    Detailed rules
    The resulting expression is made of components like 4 seconds,
    1 year, etc. In general, a positive integer and one of the valid units of time,
    separated by a space. The unit of time is used in plural if the integer is greater than 1.
    The components are separated by a comma and a space (", "). Except the last component,
    which is separated by " and ", just like it would be written in English.
    A more significant units of time will occur before than a least significant one.
    Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.
    Different components have different unit of times. So there is not repeated
    units like in 5 seconds and 1 second.
    A component will not appear at all if its value happens to be zero.
    Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.
    A unit of time must be used "as much as possible".
    It means that the function should not return 61 seconds, but 1 minute and 1 second instead.
    Formally, the duration specified by of a component must not be greater
    than any valid more significant unit of time.
    :param seconds:
    :return:
    """
    dur_sec = seconds % 60 if seconds >= 60 else seconds
    dur_min = seconds // 60 % 60 if seconds // 60 >= 60 else seconds // 60
    dur_hour = seconds // 3600 % 24 if seconds // 3600 >= 24 else seconds // 3600
    dur_day = seconds // 86400 % 365 if seconds // 86400 >= 365 else seconds // 86400
    dur_year = seconds // 31536000
    result = []
    if dur_year:
        result.append(f'{dur_year} years') if dur_year > 1 else result.append(f'{dur_year} year')
    if dur_day:
        result.append(f'{dur_day} days') if dur_day > 1 else result.append(f'{dur_day} day')
    if dur_hour:
        result.append(f'{dur_hour} hours') if dur_hour > 1 else result.append(f'{dur_hour} hour')
    if dur_min:
        result.append(f'{dur_min} minutes') if dur_min > 1 else result.append(f'{dur_min} minute')
    if dur_sec:
        result.append(f'{dur_sec} seconds') if dur_sec > 1 else result.append(f'{dur_sec} second')
    match len(result):
        case 0: return 'now'
        case 1: return ''.join(result)
        case 2: return ' and '.join(result)
        case _: return f"{', '.join(result[:-1])} and {''.join(result[-1:])}"


print(format_duration(1))  # "1 second"
print(format_duration(62))  # "1 minute and 2 seconds"
print(format_duration(120))  # "2 minutes"
print(format_duration(3600))  # "1 hour"
print(format_duration(365641262))  # "11 years, 216 days, 23 hours, 1 minute and 2 seconds"
