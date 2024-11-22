class OrdenarPilha:
    @staticmethod
    def ordenar_pilha(pilha):
        pilha_aux = []
        while pilha:
            temp = pilha.pop()
            while pilha_aux and pilha_aux[-1] > temp:
                pilha.append(pilha_aux.pop())
            pilha_aux.append(temp)
        return pilha_aux

if __name__ == "__main__":
    pilha = [5, 1, 4, 2, 8]
    resultado = OrdenarPilha.ordenar_pilha(pilha)
    print("Pilha ordenada:", resultado)
