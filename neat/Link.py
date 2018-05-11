from random import random, gauss

class Link:
    
    def __init__(self, from_layer, to_layer, from_node, to_node, innovation_num, to_link=[]):
		"""
		Create a new link between nodes 'from_node' and 'to_node'. field 'to_link'
		can be [] if this link conncects to an output node
		"""
		assert(from_layer < to_layer)
		# this link goes to 'to_link'
		self.to_link        = to_link 
		self.from_node      = from_node
		self.to_node        = to_node
        self.weight         = random()*2 -1
		self.bias           = random()*2 -1  #'from_node''s bias
		self.from_layer     = from_layer  #layer where is located the 'from_node'
		self.to_layer       = to_layer
		# input sum of the links in the previous layers. This sum will be activate
		# by an activation function and will be written in the 'to_link' input_sum
		self.input_sum	    = 0
        self.enabled        = True
        self.innovation_num = innovation_num 
		
    
	def mutate(self, weight=False, bias=False):
        """
        mutate weight and/or bias in place, following the paper
        """
		if mutate_weight:
			if random() < 0.1:
				self.weight = random()*2 -1
			else:
				self.weight += gauss(0, 1)
				if self.weight > 1:
					self.weight = 1 
				if self.weight < -1:
					self.weight = -1
				
		if mutate_bias:
			if random() < 0.1:
				self.bias = random()*2 -1
			else:
				self.bias += gauss(0, 1)
				if self.bias > 1:
					self.bias = 1 
				if self.bias < -1:
					self.bias = -1
				
				
	def connects(self, n1, n2):
		"""
		true if this link connects n1 and n2
		"""
		return (self.from_node==n1 and self.to_node==n2) or
				(self.from_node==n2 and self.to_node==n1)
                
    def same_nodes(self, l):
        """
        true if they link the same nodes
        """
        return l.from_node == self.from_node and
               l.to_node   == self.to_node
			   
    def same_inn_num(self, l):
		"""
		true if the links have the same innovation number
		"""
		return self.innovation_num == l.innovation_num