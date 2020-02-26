
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
        tamanho = len(self.get_binario())
        tamanho_intervalo = 0
        intervalo = []
        binario = self.get_binario()
        sair = False
        cont_while = 0
        for cont in range(0, tamanho):

            if cont_while > 0:
                cont_while -= 1
                continue

            else:
                i = int(binario[cont])
                if i == 1:
                    intervalo.append(i)
                    a = cont + 1
                    while not sair:
                        cont_while += 1
                        i = int(binario[a])
                        if cont_while > tamanho or i == 1:
                            sair = True

                        else:
                            intervalo.append(i)
                            tamanho_intervalo += 1

                        a += 1

        print(tamanho_intervalo)
        print(intervalo)



if __name__ == '__main__':
    binary = BinaryGap()
    binary.set_numero(153)
    print(binary.get_binario())
    binary.calcular_comprimento_intervalo()