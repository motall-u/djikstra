################# Exercice 2 ################
import numpy as np
import sys


#Graph

graph = np.array([
    [0,0,0,0,0,2],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,5,0,0,0],
    [0,0,0,0,0,0],
    [0,3,0,2,3,0],
])

class Djikstra():
    def __init__(self,graph,node):
        self.graph = graph
        self.node = node
        self.explored = []
        self.unexplored= [[i,sys.maxsize,None] for i in range(self.graph.shape[0])] #[node,distance,parent]
        #Initialser la distance du noeud choisi a 0
        for j in range(len(self.unexplored)):
            if self.unexplored[j][0] == self.node:
                self.unexplored[j][1] = 0 #Distance a 0
                self.unexplored[j][2] = 0 #Parent lui meme
    
    #Dispalay graph
    def display_graph(self):
        print(self.graph)

    #Tester si un arc existe
    def find_edge(self,arc_source, arc_dest ):
        if(self.graph[arc_source][arc_dest]>0):
            return True
        else:
            return False

    #Trouver valuation
    def find_valuation(self,arc_source,arc_dest):
        return self.graph[arc_source][arc_dest]
    
    #Retirer un arc du graph
    def delete_edge(self,arc_source, arc_dest):
        if self.find_edge(arc_source,arc_dest):
            self.graph[arc_source,arc_dest] = 0
        else:
            print("L'arc n'existe pas")

    

    #POur objectif de choisir le noeud avec la distance min afin de l'explorer
    def a_explorer(self):
        dist = [self.unexplored[k][1] for k in range(len(self.unexplored))]
        minimum = min(dist)
        for l in range(len(self.unexplored)):
            if self.unexplored[l][1] == minimum:
                return self.unexplored[l]

    def explorer(self):
        while len(self.unexplored) !=0:
            noeud_courant = self.a_explorer()
            #Ajouter dans explored
            self.explored.append(noeud_courant)
            #Enlever dans unexplored
            self.unexplored.remove(noeud_courant)

            # Explorer
            for m in range(len(self.unexplored)):
                if self.graph[noeud_courant[0]][self.unexplored[m][0]] > 0:
                    distance = noeud_courant[1] + self.graph[noeud_courant[0]][self.unexplored[m][0]]
                    noeud_to_update = self.unexplored[m] #element a mettre a jour verifier si sa distance et superieur a celle calculer et le mettre a jour

                    if self.unexplored[m][1] >=distance:
                        self.unexplored[m][1] = distance
                    self.unexplored[m][2] = noeud_courant[0]
                    
            
        return self.explored

dk = Djikstra(graph,0)
# print(dk.unexplored)
allgraph = dk.explorer()
print(allgraph)