
def solution(A):

    numero = 0
    for i in A:
        numero ^= i

    return numero


if __name__ == '__main__':
    print(solution([9, 3, 9, 3, 9, 7, 9]))
