def fibonacci_matrix(n):
    if n <= 1:
        return n

    # define a matriz de Fibonacci
    fib_matrix = [[1, 1], [1, 0]]

    # eleva a matriz à potência n usando a técnica de exponenciação rápida
    def matrix_power(matrix, power):
        result = [[1, 0], [0, 1]]
        while power > 0:
            if power % 2 == 1:
                result = matrix_multiply(result, matrix)
            matrix = matrix_multiply(matrix, matrix)
            power //= 2
        return result

    # multiplica duas matrizes 2x2
    def matrix_multiply(a, b):
        return [[a[0][0]*b[0][0] + a[0][1]*b[1][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]],
                [a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1]]]

    # retorna o n-ésimo número da sequência de Fibonacci
    return matrix_power(fib_matrix, n-1)[0][0]


def fibonacci_huge(n,m):
    array = [0] * (m * m + 1)
    array[1], p = 1, 2
    for i in range (2, m * m + 1):
        array[i] = (array[i-1] + array[i-2]) % m
        if array[i] == 1 and array [i-1] == 0:
            p = i-1
            break
    return array[n % p]


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge(n, m))
