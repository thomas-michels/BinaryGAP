
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

    for i in numeros:
        if i['ocorrencias'] == 1:
            numero_so = i['numero']

    return numero_so


if __name__ == '__main__':
    print(solution([9, 3, 9, 3, 9, 7, 9]))