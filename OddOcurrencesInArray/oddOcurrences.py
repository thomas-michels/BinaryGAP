def solution(A):
    posicoes_iguais = []

    for i in A:
        pos_iguais = []
        for j in A:
            if i == j:
                pos_iguais.append(j)

        if not pos_iguais in posicoes_iguais:
            posicoes_iguais.append(pos_iguais)

    nao_emparelhado = 0
    for i in posicoes_iguais:
        if len(i) == 1:
            nao_emparelhado = i[0]

    return nao_emparelhado

if __name__ == '__main__':
    print(solution([9, 3, 9, 3, 9, 7, 9]))