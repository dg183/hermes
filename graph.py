# Python program for solution of  
# hamiltonian cycle problem  
from sortededges import *
class Graph():  
    def __init__(self, addresses):  
        self.V = len(addresses)  
        self.graph = [[0 for column in range(self.V)] 
                            for row in range(self.V)]  
        self.addresses = addresses
        

    # make sorted list of all edges
    # apply in ascending order until circuit made 
    def solve(self):
        
        # only origin has been visited initially
        visited = {0}
        
        # empty path of length 'V'
        path = [-1] * self.V

        # set first vertex in path as our first address
        # v_origin = self.addresses[0]
        path[0] = 0

        # create dict of mapping int:list
        sorted_edges = {}
        for i in range(self.V):
            sorted_edges[i] = []

        # place each edge into dict where it belongs
        # key = source
        row_count_src = 0
        for row in self.graph:
            col_count_dest = 0
            for weight in row:
                if weight == 0:
                    col_count_dest += 1
                    continue
                sorted_edges[row_count_src].append(Edge(row_count_src,col_count_dest,weight))
                col_count_dest += 1
            row_count_src += 1


        # sort edges in increasing order
        for src in sorted_edges:
            sorted_edges[src] = sorted(sorted_edges[src], key=lambda edge:edge.weight)
        

        trip_time = 0
        pos = 0
        # while path isn't complete
        while pos < self.V - 1:
            # search through edges connected to node
            for edge in sorted_edges[path[pos]]:
                # the first destination we see that hasn't been visited
                # will be the closest possible destination
                if edge.destination not in visited: # add to path
                    pos += 1
                    path[pos] = edge.destination
                    
                    # add to visited
                    visited.add(edge.destination)

                    # log time
                    trip_time += edge.weight

                    break
                    
                    
        return (path, trip_time)


  
    def printSolution(self, path):  
        print ("Solution Exists: Following", 
                 "is one Hamiltonian Cycle") 
        for vertex in path:  
            print (vertex, end = " ") 
        print (path[0], "\n") 