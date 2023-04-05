import numpy as np

def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


# def maximum_value(num, op):
#     n, inf = len(num), 9**9
#     my_min = [[0] * n for _ in range(n)]
#     my_max = [[0] * n for _ in range(n)]
#     for i in range(n):
#         my_min[i][i] = my_max[i][i] = int(num[i])
#     for size in range(1,n):
#         for i in range(n-size):
#             j = i+size
#             my_min[i][j], my_max[i][j] = inf, -inf
#             for k in range(i,j):
#                 value = evaluate(my_min[i][k], my_min[k+1][j], op[k])
#                 my_min[i][j] = min(value, my_min[i][j])
#                 my_max[i][j] = max(value, my_max[i][j])
#                 value = evaluate(my_min[i][k], my_min[k+1][j], op[k])
#                 my_min[i][j] = min(value, my_min[i][j])
#                 my_max[i][j] = max(value, my_max[i][j])
#                 value = evaluate(my_min[i][k], my_min[k+1][j], op[k])
#                 my_min[i][j] = min(value, my_min[i][j])
#                 my_max[i][j] = max(value, my_max[i][j])
#                 value = evaluate(my_min[i][k], my_min[k+1][j], op[k])
#                 my_min[i][j] = min(value, my_min[i][j])
#                 my_max[i][j] = max(value, my_max[i][j])
#     return my_max[0][n-1]

def maximum_value(num, op):
    n, inf = len(num), 9 ** 9
    my_min = [[0] * n for _ in range(n)]
    my_max = [[0] * n for _ in range(n)]
    for i in range(n):
        my_min[i][i] = my_max[i][i] = int(num[i])
    for size in range(1, n):
        for i in range(n - size):
            j = i + size
            my_min[i][j], my_max[i][j] = inf, -inf
            value = evaluate(my_min[i][0], my_min[0 + 1][j], op[0])
            for k in range(i, j):
                temp = evaluate(my_min[i][k], my_min[k + 1][j], op[k])
                value = min(value, temp)
                my_min[i][j] = min(my_min[i][j], temp, evaluate(my_min[i][k], my_max[k + 1][j], op[k]), evaluate(my_max[i][k], my_min[k + 1][j], op[k]))
                my_max[i][j] = max(my_max[i][j], temp, evaluate(my_min[i][k], my_max[k + 1][j], op[k]), evaluate(my_max[i][k], my_min[k + 1][j], op[k]))
    return my_max[0][n - 1]


if __name__ == "__main__":
    string = input()
    numbers, operations = list(), list()
    numbers = string[0:len(string):2]
    operations = string[1:len(string)-1:2]
    print(int(maximum_value(numbers,operations)))
