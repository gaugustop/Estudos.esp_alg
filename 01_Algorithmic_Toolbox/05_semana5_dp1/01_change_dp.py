import numpy as np
def change(money, coins):
    MinNumCoins = [0] + [np.inf] * (money)
    for m in range(1,money+1):
        for c in coins:
            if m >= c:
                NumCoins = MinNumCoins[m-c] + 1
            if NumCoins < MinNumCoins[m]:
                MinNumCoins[m] = NumCoins
    return MinNumCoins[money]


if __name__ == '__main__':
    m = int(input())
    print(change(m,[1,3,4]))
