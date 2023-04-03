def binary_search(keys, query):
    def binary_search_aux(A, low, high, query):
        if low > high:
            return -1
        middle = low + (high - low)//2
        if A[middle] == query:
            return middle
        elif A[middle] < query:
            return binary_search_aux(A, middle+1, high, query)
        else:
            return binary_search_aux(A, low, middle-1, query)

    return binary_search_aux(keys, 0, len(keys)-1, query)

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')