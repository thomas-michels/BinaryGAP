
def solution(X, Y, D):

    if X == Y:
        return 0

    pulos_real = (X - Y) // D

    if pulos_real < 0:
        pulos_real *= -1

    return pulos_real.__round__()


if __name__ == '__main__':
    print(solution(10, 85, 30))
    print(solution(2, 11, 3))
