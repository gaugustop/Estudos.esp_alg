def change(money):
    money_left = money
    n_change = 0
    for c in [10, 5, 1]:
        n_c, money_left = divmod(money_left,c)
        n_change += n_c 
    return n_change

if __name__ == '__main__':
    m = int(input())
    print(change(m))
