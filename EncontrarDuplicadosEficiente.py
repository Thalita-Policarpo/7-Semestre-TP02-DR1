class EncontrarDuplicadosEficiente:
    @staticmethod
    def encontrar_duplicados(lista):
        vistos = set()
        duplicados = set()
        for numero in lista:
            if numero in vistos:
                duplicados.add(numero)
            else:
                vistos.add(numero)
        return duplicados

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 2, 5, 6, 3]
    duplicados = EncontrarDuplicadosEficiente.encontrar_duplicados(lista)
    print("Duplicados encontrados (eficiente):", duplicados)
