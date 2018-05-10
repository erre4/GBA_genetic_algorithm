from random import random, gauss


class Node:
    
    def __init__(self, id):
        self.id           = id
        self.input_sum    = 0
        self.output_sum   = 0
		self.bias         = random()*2 -1
        self.out_links    = []
        
	def mutate_bias(self):
		"""
		mutate the bias in place
		"""
		if random() < 0.1:
            self.bias = random()*2 -1
        else:
            self.bias += gauss(0, 1)
            if self.bias > 1:
                self.bias = 1 
            if self.bias < -1:
                self.bias = -1