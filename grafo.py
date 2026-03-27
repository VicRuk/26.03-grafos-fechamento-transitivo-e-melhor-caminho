from vertice import Vertice

class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.vertices = [Vertice(i) for i in range(num_vertices)]

    def cria_adjacencia(self, i, j, P):
        if 0 <= i < self.num_vertices and 0 <= j < self.num_vertices:
            self.vertices[i].adicionar_adjacencia(j, P)
        else:
            print("Erro: Índices de vértices inválidos.")

    def remove_adjacencia(self, i, j):
        if 0 <= i < self.num_vertices:
            self.vertices[i].remover_adjacencia(j)

    def imprime_adjacencias(self):
        print("Matriz de Adjacências:")
        for i in range(self.num_vertices):
            linha_matriz = [0] * self.num_vertices
            for aresta in self.vertices[i].adjacencias:
                linha_matriz[aresta.destino] = aresta.peso
            
            rotulo = self.vertices[i].informacao
            linha_str = "\t".join(map(str, linha_matriz))
            print(f"{rotulo:<15} |\t{linha_str}")

    def seta_informacao(self, i, V):
        if 0 <= i < self.num_vertices:
            self.vertices[i].informacao = str(V)
        else:
            print("Erro: Vértice inexistente.")

    def adjacentes(self, i, adj):
        if 0 <= i < self.num_vertices:
            adj.clear()
            for aresta in self.vertices[i].adjacencias:
                adj.append(aresta.destino)
            return len(adj)
        return 0
    
    def warshall(self):
        # 1. Inicialização da matriz de fechamento a partir da lista de adjacências
        fechamento = [[False] * self.num_vertices for _ in range(self.num_vertices)]
        
        for i in range(self.num_vertices):
            for aresta in self.vertices[i].adjacencias:
                fechamento[i][aresta.destino] = True
                
        # 2. Algoritmo de Warshall
        for k in range(self.num_vertices):
            for i in range(self.num_vertices):
                if fechamento[i][k]:
                    for j in range(self.num_vertices):
                        fechamento[i][j] = fechamento[i][j] or fechamento[k][j]
                        

        print("\nMatriz de Alcançabilidade (Fechamento Transitivo):")
        for i in range(self.num_vertices):
            linha = ["1" if val else "0" for val in fechamento[i]]
            rotulo = self.vertices[i].informacao
            print(f"{rotulo:<15} |\t" + "\t".join(linha))
            
        return fechamento

    def dijkstra(self, s, t):
        INFINITO = float('inf')
        distancia = [INFINITO] * self.num_vertices
        perm = [False] * self.num_vertices
        caminho = [-1] * self.num_vertices

        distancia[s] = 0
        corrente = s

        # Executa até que o nó destino se torne membro do conjunto perm ou não haja mais caminhos
        while corrente != t and corrente != -1:
            perm[corrente] = True
            dc = distancia[corrente]

            # Atualiza as distâncias para os sucessores do nó corrente
            for aresta in self.vertices[corrente].adjacencias:
                i = aresta.destino
                if not perm[i]:
                    novadist = dc + aresta.peso
                    if novadist < distancia[i]:
                        distancia[i] = novadist
                        caminho[i] = corrente
            
            # Busca o próximo nó com a menor distância que ainda não pertence a 'perm'
            menordist = INFINITO
            k = -1
            for i in range(self.num_vertices):
                if not perm[i] and distancia[i] < menordist:
                    menordist = distancia[i]
                    k = i
            
            corrente = k

        # Remonta o caminho percorrido através do vetor auxiliar
        rota = []
        if distancia[t] != INFINITO:
            atual = t
            while atual != -1:
                rota.insert(0, atual)
                atual = caminho[atual]
                
        return distancia[t], rota