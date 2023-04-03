# def lcm(a, b):
#     for l in range(1, a * b + 1):
#         if l % a == 0 and l % b == 0:
#             return l

#     assert False
def euclid_gcd(a,b):
    if b == 0:
        return a
    else:
        a2 = a % b
        return euclid_gcd(b,a2)

def lcm2(a, b):
    return a*b // euclid_gcd(a,b)


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm2(a, b))

