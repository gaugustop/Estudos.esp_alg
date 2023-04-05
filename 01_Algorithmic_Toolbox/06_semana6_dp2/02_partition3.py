def partition3(values, n):
    if sum(values) % 3 != 0:
        return 0
    target = sum(values) // 3
    array = [[0] * (target+1) for _ in range(target+1)]
    array[0][0] = 1
    for i in range(n):
        for j in range(target, -1, -1):
            for k in range(target, -1, -1):
                if array[j][k] == 0:
                    value = j - values[i]
                    if value >= 0:
                        array[j][k] = array[value][k]
                if array[j][k] == 0:
                    value = k - values[i]
                    if value >= 0:
                        array[j][k] = array[j][value]
    return array[target][target]

if __name__ == "__main__":
    n = int(input())
    values = list(map(int, input().split()))
    print (partition3(values, n))