
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
        tamanho = len(self.get_binario()) - 1
        tamanho_intervalo = 0
        loop_intervalo = 0
        intervalo = []
        binario = self.get_binario()
        cont_while = 0
        for cont in range(0, tamanho):

            if loop_intervalo > tamanho_intervalo:
                tamanho_intervalo = loop_intervalo
                loop_intervalo = 0

            sair = False

            if cont_while > 0:
                cont_while -= 1
                continue

            else:
                i = int(binario[cont])
                if i == 1:
                    intervalo.append(i)
                    if cont + 1 > tamanho:
                        continue

                    else:
                        a = cont + 1

                    while not sair:
                        i = int(binario[a])
                        if cont_while > tamanho or i == 1:
                            sair = True
                            continue

                        else:
                            intervalo.append(i)
                            loop_intervalo += 1

                        if a + 1 > tamanho:
                            a += 1

                        else:
                            break

                        cont_while += 1

        print(tamanho_intervalo)
        print(intervalo)



if __name__ == '__main__':
    binary = BinaryGap()
    binary.set_numero(32)
    print(binary.get_binario())
    binary.calcular_comprimento_intervalo()
