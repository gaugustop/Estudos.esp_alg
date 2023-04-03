from sys import stdin
import numpy as np
def maximum_gold(capacity, weights):
    weights.insert(0, 0)
    
    # subproblems:
    # valor atual = max(usa ith item, não usa ith item)
    # value(w, i) = max(value(w-wi, i-1) + vi, value(w, i-1))
    
    value = weights
    matrizPD = np.zeros((len(weights), capacity+1)) # correct initialization
    
    for i in range(1, len(weights)):
        for j in range(1, capacity+1):
            matrizPD[i,j] = matrizPD[i-1,j]
            if weights[i] <= j: # use i-th item if possible
                val = matrizPD[i-1,j-weights[i]] + value[i]
                matrizPD[i,j] = max(matrizPD[i,j], val)
    
    return int(matrizPD[-1,-1]) # convert the result to int (gold weight)


if __name__ == '__main__':
    # input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    input_capacity, n, *input_weights = list(map(int, input().split()))

    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
