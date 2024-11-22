class ContarLivrosImpares:
    @staticmethod
    def contar_livros_impares(fila):
        return sum(1 for livro in fila if livro % 2 != 0)

if __name__ == "__main__":
    fila = [101, 202, 303, 404, 505]
    impares = ContarLivrosImpares.contar_livros_impares(fila)
    print("Quantidade de livros com números ímpares:", impares)
