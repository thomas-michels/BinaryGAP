
def solution(A):

    numeros = []
    for i in A:
        dic = {
            'numero': i,
            'ocorrencias': 1
        }

        if dic not in numeros:
            numeros.append(dic)

        else:
            numeros[numeros.index(dic)]['ocorrencias'] += 1

    numero = [i for i, val in enumerate(numeros) if val['ocorrencias'] == 1]
    print(numeros)
    return numeros[numero[0]]['numero']


if __name__ == '__main__':
    print(solution([9, 3, 9, 3, 9, 7, 9]))