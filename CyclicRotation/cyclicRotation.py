
class CyclicRotation:

    def __init__(self):
        self.__matriz = []
        self.__matriz_ciclada = []

    def set_matriz(self, matriz):
        self.__matriz = matriz

    def get_matriz(self) -> list:
        return self.__matriz

    def get_matriz_ciclada(self) -> list:
        return self.__matriz_ciclada

    def loop_ciclo(self, matriz) -> list:
        tamanho = len(matriz)
        matriz_ciclada = self.criar_matriz(tamanho)

        matriz_ciclada[0] = matriz[-1]
        for i in range(1, tamanho):
            matriz_ciclada[i] = matriz[i - 1]

        return matriz_ciclada

    @staticmethod
    def criar_matriz(tamanho) -> list:
        matriz = []
        cont = 0
        for i in range(0, tamanho):
            matriz.append(cont)
            cont += 1

        return matriz

    def ciclar_matriz(self, qtd_ciclos) -> list:
        matriz = self.get_matriz().copy()

        for i in range(0, qtd_ciclos):
            matriz = self.loop_ciclo(matriz)

        self.__matriz_ciclada = matriz

        return self.__matriz_ciclada


if __name__ == '__main__':
    cyclic = CyclicRotation()
    matriz = [1, 2, 3, 4, 5, 6]
    cyclic.set_matriz(matriz)
    print(f"Inicio: {cyclic.get_matriz()}")
    print(f"Fim: {cyclic.ciclar_matriz(2)}")
