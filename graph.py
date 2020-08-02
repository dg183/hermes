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

    # need to make dictionary
    # key = node/vertex number (int)
    # value = list (of edges)
    # list will be sorted

    # make sorted list of all edges
    # apply in ascending order until circuit made 
    def solve(self):
        
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

        # print("====== sorted edges =======")
        # print(sorted_edges)
        # print("========================")

        # place each edge into dict where it belongs
        # row_count = 0

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
        
        
        # print("====== sorted edges AFTER SORT =======")
        # print(sorted_edges)
        # print("========================")
        # print(edges)
        # edges = sorted(edges, key=lambda edge:edge.weight)
        # print(edges)
        # ===== solve for path =====

        # while circuit not made, keep looping
        # for edge in edges:
            
        #     if edge.source not in visited and edge.de

        trip_time = 0
        # trip_dist = 0
        pos = 0
        # while path isn't complete
        while pos < self.V - 1:
            # print("============ pos = {} != self.V ({})=======",pos,self.V)
            # search through edges connected to node
            for edge in sorted_edges[path[pos]]:
                

                # the first destination we see that hasn't been visited
                # will be the closest possible destination
                if edge.destination not in visited:
                    # add to path
                    pos += 1
                    path[pos] = edge.destination
                    
                    # add to visited
                    visited.add(edge.destination)

                    # log time
                    trip_time += edge.weight

                    # print("Added")
                    # print(edge)
                    break
                
        # add trip time from last to first
        # for edge in sorted_edges[path[pos]]:
        #     if edge.destination == 0:
        #         trip_time += edge.weight
        #         break



        # recurse for path
        # if self.solveUtil(path,1) == False:
        #     print('Solution does not exist\n')
        #     return False

        

        # =============================


        # self.printSolution(path)
        return (path, trip_time)
        # ============ END HERE

        
        
        # weight = col["distance"]["value"]
        # matrix[row_count][col_count] = Edge(addresses[row_count],addresses[col_count],weight)
  
    # Recursive utility function for solve()
    def solveUtil(self, path, pos):

        # base case: if all vertices are included in path
        if pos == self.V:
            # last vertex must be adjacent to first to be cycle
            if self.graph[ path[pos-1] ][ path[0] ] == 1:
                return True
            else:
                return False

        # try different vertices to be next in path
        # don't try 0 because 0 is known origin
        for v in range(1, self.V):

            # if vertex is a possible candidate
            if self.isSafe(v, pos, path) == True:
                path[pos] = v



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