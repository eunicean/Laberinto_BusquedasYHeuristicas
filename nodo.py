class Nodo:
    def __init__(self, estado, padre=None, costo=0, heuristica=0):
        self.estado = estado  # (fila, columna)
        self.padre = padre
        self.costo = costo
        self.heuristica = heuristica

    def __lt__(self, otro):
        return (self.costo + self.heuristica) < (otro.costo + otro.heuristica)
