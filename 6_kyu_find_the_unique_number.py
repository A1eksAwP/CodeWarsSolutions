# https://www.codewars.com/kata/585d7d5adb20cf33cb000235

def find_uniq(arr):
    """
    There is an array with some numbers.
    All numbers are equal except for one. Try to find it!
    find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
    find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
    It’s guaranteed that array contains at least 3 numbers.
    The tests contain some very huge arrays, so think about performance.
    :param arr:
    :return: el
    """
    for el in set(arr):
        if el == arr[1] and el == arr[0]:
            continue
        return el
