# https://www.codewars.com/kata/52a382ee44408cea2500074c/

def determinant(matrix):
    """
    |a  b|
    |c  d|
    has determinant: a*d - b*c.

    The determinant of an n x n sized matrix is calculated by
    reducing the problem to the calculation of the determinants
    of n matrices ofn-1 x n-1 size.

    For the 3x3 case, [ [a, b, c], [d, e, f], [g, h, i] ] or

    |a b c|
    |d e f|
    |g h i|
    the determinant is: a * det(a_minor) - b * det(b_minor) + c * det(c_minor)
    where det(a_minor) refers to taking the determinant of the 2x2
    matrix created by crossing out the row and column in which the element a occurs:

    |- - -|
    |- e f|
    |- h i|
    Note the alternation of signs.

    The determinant of larger matrices are calculated analogously,
    e.g. if M is a 4x4 matrix with first row [a, b, c, d], then:

    det(M) = a * det(a_minor) - b * det(b_minor) + c * det(c_minor) - d * det(d_minor)
    :param matrix:
    :return:
    """
    result = 0
    L = len(matrix)
    if L == 1:
        result = matrix[0][0]
    if L == 2:
        result = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if L > 2:
        r_matrix = [matrix[i][::-1] for i in range(L)]
        for k in range(L):
            j = 0 + k
            i = 0
            p_prev = 0
            n_prev = 0
            for _ in range(L):
                pos_find = matrix[i][j]
                p_prev = p_prev * pos_find if p_prev else p_prev + pos_find
                neg_find = r_matrix[i][j]
                n_prev = n_prev * neg_find if n_prev else n_prev + neg_find
                j += 1
                j = 0 if j >= L else j
                i += 1
                i = 0 if i >= L else i
            result += p_prev - n_prev
    return result


m0 = [[5]]
m1 = [[4, 6], [3, 8]]
m5 = [[2, 4, 2], [3, 1, 1], [1, 2, 0]]
print(determinant(m1))


# # Это читерство, но всё же
import numpy as np


def determinant(matrix):
    return round(np.linalg.det(matrix))
