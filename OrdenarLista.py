class OrdenarLista:
    @staticmethod
    def ordenar_sem_funcoes(lista):
        for i in range(len(lista)):
            for j in range(0, len(lista) - i - 1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
        return lista

if __name__ == "__main__":
    lista = [5, 3, 8, 4, 2]
    ordenada = OrdenarLista.ordenar_sem_funcoes(lista)
    print("Lista ordenada:", ordenada)
