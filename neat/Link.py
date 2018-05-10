from random import random, gauss

class Link:
    
    def __init__(self, from_node, to_node, innovation_num):
        self.from_node      = from_node
        self.to_node        = to_node
        self.weight         = random()*2 -1
        self.enabled        = True
        self.innovation_num = innovation_num
    
    def mutate(self):
        """
        mutate the weight in place, following the paper
        """
        if random() < 0.1:
            self.weight = random()*2 -1
        else:
            self.weight += gauss(0, 1)
            if self.weight > 1:
                self.weight = 1 
            if self.weight < -1:
                self.weight = -1
                
    def equals(self, l):
        """
        true if they are connected to the same nodes
        """
        return l.from_node == self.from_node and
               l.to_node   == self.to_node