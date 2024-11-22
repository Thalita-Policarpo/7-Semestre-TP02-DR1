class ProximaTarefaPilha:
    @staticmethod
    def tarefa_no_topo(pilha_de_tarefas):
        if pilha_de_tarefas:
            return pilha_de_tarefas[-1]
        return None

if __name__ == "__main__":
    pilha = ["Tarefa1", "Tarefa2", "Tarefa3"]
    proxima = ProximaTarefaPilha.tarefa_no_topo(pilha)
    print("Próxima tarefa no topo da pilha:", proxima)
