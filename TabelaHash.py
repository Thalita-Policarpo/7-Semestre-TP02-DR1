class TabelaHash:
    def __init__(self, tamanho):
        self.tabela = [[] for _ in range(tamanho)]
        self.tamanho = tamanho

    def inserir(self, chave, valor):
        indice = hash(chave) % self.tamanho
        for item in self.tabela[indice]:
            if item[0] == chave:
                item[1] = valor
                return
        self.tabela[indice].append([chave, valor])

    def buscar(self, chave):
        indice = hash(chave) % self.tamanho
        for item in self.tabela[indice]:
            if item[0] == chave:
                return item[1]
        return None

    def remover(self, chave):
        indice = hash(chave) % self.tamanho
        for item in self.tabela[indice]:
            if item[0] == chave:
                self.tabela[indice].remove(item)
                return

if __name__ == "__main__":
    tabela = TabelaHash(10)
    tabela.inserir("chave1", "valor1")
    tabela.inserir("chave2", "valor2")
    print("Valor da chave1:", tabela.buscar("chave1"))
    tabela.remover("chave1")
    print("Valor da chave1 após remoção:", tabela.buscar("chave1"))
