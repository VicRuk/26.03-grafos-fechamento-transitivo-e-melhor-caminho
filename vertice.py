from aresta import Aresta

class Vertice:
    def __init__(self, id_vertice):
        self.id_vertice = id_vertice
        self.informacao = "Sem Rótulo"
        self.adjacencias = []

    def adicionar_adjacencia(self, destino, peso):
        nova_aresta = Aresta(destino, peso)
        self.adjacencias.append(nova_aresta)

    def remover_adjacencia(self, destino):
        for aresta in self.adjacencias:
            if aresta.destino == destino:
                self.adjacencias.remove(aresta)
                break