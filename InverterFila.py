from collections import deque

class InverterFila:
    @staticmethod
    def inverter_fila(fila):
        return deque(reversed(fila))

if __name__ == "__main__":
    fila = deque([1, 2, 3, 4, 5])
    invertida = InverterFila.inverter_fila(fila)
    print("Fila invertida:", list(invertida))
