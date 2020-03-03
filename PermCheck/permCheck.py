
def solution(A):
    A.sort()
    anterior = 0
    for i in A:
        if (anterior + 1) == i:
            anterior = i

        else:
            return 0

    return 1


if __name__ == '__main__':
    print(solution([4, 1, 2]))