# def fibonacci_sum_squares(n):
#     if n <= 1:
#         return n

#     previous, current, sum = 0, 1, 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         sum += current * current

#     return sum % 10
def fibonacci_huge(n,m):
    array = [0] * (m * m + 1)
    array[1], p = 1, 2
    for i in range (2, m * m + 1):
        array[i] = (array[i-1] + array[i-2]) % m
        if array[i] == 1 and array [i-1] == 0:
            p = i-1
            break
    return array[n % p]

def fibonacci_sum_squares(n):
    return (fibonacci_huge(n+1,10)*fibonacci_huge(n,10)) % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
