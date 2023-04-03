def majority_element_naive(elements):
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0

def majority_element(elements):
    count = {}
    threshold = len(elements) / 2
    for e in elements:
        if e in count:
            count[e] += 1
        else:
            count[e] = 1
        if count[e] > threshold:
            return 1
    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))