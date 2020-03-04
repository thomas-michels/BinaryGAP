
def solution(A):
    A.sort()
    anterior = 0
    for i in A:
        if i < 0:
            i *= -1

        if (anterior + 1) == i:
            anterior = i

        elif anterior == i:
            continue

        else:
            return anterior + 1

    if len(A) < 2:
        if (A[0] + 1) < 1:
            return 1

        else:
            return A[0] + 1

    return A[-1] + 1


if __name__ == '__main__':
    print(solution([-1]))
