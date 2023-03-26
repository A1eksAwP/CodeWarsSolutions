# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39
# This time we want to write calculations using functions and get the results.
# Let's have a look at some examples:
#
# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:
#
# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))

def calc(by, num):
    match num[0]:
        case '-': return int(by - num[1])
        case '+': return int(by + num[1])
        case '*': return int(by * num[1])
        case '/': return int(by / num[1])


def zero(num=None): return calc(0, num) if num else 0
def one(num=None): return calc(1, num) if num else 1
def two(num=None): return calc(2, num) if num else 2
def three(num=None): return calc(3, num) if num else 3
def four(num=None): return calc(4, num) if num else 4
def five(num=None): return calc(5, num) if num else 5
def six(num=None): return calc(6, num) if num else 6
def seven(num=None): return calc(7, num) if num else 7
def eight(num=None): return calc(8, num) if num else 8
def nine(num=None): return calc(9, num) if num else 9
def plus(num): return '+', num
def minus(num): return '-', num
def times(num): return '*', num
def divided_by(num): return '/', num
