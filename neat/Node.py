
class Node:
	
	def __init__(self, id):
		self.id   		  = id
		self.input_sum    = 0
		self.output_sum   = 0
		self.out_links    = []
		