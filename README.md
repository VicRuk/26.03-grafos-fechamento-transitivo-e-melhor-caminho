# Fechamento Transitivo e Melhor Caminho - TDE2

Integrantes do grupo:
- Gustavo Lazzari
- Mateus Roese
- Matheus Yamamoto
- Victor Ryuki

Projeto referente à matéria *Resolução de Problemas com Grafos* que estende a representação de grafo com listas de adjacências implementada no TDE anterior, acrescentando a implementação e teste do algoritmo de Warshall para determinação da Matriz de Alcançabilidade (Fechamento Transitivo) e do algoritmo de Dijkstra para determinação do menor caminho entre dois vértices.

## 1. Como executar

```zsh
python main.py
```

Para rodar a simulação de exemplo:

```zsh
python simulador.py
```

## 2. Estrutura do Repositório

```
.
├── aresta.py      # Classe Aresta, armazena o destino e o peso de uma aresta
├── vertice.py     # Classe Vertice, armazena id, rotulo e lista de adjacências
├── grafo.py       # Classe Grafo, implementa as operacoes sobre o grafo (criar/remover adjacência, imprimir matriz, Warshall, Dijkstra)
├── main.py        # Menu interativo para manipular o grafo via terminal
├── simulador.py   # Exemplo pronto que cria um grafo de 5 locais e demonstra todas as operacoes, incluindo Warshall e Dijkstra
└── README.md      
```

## 3. Operações disponíveis

- cria_adjacencia(i, j, P) - cria uma aresta direcionada de i para j com peso P
- remove_adjacencia(i, j) - remove a aresta de i para j
- imprime_adjacencias() - exibe a matriz de adjacências do grafo
- seta_informacao(i, V) - define o rótulo do vértice i com a string V
- adjacentes(i, adj) - retorna a quantidade de adjacentes do vértice i e preenche o vetor adj com eles
- warshall() - calcula e exibe a Matriz de Alcançabilidade (Fechamento Transitivo) utilizando o algoritmo de Warshall
- dijkstra(s, t) - calcula o menor caminho do vértice s até o vértice t utilizando o algoritmo de Dijkstra, retornando a distância e a rota percorrida

## 4. Exemplo de uso 

Saída do programa simulador.py, que cria um grafo de 5 locais e demonstra todas as operações:

```
==================================================
   SIMULAÇÃO DE GRAFOS (MAPA)
==================================================
[*] A inicializar o mapa com 5 locais...
[*] A estabelecer rotas e distâncias (em km/minutos)...

--------------------------------------------------
Matriz de Adjacências:
Casa            |	0	10	25	0	0
Trabalho        |	0	0	0	40	0
Faculdade       |	0	0	0	35	5
Academia        |	0	0	0	0	0
Parque          |	0	0	0	0	0
--------------------------------------------------

[Análise de Rotas] A partir da Faculdade (índice 2) tem acesso a 2 local(is).
Índices de destino: [3, 4]
Nomes dos Lugares: ['Academia', 'Parque']
==================================================

[*] A executar o Algoritmo de Warshall (Matriz de Alcançabilidade)...

Matriz de Alcançabilidade (Fechamento Transitivo):
Casa            |	0	1	1	1	1
Trabalho        |	0	0	0	1	0
Faculdade       |	0	0	0	1	1
Academia        |	0	0	0	0	0
Parque          |	0	0	0	0	0
==================================================

[*] A executar o Algoritmo de Dijkstra (Menor Caminho)...

-> Rota: Casa (0) até Academia (3)
Menor distância encontrada: 50
Caminho percorrido: Casa -> Trabalho -> Academia

-> Rota: Casa (0) até Parque (4)
Menor distância encontrada: 30
Caminho percorrido: Casa -> Faculdade -> Parque

-> Rota: Academia (3) até Casa (0) [Teste de Rota Inexistente]
Não existe um caminho possível.

==================================================
```