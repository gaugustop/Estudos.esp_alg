# def fibonacci_sum(n):
#     if n <= 1:
#         return n

#     previous, current, _sum = 0, 1, 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         _sum += current

#     return _sum % 10
def fibonacci_huge(n,m):
    array = [0] * (m * m + 1)
    array[1], p = 1, 2
    for i in range (2, m * m + 1):
        array[i] = (array[i-1] + array[i-2]) % m
        if array[i] == 1 and array [i-1] == 0:
            p = i-1
            break
    return array[n % p]

def fibonacci_sum(n):
    Sn =  fibonacci_huge(n + 2,10) - 1
    return Sn % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
