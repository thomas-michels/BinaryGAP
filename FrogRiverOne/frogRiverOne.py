
def solution(X, A):
    seta = set()
    for indice, valorIndice in enumerate(A):
        seta.add(valorIndice)
        if len(seta) == X:
            return indice

    return -1


if __name__ == '__main__':
    print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))
