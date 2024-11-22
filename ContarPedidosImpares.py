class ContarPedidosImpares:
    @staticmethod
    def contar_pedidos_impares(pilha):
        return sum(1 for pedido in pilha if pedido % 2 != 0)

if __name__ == "__main__":
    pilha = [1, 2, 3, 4, 5]
    impares = ContarPedidosImpares.contar_pedidos_impares(pilha)
    print("Quantidade de pedidos ímpares:", impares)
