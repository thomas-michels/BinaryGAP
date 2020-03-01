
def solution(X, Y, D):

    if X == Y:
        return 0

    saltos = 0
    sair = False
    while not sair:
        X += D
        saltos += 1
        if X >= Y:
            sair = True
            continue

    return saltos


if __name__ == '__main__':
    print(solution(1, 5, 2))
