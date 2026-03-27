from grafo import Grafo

def exibir_menu():
    print("\n" + "="*30)
    print("    MENU DO GRAFO")
    print("="*30)
    print("1. Atualizar informação de um vértice")
    print("2. Criar nova adjacência (Aresta)")
    print("3. Remover adjacência")
    print("4. Imprimir matriz de adjacências")
    print("5. Ver adjacentes de um vértice")
    print("6. Matriz de Alcançabilidade (Warshall)")
    print("7. Menor Caminho (Dijkstra)")
    print("0. Sair do programa")
    print("="*30)
    return input("Escolha uma opção: ")

def main():
    print("Bem-vindo ao sistema de Grafos!")
    
    while True:
        try:
            num_v = int(input("Para começar, digite a quantidade de vértices do grafo: "))
            if num_v > 0:
                break
            print("O grafo precisa ter pelo menos 1 vértice.")
        except ValueError:
            print("Erro: digite um número inteiro")

    grafo = Grafo(num_v)
    print(f"\nGrafo criado com sucesso! Os índices vão de 0 a {num_v - 1}.")

    while True:
        opcao = exibir_menu()

        try:
            if opcao == '1':
                i = int(input(f"Digite o índice do vértice (0 a {num_v - 1}): "))
                info = input("Digite o nome/rótulo para este vértice: ")
                grafo.seta_informacao(i, info)
                print("Atualizado com sucesso")

            elif opcao == '2':
                i = int(input("Índice do vértice de ORIGEM: "))
                j = int(input("Índice do vértice de DESTINO: "))
                peso = int(input("Peso (custo) da aresta: "))
                grafo.cria_adjacencia(i, j, peso)
                print("Adicionado com sucesso")

            elif opcao == '3':
                i = int(input("Índice do vértice de ORIGEM: "))
                j = int(input("Índice do vértice de DESTINO: "))
                grafo.remove_adjacencia(i, j)
                print("Removido com sucesso")

            elif opcao == '4':
                grafo.imprime_adjacencias()

            elif opcao == '5':
                i = int(input("Digite o índice do vértice de origem: "))
                vetor_adj = []
                qtd = grafo.adjacentes(i, vetor_adj)
                print(f"O vértice {i} possui {qtd} adjacente(s).")
                print(f"Destinos conectados: {vetor_adj}")

            elif opcao == '6':
                grafo.warshall()

            elif opcao == '7':
                s = int(input("Índice do vértice de ORIGEM: "))
                t = int(input("Índice do vértice de DESTINO: "))
                distancia, rota = grafo.dijkstra(s, t)
                
                if distancia == float('inf'):
                    print(f"Não existe um caminho possível entre {s} e {t}.")
                else:
                    nomes_rota = [grafo.vertices[idx].informacao for idx in rota]
                    print(f"\nMenor distância encontrada: {distancia}")
                    print(f"Caminho percorrido: {' -> '.join(nomes_rota)}")

            elif opcao == '0':
                print("Saindo do programa...")
                break

            else:
                print("Opção inválida")
                
        except ValueError:
            print("Erro: Entrada inválida")

if __name__ == "__main__":
    main()