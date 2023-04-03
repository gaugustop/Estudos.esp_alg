def optimal_summands(n):
    summands = []
    resta = n
    s = 0
    i = 0
    while resta > 0:           
        i += 1
        summands.append(i)
        s += i
        resta -= i
        if resta in summands and resta != 0 :
           i += resta
           summands[-1] = i
           resta = 0
    return summands
#11
# i | s | resta
# 1 | 1 | 10
# 2 | 3 | 8
# 3 | 6 | 5
# 4 | 10 | 1

# 10 
#  i | s | resta
#  1 | 1 | 9
#  2 | 3 | 7
#  3 | 6 | 4
#  4 | 10 | 0   
import math

# Sn = (a1 + an)n / 2
# an = (a1 + (n-1)r)
# Sn = (2a1 + (n-1)r)n / 2 (a1 = 1, r = 1)
# Sn = (n + 1)n / 2
# fazendo Sn = k -> n = (sqrt(8k + 1) - 1) / 2

def max_prize(k):
    max_prizes = int((math.sqrt(8 * k + 1) - 1) / 2)
    prizes = list(range(1, max_prizes + 1))
    last_prize = sum(prizes)
    diff = k - last_prize
    if diff > 0:
        prizes[-1] += diff
    return prizes

if __name__ == '__main__':
    n = int(input())
    # summands = optimal_summands(n)
    summands = max_prize(n)
    print(len(summands))
    print(*summands)
