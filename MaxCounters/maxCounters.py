def solution(N , A):
    retorno = [0] * N
    max_counter = 0
    max_current = 0

    for i in A:
        if 1 <= i <= N:
            if max_counter > retorno[i -1]:
                retorno[i - 1] = max_counter

            retorno[i - 1] += 1
            if max_current < retorno[i - 1]:
                max_current = retorno[i -1]

        else:
            max_counter = max_current

    for j in range(0, N):
        if retorno[j] < max_counter:
            retorno[j] = max_counter

    return retorno

if __name__ == '__main__':
    print(solution(5, [3, 4, 4, 6, 1, 4, 4]))