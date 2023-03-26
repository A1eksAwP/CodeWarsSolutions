# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

def move_zeros(lst):
    """
    Write an algorithm that takes an array and moves all of the zeros
    to the end, preserving the order of the other elements.
    move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
    :param lst:
    :return:
    """
    result = []
    lazy_arr = []
    for el in lst:
        if el != 0:
            result.append(el)
        else:
            lazy_arr.append(el)
    result += lazy_arr
    return result


# красивее, но медленнее O(n^2)
def move_zeros_v2(lst):
    return [x for x in lst if x] + [0] * lst.count(0)
