class Spec:

    def __init__(self):
        
        self.c1 = 1.0
        self.c2 = 1.0
        self.c3 = 0.4
        self.thereshold = 3.0

    def getDisjoint(link_i,link_j):

        len_i = len(link_i)
        len_j = len(link_j)
        disjoint = 0

        if(link_i[-1].innovation_num > link_j[-1].innovation_num):
            j = 0
            
            for i in range(0,len_j):
                
                if(link_j[i].innovation_num > link_i[j].innovation_num):
                    disjoint += 1
                    j += 1

                elif(link_j[i].innovation_num < link_i[j].innovation_num):
                    disjoint += 1
                else:
                    j+=1
                
        elif(link_j[-1].innovation_num > link_i[-1].innovation_num):

            j = 0
            
            for i in range(0,len_i):
                
                if(link_i[i].innovation_num > link_j[j].innovation_num):
                    disjoint += 1
                    j += 1

                elif(link_i[i].innovation_num < link_j[j].innovation_num):
                    disjoint += 1
                else:
                    j+=1

        return disjoint
    
    def getExcess(link_i,link_j):

        len_i = len(link_i)
        len_j = len(link_j)
        excess = 0
        
        if(link_i[-1].innovation_num > link_j[-1].innovation_num):

            for i in range(0,len_i):
                if(link_i[len_i-(i+1)].innovation_num > link_j[-1].innovation_num):
                    exces+=1
                else:
                    break
                
        elif(link_j[-1].innovation_num > link_i[-1].innovation_num):

            for i in range(0,len_j):
                if(link_j[len_j-(i+1)].innovation_num > link_i[-1].innovation_num):
                    exces+=1
                else:
                    break

        return excess

    def getWAvarage(link_i,link_j):
        len_i = len(link_i)
        len_j = len(link_j)
        avarage = 0

        max_len = max(len_i,len_j)
        
        for i in range(0,max_len):
            if(i < len_i):
                avarage += link_i[i].weight
            if(i < len_j):
                avarage += link_j[i].weight

        avarage /= (len_i+len_j)

        return avarage

    def getMaxSize(link_i,link_j):
        
        max_len = max(len(link_i),len(link_j))
        return max_len
    
    def getSpecies(self, genomes):

        matrix = []
        length = len(genomes)
        places = [0] * length
        counter = 0

        for i in range(0,length-1):
            for j in range(i+1, length):
                excess = self.getExcess(genomes[i].links,genomes[j].links)
                disjoint = self.getDisjoint(genomes[i].links,genomes[j].links)
                w = self.getWAvarage(genomes[i].links,genomes[j].links)
                n = self.getMaxSize(genomes[i].links,genomes[j].links)
                delta = self.c1*excess/n + self.c2*disjoint/n +self.c3*w
                if(delta < self.thereshold and places[j] == 0):
                    if(places[i] == 0):
                        counter += 1
                        places[i] = counter
                        places[j] = counter
                        matrix.append([genomes[i],genomes[j])
                    else:
                        places[j] = places[i]
                        matrix[places[i]-1].append(genomes[j])
				
				elif(delta > self.thereshold and j == length-1):
					if(places[i] == 0):
                        counter += 1
                        places[i] = counter
                        matrix.append([genomes[i])
						
		return matrix
		
	
	def setC1(self,var):
		
		self.c1 = var
	
	def setC2(self,var):
		
		self.c2 = var
	
	def setC3(self,var):
	
		self.c3 = var
	
	def setThereshold(self,var):
	
		self.thereshold = var
                                      


    
