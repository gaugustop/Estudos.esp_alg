# def binary_search_wrapper(keys, query):
#     def binary_search(A, low, high, query):
#         if low > high:
#             return -1
#         middle = low + (high - low)//2        
#         while query == A[middle]:
#             if A[middle - 1] != query:
#                 return middle
#             middle -= 1
#         if query > A[middle]:
#             return binary_search(A, middle+1, high, query)
#         else:
#             return binary_search(A, low, middle-1, query)
#     return binary_search(keys, 0, len(keys)-1, query)

def binary_search_wrapper(keys, query):
    def binary_search(A, low, high, query):
        if low > high:
            return -1
        middle = low + (high - low) // 2
        if A[middle] == query:
            if middle == 0 or A[middle - 1] != query:
                return middle
            else:
                return binary_search(A, low, middle - 1, query)
        elif query < A[middle]:
            return binary_search(A, low, middle - 1, query)
        else:
            return binary_search(A, middle + 1, high, query)

    return binary_search(keys, 0, len(keys) - 1, query)

#lenta!
def busca_safada(lista,query):
    if query in lista:
        return lista.index(query) 
    else:
         return -1

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search_wrapper(input_keys, q), end=' ')
        # print(busca_safada(input_keys,q), end=' ')

