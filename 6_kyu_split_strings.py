# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001

def solution(s):
    """
    Complete the solution so that it splits the string into pairs of two characters.
    If the string contains an odd number of characters then it should replace the
    missing second character of the final pair with an underscore ('_').
    Examples:
    * 'abc' =>  ['ab', 'c_']
    * 'abcdef' => ['ab', 'cd', 'ef']
    :param s:
    :return: split(list)
    """
    s += '_' if len(s) % 2 != 0 else ''
    return [s[i:i + 2] for i in range(len(s)) if i % 2 == 0]
