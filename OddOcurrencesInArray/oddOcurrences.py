
class OddOcurrences:

    def __init__(self):
        self.__matriz = []

    def set_matriz(self, matriz):
        self.__matriz = matriz

    def get_matriz(self):
        return self.__matriz

    def ver_emparelhados(self):
        posicoes_iguais = []

        for i in self.__matriz:
            pos_iguais = []
            for j in self.__matriz:
                if i == j:
                    pos_iguais.append(j)

            if not pos_iguais in posicoes_iguais:
                posicoes_iguais.append(pos_iguais)

        nao_emparelhado = 0
        for i in posicoes_iguais:
            if len(i) == 1:
                nao_emparelhado = i[0]

        return nao_emparelhado

def solucion(A):
    odd = OddOcurrences()
    odd.set_matriz(A)
    return odd.ver_emparelhados()

if __name__ == '__main__':
    print(solucion([1, 2, 1, 2, 4, 1, 2]))