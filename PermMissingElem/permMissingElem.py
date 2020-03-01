
def solution(A):
    length = len(A)
    xor_sum = 0
    for i in range(0, length):
        sum_a = xor_sum ^ A[i]
        xor_sum = sum_a ^ (i + 1)
    return xor_sum^(length + 1)

if __name__ == '__main__':
    print(solution([1, 2, 5, 4]))