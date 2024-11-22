from collections import deque

class FilaAtendimento:
    def __init__(self):
        self.fila = deque()

    def adicionar_cliente(self, nome):
        self.fila.append(nome)

    def atender_cliente(self):
        if self.fila:
            return self.fila.popleft()
        return "Nenhum cliente na fila."

    def tamanho_fila(self):
        return len(self.fila)

if __name__ == "__main__":
    fila = FilaAtendimento()
    fila.adicionar_cliente("Cliente1")
    fila.adicionar_cliente("Cliente2")
    print("Cliente atendido:", fila.atender_cliente())
    print("Tamanho da fila:", fila.tamanho_fila())
