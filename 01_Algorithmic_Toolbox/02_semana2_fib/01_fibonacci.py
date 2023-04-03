# naive solution
# def fibonacci_number(n):
#     if n <= 1:
#         return n

#     return fibonacci_number(n - 1) + fibonacci_number(n - 2)

def fibonacci_number(n):
    if n <= 1:
        return n
    list_fib = list(range(n+1))
    list_fib[0] = 0
    list_fib[1] = 1
    for i in range(2,n+1):
        list_fib[i] = list_fib[i-1] + list_fib[i-2]
    return list_fib[n]

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
