class CyclicRotation:

    def __init__(self):
        self.__matriz = []

    def set_matriz(self, matriz):
        self.__matriz = matriz

    def get_matriz(self) -> list:
        return self.__matriz

    def loop_ciclo(self) -> list:

        if self.__matriz == []:
            return self.__matriz

        tamanho = len(self.__matriz)
        matriz_ciclada = self.criar_matriz(tamanho)

        matriz_ciclada[0] = self.__matriz[-1]
        for i in range(1, tamanho):
            matriz_ciclada[i] = self.__matriz[i - 1]

        self.__matriz = matriz_ciclada
        return self.__matriz

    def criar_matriz(self, tamanho) -> list:
        matriz = []
        cont = 0
        for i in range(0, tamanho):
            matriz.append(cont)
            cont += 1

        return matriz

    def ciclar_matriz(self, qtd_ciclos) -> list:

        for i in range(0, qtd_ciclos):
            self.loop_ciclo()

        return self.__matriz

def solution(A, K):
    cyclic = CyclicRotation()
    cyclic.set_matriz(A)
    ciclado = cyclic.ciclar_matriz(K)
    return ciclado


if __name__ == '__main__':
    print(solution([], 2))
