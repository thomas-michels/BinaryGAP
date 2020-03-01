
def solution(X, Y, D):

    if X == Y:
        return 0

    dist_plus = X // D

    saltos = (Y / D).__round__() - dist_plus

    return saltos


if __name__ == '__main__':
    print(solution(10, 85, 30))
