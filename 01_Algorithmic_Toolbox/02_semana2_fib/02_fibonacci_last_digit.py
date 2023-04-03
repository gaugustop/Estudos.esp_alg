def fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def fibonacci_number(n):
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

def fibonacci_last_digit2(n):    
    return fibonacci_number(n) % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit2(n))
