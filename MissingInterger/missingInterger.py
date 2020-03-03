
def solution(A):
    A.sort()
    anterior = 0
    for i in A:
        if (anterior + 1) == i or i == anterior:
            anterior = i

        else:
            return anterior + 1

    return A[-1] + 1


if __name__ == '__main__':
    print(solution([1, 3, 6, 4, 1, 2]))