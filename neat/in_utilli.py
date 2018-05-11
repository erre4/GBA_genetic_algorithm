
def relu(x):
    return max(0, x)
    
def sigm(x):
    return 1/(1+exp(-x))
	
	
def display(g, file="net.png"):
	"""
	funzione bruzza che stampa a schermo piu o meno come appare la rete di un genoma
	"""
	try:
		from PIL import Image, ImageDraw
	except ModuleNotFoundError:
		print("Install PIL module to draw images")
		return

	img = Image.new('RGB', (1000, 1000))
	draw = ImageDraw.Draw(img)
	
	
	layers = g.get_num_layers()
	nodes = [[]] * layers
	for l in g.links:
		if not l.from_node in nodes[l.from_layer]:
			nodes[l.from_layer].append(1)
		if not l.to_node in nodes[l.to_layer]:
			nodes[l.to_layer].append(1)
	
	# draw nodes
	square_edge = 10  #10 px
	offset_y, offset_x = 50, 50
	distance_y = 20     #vertical distance
	distance_x = 100    #horizontal distance
	for layer, i in zip(nodes, range(len(nodes))):
		for node, j in zip(layer, range(len(layer))):
			x1 = offset_x + i*(distance_x+square_edge)
			y1 = offset_y + j*(distance_y+square_edge)
			x2 = x1 + square_edge
			y2 = y1 + square_edge
			draw.rectangle((x1, y1), (x2, y2))
			
	# draw connections
	
	### TODO ###
	
	
	
	
	