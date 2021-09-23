import numpy as np
import itertools


def check_all_is_same(r):
    return np.max(r) == np.min(r)


def sum_rows(m):
    return np.sum(m, axis=1)


def sum_cols(m):
    return np.sum(m, axis=0)


def sum_diag(m):
    return np.trace(m)


def sum_anti_diag(m):
    a = np.fliplr(m)
    return np.trace(a)


def is_magic_square(m):
    sum = sum_rows(m)
    r = sum[0]
    check = check_all_is_same(sum)
    if not check:
        return False

    sum = sum_cols(m)
    c = sum[0]
    check = check_all_is_same(sum)
    if not check:
        return False

    d = sum_diag(m)

    a = sum_anti_diag(m)

    return r == c == d == a


# m = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
# print(is_magic_square(m))

source = '123456789'
numbers = list(source)

permutations = list(itertools.permutations(numbers))

# [
#   ('1', '2', '3', '4', '5', '6', '7', '8', '9'), 
#   ('1', '2', '3', '4', '5', '6', '7', '9', '8'), 
#   ('1', '2', '3', '4', '5', '6', '8', '7', '9'), 
#   ('1', '2', '3', '4', '5', '6', '8', '9', '7')
# ]
# print(permutations[:4])

for permutation in permutations:
    if(is_magic_square(np.array([int(char) for char in permutation]).reshape(3, 3))):
        print(permutation)

# ('2', '7', '6', '9', '5', '1', '4', '3', '8')
# ('2', '9', '4', '7', '5', '3', '6', '1', '8')
# ('4', '3', '8', '9', '5', '1', '2', '7', '6')
# ('4', '9', '2', '3', '5', '7', '8', '1', '6')
# ('6', '1', '8', '7', '5', '3', '2', '9', '4')
# ('6', '7', '2', '1', '5', '9', '8', '3', '4')
# ('8', '1', '6', '3', '5', '7', '4', '9', '2')
# ('8', '3', '4', '1', '5', '9', '6', '7', '2')
