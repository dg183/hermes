# Python program for solution of  
# hamiltonian cycle problem  

class Edge():
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight
    
    def __str__(self):
        return f'Edge({self.source},{self.destination},{self.weight})'
        
    def __repr__(self):
        return f'Edge({self.source},{self.destination},{self.weight})'