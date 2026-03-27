from grafo import Grafo

def main():
    print("="*50)
    print("   SIMULAÇÃO DE GRAFOS (MAPA)")
    print("="*50)
    
    print("[*] A inicializar o mapa com 5 locais...")
    grafo = Grafo(5)
    
    grafo.seta_informacao(0, "Casa")
    grafo.seta_informacao(1, "Trabalho")
    grafo.seta_informacao(2, "Faculdade")
    grafo.seta_informacao(3, "Academia")
    grafo.seta_informacao(4, "Parque")
    
    print("[*] A estabelecer rotas e distâncias (em km/minutos)...")
    grafo.cria_adjacencia(0, 1, 10)  
    grafo.cria_adjacencia(0, 2, 25)  
    grafo.cria_adjacencia(1, 3, 40)
    grafo.cria_adjacencia(2, 3, 35)
    grafo.cria_adjacencia(2, 4, 5)
    
    print("\n" + "-"*50)
    grafo.imprime_adjacencias()
    print("-"*50)
    
    vetor_adj = []
    qtd = grafo.adjacentes(2, vetor_adj)
    
    print(f"\n[Análise de Rotas] A partir da Faculdade (índice 2) tem acesso a {qtd} local(is).")
    print(f"Índices de destino: {vetor_adj}")
    
    nomes_conectados = [grafo.vertices[idx].informacao for idx in vetor_adj]
    print(f"Nomes dos Lugares: {nomes_conectados}")
    print("="*50)

    print("\n[*] A executar o Algoritmo de Warshall (Matriz de Alcançabilidade)...")
    grafo.warshall()
    print("="*50)

    print("\n[*] A executar o Algoritmo de Dijkstra (Menor Caminho)...")
    
    # Teste 1: Casa (0) para Academia (3)
    print("\n-> Rota: Casa (0) até Academia (3)")
    dist, rota = grafo.dijkstra(0, 3)
    # Verifica tanto o float('inf') do Python quanto o 999999999
    if dist == float('inf') or dist == 999999999:
        print("Não existe um caminho possível.")
    else:
        nomes_rota = [grafo.vertices[idx].informacao for idx in rota]
        print(f"Menor distância encontrada: {dist}")
        print(f"Caminho percorrido: {' -> '.join(nomes_rota)}")

    # Teste 2: Casa (0) para Parque (4)
    print("\n-> Rota: Casa (0) até Parque (4)")
    dist, rota = grafo.dijkstra(0, 4)
    if dist == float('inf') or dist == 999999999:
        print("Não existe um caminho possível.")
    else:
        nomes_rota = [grafo.vertices[idx].informacao for idx in rota]
        print(f"Menor distância encontrada: {dist}")
        print(f"Caminho percorrido: {' -> '.join(nomes_rota)}")

    # Teste 3: Academia (3) para Casa (0) - Rota sem saída
    print("\n-> Rota: Academia (3) até Casa (0) [Teste de Rota Inexistente]")
    dist, rota = grafo.dijkstra(3, 0)
    if dist == float('inf') or dist == 999999999:
        print("Não existe um caminho possível.")
    else:
        nomes_rota = [grafo.vertices[idx].informacao for idx in rota]
        print(f"Menor distância encontrada: {dist}")
        print(f"Caminho percorrido: {' -> '.join(nomes_rota)}")
        
    print("\n" + "="*50)

if __name__ == "__main__":
    main()