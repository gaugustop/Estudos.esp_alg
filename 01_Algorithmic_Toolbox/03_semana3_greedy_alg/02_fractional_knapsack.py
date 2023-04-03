from sys import stdin
#while knapsack is not full
#choose item i with maximum vi/wi
#if item fits into knapsack, take all of it
#otherwise take so much as to fill the knapsack
#return total valua and amounts taken
def best_item(weights, values):
    maxValuePerWeight = 0
    bestItem = 0
    for i in range(0,len(values)):
        if weights[i] > 0:
            if values[i]/weights[i] > maxValuePerWeight:
                maxValuePerWeight = values[i]/weights[i]
                bestItem = i
    return bestItem

def optimal_value(capacity, weights, values):
    value = 0.
    W = capacity
    for i in range(0,len(values)):
        if W == 0:
            return value
        bestItem = best_item(weights,values)
        w = weights.pop(bestItem)
        v = values.pop(bestItem)
        a = min(w,W)
        value += a * (v/w)
        W -= a
    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    # print(data)
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    # print(n)
    # print(capacity)
    # print(values)
    # print(weights)
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
