
class BinaryGap:

    def __init__(self):
        self.__numero = 0
        self.__numero_binario = 0

    def set_numero(self, numero):
        self.__numero = numero
        self.converter_binario()

    def get_numero(self):
        return self.__numero

    def get_binario(self):
        return self.__numero_binario

    def converter_binario(self):
        binario = bin(self.__numero)
        binario_str = ''
        for i in range(0, len(binario)):
            if i > 1:
                binario_str += binario[i]

        self.__numero_binario = binario_str

    def calcular_comprimento_intervalo(self):
        binario = str(self.get_binario())
        tamanho_intervalo = 0
        loop_intervalo = 0
        intervalo = False
        cont = 0
        inicio_intervalo = 0

        for i in binario:
            if int(i) == 1 and intervalo is False:
                intervalo = True
                inicio_intervalo = cont

            if intervalo is True and int(i) == 0:
                loop_intervalo += 1

            if intervalo is True and int(i) == 1 and inicio_intervalo != cont:
                intervalo = False

            if loop_intervalo > tamanho_intervalo and intervalo is False:
                tamanho_intervalo = loop_intervalo
                loop_intervalo = 0

            cont += 1

        return tamanho_intervalo

def solution(N):
    binary = BinaryGap()
    binary.set_numero(N)
    return binary.calcular_comprimento_intervalo()

if __name__ == '__main__':
    print(solution(20))