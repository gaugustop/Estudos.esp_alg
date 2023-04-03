import numpy as np

# def max_pairwise_product(numbers):
#     n = len(numbers)
#     max_product = 0
#     for i in range(n):
#         for second in range(i + 1, n):
#             max_product = max(max_product,
#                 numbers[i] * numbers[second])

#     return max_product

def max_pairwise_product2(numbers):
    numbers = np.array(numbers, dtype = 'int64')
    n = len(numbers)
    n1 = 0
    imax1 = 0
    for i in range(n):
        if numbers[i] > n1:
            imax1 = i
            n1 = numbers[i]
    n2 = 0
    for i in range(n):
        if numbers[i] > n2 and i != imax1:
            n2 = numbers[i]       
    return n1*n2

# def stress_test():
#     from numpy.random import randint as randint
#     nt = 1
#     while True:
#         print(f'teste número: = {nt}')
#         nt += 1
#         numbers = list(randint(1,10000000, 200,dtype = 'int64'))
#         p1 = max_pairwise_product(numbers)
#         p2 = max_pairwise_product2(numbers)
#         if p1 == p2:
#             print(f'max product = {p1}, Teste ok!')
#         else:
#             print('====== TESTE FALHOU!!! ======')
#             print(f'numeros = {numbers}')
#             print(f'p1 = {p1}, p2 = {p2}')
#             break


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product2(input_numbers))
    # stress_test()
