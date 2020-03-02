import numpy

def solution(X, A):

    ordem = []
    cont = 0

    for i in A:
        if i not in ordem:
            ordem.append(i)

        if numpy.math.factorial(X) == numpy.prod(ordem):
            return cont

        cont += 1

    return -1


if __name__ == '__main__':
    print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))