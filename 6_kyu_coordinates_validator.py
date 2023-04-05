# https://www.codewars.com/kata/5269452810342858ec000951

"""
Latitude (which is first float) can be between 0 and 90, positive or negative. Longitude (which is second float) can be between 0 and 180, positive or negative.

Coordinates can only contain digits, or one of the following symbols (including space after comma) __ -, . __

There should be no space between the minus "-" sign and the digit after it.

Here are some valid coordinates:

-23, 25
24.53525235, 23.45235
04, -23.234235
43.91343345, 143
4, -3
And some invalid ones:

23.234, - 23.4234
2342.43536, 34.324236
N23.43345, E32.6457
99.234, 12.324
6.325624, 43.34345.345
0, 1,2
0.342q0832, 1.2324
"""
import re


def is_valid_coordinates(x):
    result = re.fullmatch(r'-?\d+\.?\d*,\s-?\d+\.?\d*', x)
    lat, lon = result.group().split(',') if result else [500, 500]
    return -90 <= float(lat) <= 90 and -180 <= float(lon) <= 180
