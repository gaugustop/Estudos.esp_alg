import numpy as np
def edit_distance(A,B):
    A, B = ' ' + A, ' ' + B
    n1, n2 = len(A), len(B)
    D = np.array([[0] * n2] * n1)
    for i in range(0,n1):
        D[i][0] = i
    for j in range(0,n2):
        D[0][j] = j
    for i in range(1,n1):
        for j in range(1,n2):
            insertion = D[i,j-1] + 1
            deletion  = D[i-1,j] + 1
            match_mismatch     = D[i-1,j-1] + (A[i] != B[j])
            D[i,j] = min(insertion, deletion, match_mismatch)            
    return D[n1-1,n2-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
