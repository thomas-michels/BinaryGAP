
def solution(A):
    length = len(A)
    menor_diferenca = 100000

    for i in range(1, length):
        diferenca = sum(A[i:]) - sum(A[:i])
        if diferenca < 0:
            diferenca *= -1

        if diferenca < menor_diferenca:
            menor_diferenca = diferenca

        if menor_diferenca == 1:
            break

    return menor_diferenca


if __name__ == '__main__':
    print(solution([3, 1, 2, 4, 3]))