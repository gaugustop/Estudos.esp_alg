def compute_operations(n):
    num_operations = [0] * (n+1)
    previous = [0] * (n+1)
    num_operations[1] = 0
    for i in range(2,n+1):
        num_operations[i] = num_operations[i-1] + 1
        previous[i]       = i - 1
        if i % 2 == 0 and num_operations[i] > num_operations[i // 2] + 1:
            num_operations[i] = num_operations[i // 2] + 1
            previous[i]       = i // 2
        if i % 3 == 0 and num_operations[i] > num_operations[i // 3] + 1:
            num_operations[i] = num_operations[i // 3] + 1
            previous[i]       = i // 3
    sequence = [n]
    while n != 1:
        sequence += [previous[n]]
        n = previous[n]
    sequence.reverse()
    return sequence


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
