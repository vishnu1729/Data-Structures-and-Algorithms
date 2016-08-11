""" graph adt implementation for undirected graph along with breadth first and depth first traversals
class Graph creates an empty graph in which various methods are provided
to perform different operations"""
""" Author: Vishnu Muralidharan"""

class Graph:
    # a Vertex class models the Vertex in a Graph
    # nested so that it can only be created by the insertVertex fuction
    class Vertex:
        def __init__(self,value):
            self._value = value             # holds the label denoting the vertex
            self._neighbors = {}            # an empty dictionary that is the adjacency list for the vertex
        
        def element(self):
            return self._value              # retuens the vertex label
    # the graph is realized as dileneated:
    # first a top level dictionaty is created that stores all the vertices as keys
    # for each key or in other words a vertex, an afajacency dictionary is created to denote the conneting edges
    # so overall it is a nested strucure of a dictionaries within a dictionary
    
    def __init__(self):
        self._vertList = {}                 # an empty disttionary that holds the different vertices of the graph

    # method to insert a vertex. declaration Vertex(value) is invalid outside the class    
    def insertVertex(self,value):
        newVertex = self.Vertex(value)      # create new vertex object
        self._vertList[value] = newVertex   # add the vertex to the vertices list with the value as the key
        return newVertex

    # method to return the list of all vertices 
    def vertices(self):
        return self._vertList

    # method to insert an edge, an undirected graph is assumed
    def insertEdge(self,src,dst,weight=1):
        self._vertList[src]._neighbors[dst] = weight    # enter the appropriate weight at the (src,dst) creating an edge 
        self._vertList[dst]._neighbors[src] = weight    # since it is an undirected graph, the edge is symmetrical

    # method to return an edge given the endpoints
    def getEdge(self,src,dst):
         return self._vertList[src]._neighbors[self._vertList[dst]]

    # method to print all the vertices connected by an edge
    def printEdges(self):
        for vertex in self._vertList:
            print(vertex,":",self._vertList[vertex]._neighbors)         # for each vertex print the adajacency dictionary
        
    # method to obtain the neighbors connected by an edge for a vertex   
    def nbrEdges(self,vertex):
        adj = self._vertList[vertex]._neighbors.keys()
        return adj

    # method to perform the breadth first search, a starting vertex is provided as argument 
    def BFSearch(self,vertex):
        level = [vertex]                            # the current level of vertices being processed
        discovered = [vertex]                       # mark the starting vertex as visited
        while len(level):                           # while the current level is not empty
            parent = []                             # list used to hold the next level of vertices to be processed
            for u in level:                         # in the current level
                for v in self.nbrEdges(u):          # check the neighbors of the current vertex u
                    if v not in discovered:         # if there is an unvisited neighbor
                        discovered.append(v)        # mark unvisited neighbor as visited
                        parent.append(v)            # next level of nodes to be processed
            level = parent                          # move to the next level
        return discovered                           # return the travered list of vertices

    # method to perform the depth first search, an arbitrary starting vertex is chosen
    def DFSearch(self):
        discovered = []                             # empty list of visited vertices
        for vertex in self._vertList:               # loop through the vertices in the graph
            if vertex not in discovered:            # if the vertex is not discovered
                self.dfsVisit(vertex,discovered)    # call method to visit deep down the branch
        return discovered                           # return the list of traversed vertices

    # method to explore a branch to the deepest level
    def dfsVisit(self,currentVertex,visited):
        visited.append(currentVertex)               # mark the current vertex as visited
        for nbr in self.nbrEdges(currentVertex):    # examine the neighbors of the current vertex
            if nbr not in visited:                  # if one of the neighbors is not visited
                self.dfsVisit(nbr,visited)          # recursive call to visit the connecting vertex
    
        
g = Graph()
g.insertVertex('A')
g.insertVertex('B')
g.insertVertex('C')
g.insertVertex('D')
g.insertVertex('E')
g.insertVertex('F')


g.insertEdge('A','B',5)
g.insertEdge('A','D',2)
g.insertEdge('B','D',4)
g.insertEdge('B','C',9)
g.insertEdge('D','E',7)
g.insertEdge('E','B',3)
g.insertEdge('E','F',1)
g.insertEdge('F','C',8)


g.printEdges()
print(g.BFSearch('F'))
print(g.DFSearch())
