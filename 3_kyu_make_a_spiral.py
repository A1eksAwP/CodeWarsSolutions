# https://www.codewars.com/kata/534e01fbbb17187c7e0000c6/

def display_spiral(lines: list):
    [print(line) for line in lines]


def spiralize(size):
    """
    Your task, is to create a NxN spiral with a given size.

    For example, spiral with size 5 should look like this:

    00000
    ....0
    000.0
    0...0
    00000
    and with the size 10:

    0000000000
    .........0
    00000000.0
    0......0.0
    0.0000.0.0
    0.0..0.0.0
    0.0....0.0
    0.000000.0
    0........0
    0000000000
    Return value should contain array of arrays, of 0 and 1, with the first
    row being composed of 1s. For example for given size 5 result should be:

    [[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
    Because of the edge-cases for tiny spirals, the size will be at least 5.

    General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself.
    :param size:
    :return:
    """
    field = [[0 for _ in range(size)] for _ in range(size)]
    i = 0
    j = 0
    x = 0
    future_i = 0
    future_j = 1
    step = ['right', 'down', 'left', 'up']
    turn_dict = {'right': j + 1, 'down': i + 1, 'left': j - 1, 'up': i - 1}
    fail_count = 0
    while fail_count < 2:
        if field[future_i][future_j] != 1:
            field[i][j] = 1
            fail_count = 0
        else:
            i = i - turn_dict[step[x]] if x == 1 or x == 3 else i
            j = j - turn_dict[step[x]] if x == 0 or x == 2 else j
            x = 0 if x == len(step) - 1 else x + 1
            fail_count += 1
        next_i = i + turn_dict[step[x]] if x == 1 or x == 3 else i
        next_j = j + turn_dict[step[x]] if x == 0 or x == 2 else j
        if next_i < 0 or next_i >= len(field) or next_j < 0 or next_j >= len(field):
            x = 0 if x == len(step) - 1 else x + 1
            i = i + turn_dict[step[x]] if x == 1 or x == 3 else i
            j = j + turn_dict[step[x]] if x == 0 or x == 2 else j
        else:
            i = next_i
            j = next_j
        if fail_count:
            temp_x = x
            x = 0 if x == len(step) - 1 else x + 1
            future_i = i + turn_dict[step[x]] if x == 1 or x == 3 else i
            future_j = j + turn_dict[step[x]] if x == 0 or x == 2 else j
            if field[future_i][future_j] == 1:
                fail_count += 1
            x = temp_x
        future_i = i + turn_dict[step[x]] if x == 1 or x == 3 else i
        future_j = j + turn_dict[step[x]] if x == 0 or x == 2 else j
        if future_i < 0 or future_i >= len(field) or future_j < 0 or future_j >= len(field):
            future_i = next_i
            future_j = next_j
    return field


display_spiral(spiralize(50))
