import sys
import networkx as nx
import matplotlib.pyplot as plt
import random as rd
import numpy as np

np.set_printoptions(threshold=sys.maxsize)

# ************ FUNÇÃO QUE GERA A MATRIZ DE ADJACÊNCIA ************
def geraMatriz(numComunidade, numVertices, grauMedio, Pin, Pout):
    k_atual = 0
    arestas = 0
    totalVertices = numComunidade * numVertices

    matrizAdj = np.zeros((totalVertices, totalVertices))

    for i in range(0, totalVertices):
        matrizAdj[i][i] = 1

    while k_atual < grauMedio:

        comunidade = rd.randint(0, numComunidade - 1)
        if comunidade == 0:
            alcance = range(0, numVertices)
        if comunidade == 1:
            alcance = range(numVertices, 2 * numVertices)
        if comunidade == 2:
            alcance = range(2 * numVertices, 3 * numVertices)
        if comunidade == 3:
            alcance = range(3 * numVertices, 4 * numVertices)
        if comunidade == 4:
            alcance = range(4 * numVertices, 5 * numVertices)
        if comunidade == 5:
            alcance = range(5 * numVertices, 6 * numVertices)
        if comunidade == 6:
            alcance = range(6 * numVertices, 7 * numVertices)
        if comunidade == 7:
            alcance = range(7 * numVertices, 8 * numVertices)
        if comunidade == 8:
            alcance = range(8 * numVertices, 9 * numVertices)
        if comunidade == 9:
            alcance = range(9 * numVertices, 10 * numVertices)

        lista = rd.sample(alcance, 2)
        vr1 = lista[0]
        vr2 = lista[1]
        prob = rd.random()

        if prob < Pin:
            if matrizAdj[vr1][vr2] == 0:
                matrizAdj[vr1][vr2] = 1
                matrizAdj[vr2][vr1] = 1
                arestas += 1

        listaInter = rd.sample(range(0, totalVertices), 2)
        vr1inter = listaInter[0]
        vr2inter = listaInter[1]

        prob = rd.random()
        if prob < Pout:
            if matrizAdj[vr1inter][vr2inter] == 0:
                matrizAdj[vr1inter][vr2inter] = 1
                matrizAdj[vr2inter][vr1inter] = 1
                arestas += 1
        k_atual = arestas / totalVertices

    return matrizAdj

# ************ FUNÇÃO QUE GERA O GRAFO ************
def geraGrafo(matrizAdj, tamanho, numVertices):
    G = nx.Graph()
    colormap = []
    for x in range(tamanho):
        G.add_node(x + 1)
        if x < numVertices:
            colormap.append('blue')
        if x > numVertices - 1 and x < 2 * numVertices:
            colormap.append('green')
        if x > 2 * numVertices - 1 and x < 3 * numVertices:
            colormap.append('red')
        if x > 3 * numVertices - 1 and x < 4 * numVertices:
            colormap.append('purple')
        if x > 4 * numVertices - 1 and x < 5 * numVertices:
            colormap.append('gray')
        if x > 5 * numVertices - 1 and x < 6 * numVertices:
            colormap.append('teal')
        if x > 6 * numVertices - 1 and x < 7 * numVertices:
            colormap.append('lime')
        if x > 7 * numVertices - 1 and x < 8 * numVertices:
            colormap.append('brown')
        if x > 8 * numVertices - 1 and x < 9 * numVertices:
            colormap.append('gold')
    for i in range(tamanho):
        for j in range(tamanho):
            if matrizAdj[i][j] == 1:
                G.add_edge(i + 1, j + 1)
#************ PLOTAR A MATRIZ_ADJ E O GRAFO ************
    plt.figure(2, figsize=(5, 5))
    fig = plt.imshow(matrizAdj, cmap='hot', interpolation='nearest')
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    plt.figure(1, figsize=(7, 7))
    nx.draw(G, node_color=colormap, font_color='white', node_size=500, with_labels=False)
    plt.show()

print("**************** Grafo Randômico Clusterizado ****************")

M = int(input('Entre com o numero de comunidades(de 1 a 9): ')) #Nº_COMUNIDADES
N = int(input('Entre com o numero de vertices de cada comunidade: ')) #Nº_VERTICES_COMUNIDADE
K = 16
Pin = float(input('Entre com a probabilidade P_in(de 0 a 1): ')) #PROBABILIDADE DE UM NÓ ALEATORIO SE LIGAR COM A SUA PRÓPRIA COMUNIDADE
Pout = 1 - Pin #PROBABILIDADE DE UM NÓ ALEATORIO SE LIGAR COM OUTRA COMUNIDADE

geraGrafo(geraMatriz(M,N,K,Pin,Pout), M*N, N)
