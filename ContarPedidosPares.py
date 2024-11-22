class ContarPedidosPares:
    @staticmethod
    def contar_pedidos_pares(pilha):
        return sum(1 for pedido in pilha if pedido % 2 == 0)

if __name__ == "__main__":
    pilha = [1, 2, 3, 4, 5]
    pares = ContarPedidosPares.contar_pedidos_pares(pilha)
    print("Quantidade de pedidos pares:", pares)
