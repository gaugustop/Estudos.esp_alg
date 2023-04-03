from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest

# def largest_number(numbers):
#     numbers = list(map(int, numbers))
#     largest = ""
#     numbers.sort()
#     for _ in range(0,len(numbers)):
#         largest_digit = numbers.pop(-1)
#         largest += str(largest_digit)
#     return int(largest)

def largest_number(numbers):
    numbers = [str(x) for x in numbers]  # convert all numbers to strings
    numbers.sort(key=lambda x: x*3, reverse=True)  # sort in non-increasing order
    return int(''.join(numbers))

if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    # print(type(input_numbers[0]))
    # print(largest_number_naive(input_numbers))
    print(largest_number(input_numbers))
    # assert(largest_number_naive(input_numbers) == largest_number(input_numbers))
