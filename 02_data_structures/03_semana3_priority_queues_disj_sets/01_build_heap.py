# python3

#zero index:
#    0
#  1   2
# 3 4 5 6


# pseudocode from lecture
#adaptado para zero indexing
# def shiftDown(H,i,size,swaps):
#     maxIndex = i
#     l = leftChild(i)
#     if l <= size and H[l] < H[maxIndex]:  #sinal > trocado por < pois queremos o min-heap
#         maxIndex = l
#     r = rightChild(i)
#     if r <= size and H[r] < H[maxIndex]:  #sinal > trocado por < pois queremos o min-heap
#         maxIndex = r
#     if i != maxIndex:
#         H[i], H[maxIndex] = H[maxIndex], H[i]
#         swaps.append([i,maxIndex])
#         shiftDown(maxIndex)
def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps

def parent(i):
    return (i-1)//2
def leftChild(i):
    return 2*i + 1
def rightChild(i):
    return 2*i + 2

def shiftUp(H,i,swaps):
    while i > 0 and H[parent(i)] > H[i]: #sinal < trocado por > pois queremos o min-heap
        H[parent(i)], H[i] = H[i], H[parent(i)]
        swaps.append([parent(i),i])
        i = parent(i)

def build_heap_efficient(data):
    swaps = list()
    for i in range(len(data)-1,-1,-1):
        shiftUp(data,i,swaps)
    return swaps

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap_efficient(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
