from itertools import combinations

# def inversions_naive(a):
#     number_of_inversions = 0
#     for i, j in combinations(range(len(a)), 2):
#         if a[i] > a[j]:
#             number_of_inversions += 1
#     return number_of_inversions

# def merge_sort(array):
#     if len(array) <= 1:
#         return array

#     middle = len(array) // 2
#     left = merge_sort(array[:middle])
#     right = merge_sort(array[middle:])
#     return merge(left, right)

# def merge(left, right):
#     result = []
#     i, j = 0, 0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result += left[i:]
#     result += right[j:]
#     return result

# def inversions_merge_sort(a):
#     def merge(left, right):
#         result = []
#         i = j = inversions = 0
#         while i < len(left) and j < len(right):
#             if left[i] <= right[j]:
#                 result.append(left[i])
#                 i += 1
#             else:
#                 result.append(right[j])
#                 j += 1
#                 inversions += len(left) - i
#         result += left[i:]
#         result += right[j:]
#         return result, inversions

#     if len(a) <= 1:
#         return a, 0

#     middle = len(a) // 2
#     left, left_inversions = inversions_merge_sort(a[:middle])
#     right, right_inversions = inversions_merge_sort(a[middle:])
#     merged, merge_inversions = merge(left, right)
#     total_inversions = left_inversions + right_inversions + merge_inversions
#     return total_inversions

def calculate_inversions(array, left, right):
    if left == right:
        return 0
    mid = (left + right) // 2
    num_inv = calculate_inversions(array, left, mid)
    num_inv += calculate_inversions(array, mid + 1, right)
    aux = []
    i,j,k = left, mid+1, 0
    while i <= mid or j <= right:
        if i > mid or (j <= right and array[i] > array[j]):
            aux.append(array[j])
            j += 1
            num_inv += mid - i + 1
        else:
            aux.append(array[i])
            i += 1
    array[left:right + 1] = aux
    return num_inv


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(calculate_inversions(elements))
