
def solution(X, Y, D):

    if X == Y:
        return 0

    if Y < 100:
        saltos = 0
        sair = False
        while not sair:
            X += D
            saltos += 1
            if X >= Y:
                sair = True
                continue


        return saltos

    dist_plus = X // D
    dist_padrao = (Y / D).__round__()
    saltos = dist_padrao - dist_plus

    return saltos


if __name__ == '__main__':
    print(solution(10, 85, 30))
    print(solution(2, 11, 3))
