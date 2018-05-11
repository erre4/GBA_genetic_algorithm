import random import random, randint, choice, sample
from numpy import inf
from math import exp
from copy import deepcopy

from Link import Link



class Genome:
    
    def __init__(self, inputs_n, outputs_n):
		"""
		Creates a new Genome with 'inputs_n' input nodes, and 'outputs_n' output nodes,
		AND a single one random connection between two of these nodes
		"""
		# the network is represented by a list of links, ORDERED by their layer.
        self.links   = []
		

		# stores input and output nodes as integers. Since these nodes are constant and 
		# will not change during generations or during mutation, every node with ID < inputs_n		
		# will be an input node, and every node with inputs_n <= ID < outputs_n will be
		# an output node
        self.inputs_n  = inputs_n
		self.outputs_n = outputs_n
		
		# nodes in the net as a set
		nodes = set([i for i in range(inputs_n+outputs_n)])
		
		# fitness of this genome. It's None if it hasn't been evaluated yet
		self.fitness = None
        
        # create only one random link between input and output layer
		# select two random nodes, one for each layer
        n0 = randint(0, inputs_n-1)
        n1 = randint(inputs_n_n-1)
        l  = Link(0, 1, n0, n1, inn numbner gloabl)  #since this layer connects the last layer, its field 'to_link' is not set
		l.bias = 0	#input node has not bias
        self.links.append(l)
    
    
    def _feed_forward(self, inputs):
		assert(len(inputs) == self.inputs_n)
		outputs = [0] * self.outputs_n
		
		# iterate only on first layer links to initialize their input_sums to the inputs provided
		for l in self.links:  
			if l.from_layer > 0:	  #self.links is ordered by layer, so i can break if i find the first layer > 0
				break
			# if the link is on the first layer, its l.from_node should be in range(len(inputs)), which is
			# equal to range(self.inputs_n)
			l.input_sum = inputs[l.from_node]
			
		# feed the rest of the net
		for l in self.links:
			
			if l.to_link == []:	#if its 'to_link' is [], then its 'to_node' is in range(len(outputs))
				outputs[l.to_node]  += (l.input_sum + l.bias) * l.weight
			else:
				x = relu(l.input_sum + l.bias) * l.weight
				map(lambda out_link: out_link.input_sum += x, l.to_link)
		
		# TODO: SOFTMAX OUTPUTS
		
		return outputs

		

    def mutate(self, link_history):
        """
        mutate the genome following Kenneth O. Stanley's paper.
        Doesn't mutate in place, but returns a new mutated genome
        """
        g = deepcopy(self)    #new genome to be muted and returned
        
        if random() < 0.8:    #mutate all weights with 80% prob
            map(lambda link: link.mutate(weight=True), g.links)
		
		if random() < 0.8:	  #mutate all biases with 80% prob
			map(lambda node: link.mutate(bias=True), g.links)
        
        if random() < 0.05:   #add new link with 5% prob
            g.add_link(link_history)
        
        if random() < 0.01:   #add new node with 1% prob
            g.add_node(link_history)
        
        return g
		
		
	def crossover(self, g):
		"""
		Returns a "child" from the genomes 'self' and 'g'
		"""
		gen = Genome()  #create a new genome with only the input and output neurons
		gen.links.clear() #cleares all links
		i1, i2 = 0, 0
		while i1 in range(len(self.links)) or i2 in range(len(self.links)):
		
			l1 = self.links[i1] if i1 in range(len(self.links)) else None
			l2 = g.links[i2]    if i2 in range(len(g.links))    else None
				
			# if only one of them is None we have an excess gene
			if l1 is None:
				gen.links.append(deepcopy(l2))
				i2 += 1
			elif l2 is None:
				gen.links.append(deepcopy(l1))
				i1 += 1
				
			# if innovations number match we have the same gene
			elif l1.innovation_num == l2.innovation_num:
				#same gene, decide to take l1 or l2 with same prob (50%)
				new_link = deepcopy(l1) if random() < 0.5 else deepcopy(l2)
				#if one of them is not enabled, disable it in the child with prob 75%
				if not l1.enabled or not l2.enabled:
					new_link.enabled = False if random() < 0.75 else True
				else:
					new_link.enabled = True
				gen.links.append(new_link)
				i1+=1
				i2+=1
			
			# if one innovation_num is < or > we have a disjoint gene
			elif l1.innovation_num < l2.innovation_num:
				new_link = deepcopy(l1)
				i1 += 1
			else:
				new_link = deepcopy(l2)
				i2 += 1
				
		# sort the new created list of links and return the new genoma
		gen.links.sort(key=lambda l: l.from_layer)
		return gen
        

    # utilities
    def add_link(self, link_history):
        """
        Creates a random link between 2 not connected nodes
        """	
		# todo: if fully connected va tutto a puttane
		
		ok = False
		while not ok:
			# find random nodes
			n1, n2 = sample(self.nodes, 2)
			ok = True
			# check if they are already connected
			for l in self.links:
				if l.connects(n1, n2):
					ok = False
			# check their layers
			layer_n1, layer_n2 = None, None
			for l in self.links:
				if l.from_node == n1:
					layer_n1 = l.from_layer
				if l.from_node == n2:
					layer_n2 = l.from_layer
			
			if layer_n1 == layer_n2:
				ok = False
			if layer_n1 is None or layer_n2 is None:
				raise Exception("didn't find the node in the links")
				
		if layer_n1 > layer_n2:  #swap
			n1, n2 = n2, n1
			layer_n1, layer_n2 = layer_n2, layer_n1
			
		# take the list of links that have n2 as 'from_node'. These will be the
		# to_links of the new link
		out_links = [l for l in self.links if l.from_node == n2]
		
		# create link
		new_link = Link(layer_n1, layer_n2, n1, n2, glob inn num, out_links)
		
		# update out_link to all links pointing to n1
		for l in self.links:
			if l.to_node == n1:
				l.to_link.append(new_link)
				
		self.links.append(new_link)
				
		
		
			
		
				
			
		
        
        
    def add_node(self, link_history):
        """
        Adds a new node by splitting an existing link
        """
		link = choice(self.links)
		
		# if adjacent layer create a new layer in between
		if link.to_layer == link.from_layer +1:	
			for l in self.links:    # scale all links in layer number to_layer to to_layer+1
				if l.from_layer == link.from_layer:
					l.from_layer += 1
		
		new_node = glob node id
		self.nodes.add(new_node)
		l2 = Link(link.from_layer+1, link.to_layer, new_node, link.to_node, glob inn num, link.to_link)
		l1 = Link(link.from_layer, link.from_layer+1, link.from_node, new_node, glob inn num, [l2])
		
		# update all links pointing to l1
		for l in self.links:
			if l.to_node == l1.from_node:
				l.to_link.append(l1)
		
		# finish
		link.enabled = False
		self.links.append(l1)
		self.links.append(l2)
	
		
	
	
    # utilities inutyli        
    def display(self):
        """
        funzione bruzza che stampa a schermo piu o meno come appare la rete
        """
        pass

    def feed_forward(self, inputs):
        output = list(self._feed_forward(inputs))
		map(lambda l: l.input_sum=0, self.links)	#resets input sum of the links
		return output
		
	def get_num_layers(self):
		# self.links is ordered by links' layer
		return self.links[-1].to_layer+1


def relu(x):
    return max(0, x)
    
def sigm(x):
    return 1/(1+exp(-x))




    
    
    
    