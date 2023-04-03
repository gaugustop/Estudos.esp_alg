from sys import stdin
import numpy as np

def partition3(values):
    if sum(values) % 3 != 0:
        return 0
    target = sum(values) // 3
    array = np.zeros((target+1,target+1), dtype=bool)
    array[0][0] = 1
    n = len(values)
    for i in range(n):
        for j in range(target,-1,-1):
            for k in range(target,-1,-1):
                if array[j][k] == 0:
                    value = j - values[i]
                    if value >= 0:
                        array[j][k] = array[value][k]
                if array[j][k] == 0:
                    value = j - values[i]
                    if value >= 0:
                        array[j][k] = array[j][value]
    return array[target][target]


# if __name__ == '__main__':
#     input_n, *input_values = list(map(int, stdin.read().split()))
#     # print(input_n)
#     assert input_n == len(input_values)
#     print(int(partition3(input_values)))

# import numpy as np

# def partition3(values):
#     if sum(values) % 3 != 0:
#         return 0
#     target = sum(values) // 3
#     array = np.zeros((target+1, target+1, len(values)+1), dtype=bool)
#     array[0][0][0] = True
#     for i in range(len(values)):
#         for j in range(target+1):
#             for k in range(target+1):
#                 array[j][k][i+1] = array[j][k][i]
#                 if j >= values[i]:
#                     array[j][k][i+1] |= array[j-values[i]][k][i]
#                 if k >= values[i]:
#                     array[j][k][i+1] |= array[j][k-values[i]][i]
#     return array[target][target][len(values)]


if __name__ == '__main__':
    input_n, *values = list(map(int, stdin.read().split()))
    # n = int(input())
    # values = list(map(int, input().split()))
    print(int(partition3(values)))