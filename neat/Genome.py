import random import random, randint, choice
from math import exp
from copy import deepcopy

from Link import Link
from Node import Node

class Genome:
    
    def __init__(self, inputs_n, outputs_n):
        self.links  = []
        # self.nodes is a matrix. self.node[i][j] is the j-neuron on the i-layer
        # thus, the number of layers is len(self.nodes)
        self.nodes  = [[], []]
        
        # create I/O nodes
        for i in range(inputs_n):
            self.nodes[0].append(Node(i))
        for i in range(outputs_n):
            self.nodes[1].append(Node(inputs_n+i))    
        
        # create only one random link between input and output layer
        n0 = random.choice(self.nodes[0])
        n1 = random.choice(self.nodes[1])
        l  = Link(n0, n1, inn numbner gloabl)
        n0.out_links.append(l)
        self.links.append(l)
    
    
    def _feed_forward(self, inputs):
        for layer, i, val in zip(self.nodes, range(len(self.nodes)), inputs):
            for node in self.nodes[layer]:
            
                if i == 0: #if first layer copy input values in input nodes
                    node.output_sum = val
                else:
                    node.output_sum = self.relu(node.input_sum)
                    
                for link in node.out_links: 
                    link.to_node.input_sum += node.output_sum * link.weight
        
        # return outputs
        for node in self.nodes[-1]:    #output nodes, in the last layer
            yield sigm(node.output_sum)
        

    def mutate(self, link_history):
        """
        mutate the genome following Kenneth O. Stanley's paper.
        Doesn't mutate in place, but returns a new mutated genome
        """
        g = deepcopy(self)    #new genome to be muted and returned
        
        if random() < 0.8:    #mutate all weights with 80% prob
            map(lambda link: link.mutate(), g.links)
        
        if random() < 0.05:    #add new link with 5% prob
            g.add_link(link_history)
        
        if random() < 0.01:    #add new node with 1% prob
            g.add_node()
        
        return g
        

    # utilities
    def add_link(self, link_history):
        """
        Creates a random link between 2 not connected nodes
        """
        _l1 = choice(range(len(self.nodes)))
        _l2 = choice(range(len(self.nodes)))
        while _l1 == _l2:
            _l1 = choice(range(len(self.nodes)))
            _l2 = choice(range(len(self.nodes)))
        
        l1 = min(_l1, _l2)
        l2 = max(_l1, _l2)
        
        n1 = choice(self.nodes[l1])
        n2 = choice(self.nodes[l2])
        while n2 in n1.out_links:
            n1 = choice(self.nodes[l1])
            n2 = choice(self.nodes[l2])
            
        link = Link(n1, n2, inn numbner gloabl)
        
        # check if the same link is already formed in the current generation
        for l in link_history:
            if link.equals(l):
                link.innovation_num = l.innovation_num
        
        self.links.append(link)
        
        
    def add_node(self, link_history):
        """
        Adds a new node by splitting an existing link
        """
        link = choice(self.links)
        n1, n2 = link.from_node, link.to_node        
        
        #assert
        nodes = [node for layer in self.nodes for node in layer]
        if not n1 in nodes or not n2 in nodes:
            raise Exception("mezzo porcoddio")
        #end assert
        
        # find layer of n1 and n2
        l1, l2 = None, None
        for i in range(len(self.nodes)):
            if n1 in self.nodes[i]:
                l1 = i
            if n2 in self.nodes[i]:
                l2 = i
                
        assert(l1 > l2)
        
        link.enabled = False
        new_node = Node(gloabl node id)
        link_to_new_node   = Link(n1, new_node, gloabl inn numb)
        link_from_new_node = Link(new_node, n2, gloabl inn numb)
        #change the weight of new links according to the paper
        link_to_new_node.weight   = 1
        link_from_new_node.weight = link.weight
        #update outgoing links of new_node
        new_node.out_links += link_from_new_node
        #update self.links
        self.links.append(link_from_new_node)
        self.links.append(link_tonew_node)
        if l2 == l1 +1:    #if they are consecutive layers create a new one
            self.nodes = self.nodes[:l2] + [[new_node]] + self.nodes[l2:]
        else:            #if they are not consecutive a node is added to the l+1 layer
            self.nodes[l1+1].append(new_node)

    
    # utilities inutyli        
    def display(self):
        """
        funzione bruzza che stampa a schermo piu o meno come appare la rete
        """
        pass

    def feed_forward(self, inputs):
        return list(self._feed_forward(inputs))


def relu(x):
    return max(0, x)
    
def sigm(x):
    return 1/(1+exp(-x))




    
    
    
    