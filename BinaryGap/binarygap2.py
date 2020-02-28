
def solution(N):
    binario_cru = bin(N)
    binario = binario_cru[2:]
    inicio_intervalo, cont, retorno_intervalo, tamanho_intervalo = 0, 0, 0, 0

    for i in binario:
        if int(i) == 1:
            inicio_intervalo = cont

            if retorno_intervalo < tamanho_intervalo:
                retorno_intervalo = tamanho_intervalo

            tamanho_intervalo = 0

        if int(i) == 0 and cont != inicio_intervalo:
            tamanho_intervalo += 1

        cont += 1

    return retorno_intervalo


if __name__ == '__main__':
    print(solution(561892))