class OrdenarListaEficiente:
    @staticmethod
    def ordenar_lista(lista):
        return sorted(lista)  # Uso do Timsort, algoritmo eficiente para grandes listas

if __name__ == "__main__":
    import random
    # Gerando uma lista de 5 milhões de números aleatórios
    lista = [random.randint(1, 1000000) for _ in range(5000000)]
    print("Ordenando uma lista de 5 milhões de elementos...")
    ordenada = OrdenarListaEficiente.ordenar_lista(lista)
    print("Lista ordenada (exibindo os 10 primeiros elementos):", ordenada[:10])
