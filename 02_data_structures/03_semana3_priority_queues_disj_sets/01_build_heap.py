# python3

#zero index:
#    0
#  1   2
# 3 4 5 6


# def build_heap(data):
#     """Build a heap from ``data`` inplace.

#     Returns a sequence of swaps performed by the algorithm.
#     """
#     # The following naive implementation just sorts the given sequence
#     # using selection sort algorithm and saves the resulting sequence
#     # of swaps. This turns the given array into a heap, but in the worst
#     # case gives a quadratic number of swaps.
#     #
#     # TODO: replace by a more efficient implementation
#     swaps = []
#     for i in range(len(data)):
#         for j in range(i + 1, len(data)):
#             if data[i] > data[j]:
#                 swaps.append((i, j))
#                 data[i], data[j] = data[j], data[i]
#     return swaps

def parent(i):
    return (i-1)//2
def leftChild(i):
    return 2*i + 1
def rightChild(i):
    return 2*i + 2

def shiftDown(H,i,size,swaps):
    minIndex = i
    l = leftChild(i)
    print(i)
    if l <= size and H[l] < H[minIndex]:  #sinal > trocado por < pois queremos o min-heap
        minIndex = l
    r = rightChild(i)
    if r <= size and H[r] < H[minIndex]:  #sinal > trocado por < pois queremos o min-heap
        minIndex = r
    if i != minIndex:
        H[i], H[minIndex] = H[minIndex], H[i]
        swaps.append([i,minIndex])
        shiftDown(minIndex)

def shiftUp(H,i,swaps):
    while i > 0 and H[parent(i)] > H[i]: #sinal < trocado por > pois queremos o min-heap
        H[parent(i)], H[i] = H[i], H[parent(i)]
        swaps.append([parent(i),i])
        i = parent(i)

def build_heap_efficient(data):
    swaps = list()
    for i in range((len(data)-1) // 2,-1,-1):
        shiftDown(data,i,len(data),swaps)
    return swaps

def build_heap2(data):
    swaps = list()
    left = lambda i: 2*i+1
    right = lambda i:2*i+2
    n = len(data)
    for j in range ((n-1)//2, -1, -1):
        i = j 
        min_index = i
        while True:
            if left(i) < n and data[left(i)] < data[min_index]:
                min_index = left(i)
            if right(i) < n and data[right(i)] < data[min_index]:
                min_index = right(i)
            if i == min_index:
                break
            data[i], data[min_index] = data[min_index], data[i]
            swaps.append((i, min_index))
            i = min_index
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap2(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
