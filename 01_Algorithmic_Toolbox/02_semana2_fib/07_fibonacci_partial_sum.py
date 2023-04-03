# Uses python3
import sys

# def fibonacci_partial_sum_naive(from_, to):
#     _sum = 0

#     current = 0
#     _next  = 1

#     for i in range(to + 1):
#         if i >= from_:
#             _sum += current

#         current, _next = _next, current + _next

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

def fibonacci_partial_sum(m,n):
    _sum_m_first = (fibonacci_huge(m+2,10) - 1) % 10
    _sum_n_first = (fibonacci_huge(n+2,10) - 1) % 10
    partial_sum  = (_sum_n_first - _sum_m_first) % 10
    return partial_sum

if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))
