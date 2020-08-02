# Python program for solution of  
# hamiltonian cycle problem  
from sortededges import *
class Graph():  
    def __init__(self, addresses):  
        self.V = len(addresses)  
        self.graph = [[0 for column in range(self.V)] 
                            for row in range(self.V)]  
        self.addresses = addresses
  
    ''' Check if this vertex is an adjacent vertex  
        of the previously added vertex and is not  
        included in the path earlier '''
    def isSafe(self, v, pos, path):  
        # Check if current vertex and last vertex  
        # in path are adjacent  
        if self.graph[ path[pos-1] ][v] == 0:  
            return False
  
        # Check if current vertex not already in path  
        for vertex in path:  
            if vertex == v:  
                return False
  
        return True
        
    def solve(self):
        # make sorted list of all edges
        # apply in ascending order until circuit made
        
        edges = []
        
        row_count = 0
        for row in self.graph:
            col_count = 0
            for col in row:
                edges.append(Edge(row_count,col_count,col))
                
                col_count += 1
                
            row_count += 1
                
                
        print(edges)
        edges = sorted(edges, key=lambda edge:edge.weight)
        print(edges)
        
        # weight = col["distance"]["value"]
        # matrix[row_count][col_count] = Edge(addresses[row_count],addresses[col_count],weight)
  
    # A recursive utility function to solve  
    # hamiltonian cycle problem  
    def hamCycleUtil(self, path, pos):  
  
        # base case: if all vertices are  
        # included in the path  
        if pos == self.V:  
            # Last vertex must be adjacent to the  
            # first vertex in path to make a cyle  
            if self.graph[ path[pos-1] ][ path[0] ] == 1:  
                return True
            else:  
                return False
  
        # Try different vertices as a next candidate  
        # in Hamiltonian Cycle. We don't try for 0 as  
        # we included 0 as starting point in hamCycle()  
        for v in range(1,self.V):  
  
            if self.isSafe(v, pos, path) == True:  
  
                path[pos] = v  
  
                if self.hamCycleUtil(path, pos+1) == True:  
                    return True
  
                # Remove current vertex if it doesn't  
                # lead to a solution  
                path[pos] = -1
  
        return False
  
    def hamCycle(self):  
        path = [-1] * self.V  
  
        ''' Let us put vertex 0 as the first vertex  
            in the path. If there is a Hamiltonian Cycle,  
            then the path can be started from any point  
            of the cycle as the graph is undirected '''
        path[0] = 0
  
        if self.hamCycleUtil(path,1) == False:  
            print ("Solution does not exist\n") 
            return False
  
        self.printSolution(path)  
        return True
  
    def printSolution(self, path):  
        print ("Solution Exists: Following", 
                 "is one Hamiltonian Cycle") 
        for vertex in path:  
            print (vertex, end = " ") 
        print (path[0], "\n") 