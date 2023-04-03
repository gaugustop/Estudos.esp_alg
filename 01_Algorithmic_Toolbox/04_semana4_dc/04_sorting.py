from random import randint
def partition3(array, left, right):
    # write your code here
    # l  <= k <= m1-1, A[k] < x
    # m1 <= k <= m2,   A[k] = x
    # m2+1 <= k <= r, A[k] > x
    x = array[left] #pivot
    m1 = left
    m2 = left
    for i in range(left+1, right+1):
        if array[i] < x:
            m1 += 1
            m2 += 1
            array[i], array[m1] = array[m1], array[i]
            if m1 != m2:
                array[i], array[m2] = array[m2], array[i]
        elif array[i] == x:
            m2 += 1
            array[i], array[m2] = array[m2], array[i]
    array[left], array[m1] = array[m1], array[left]
    return m1,m2    

def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)

#possiveis outros passos: 
#   eliminar as recursões
#   intro sort, adicionar heuristica para escolha do pivot

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)