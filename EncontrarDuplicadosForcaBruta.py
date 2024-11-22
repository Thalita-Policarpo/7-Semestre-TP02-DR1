class EncontrarDuplicadosForcaBruta:
    @staticmethod
    def encontrar_duplicados(lista):
        duplicados = set()
        for i in range(len(lista)):
            for j in range(i + 1, len(lista)):
                if lista[i] == lista[j]:
                    duplicados.add(lista[i])
        return duplicados

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 2, 5, 6, 3]
    duplicados = EncontrarDuplicadosForcaBruta.encontrar_duplicados(lista)
    print("Duplicados encontrados (força bruta):", duplicados)
