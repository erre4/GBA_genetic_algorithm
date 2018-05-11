#class Game
#initial_population: number of the initiatial population that will be mutated
#total population: number of all the genomes after mutation including initial population

class Game:
    
        def __init__(self,initial_population, total_population, n_inputs, n_outputs):
            
            self.total_population = total_population
            self._initial_population = population
            self.spec = Spec()
            self.genomes = []
            
            for i in range(0,initial_population):
                self.genomes.append(Genome(n_inputs, n_outputs))
            
            
        
        def generate_mutation():
            
            new_mutations = []
            j = 0
            for i in range(0, self.total_population-initial_population):
            
                new_mutations.append(self.genomes[j].mutate())
                
                if(j == self-initial_population -1):
                    j = 0
                else:
                    j += 1
            
            self.genomes += new_mutations
            
            return self.genomes
            
        def rules_game():
            #rules
        
        def play_games():
            #feedforward following rules of the game
            #and computing fitness at same time
        
        def compute_speciations(self):
        
            return self.spec.getSpecies(self.genomes)
            
        def best_genomes(self,species_matrix):
        
            best_matrix = []
            counter = 0
            for i in range(0,len(species_matrix)):
                best_matrix.append([])
                species_matrix[i] = sorted(species_matrix[i], key=operator.attrgetter('fitness'))
                length = len(species_matrix[i])
                    for j in range(0,length):
                        if counter < self.initial_population:
                            best_matrix[i].append(species_matrix[i][length-(j+1)])
                        
                        else:
                            maximum = 0
                            index = -1
                            minimum = 9999999
                            for k in range(0,i):
                                if len(best_matrix[k]) > maximum:
                                    maximum = len(best_matrix[k])
                                    index = k
                                elif len(best_matrix[k]) == maximum:
                                    if best_matrix[k][-1].fitness < best_matrix[index][-1].fitness:
                                        index = k
                                    
                            if(maximum == 1 and len(best_matrix[i]) == 0):        
                                if(species_matrix[i][length-(j+1)].fitness > minimum):
                                    best_matrix[index][0] = []
                                    best_matrix[i].append(species_matrix[i][length-(j+1)])
                                    
                            elif(len(best_matrix[i]) < maximum and species_matrix[i][length-(j+1)].fitness > best_matrix[index][-1].fitness):
                                best_matrix[index] = best_matrix[0:len(best_matrix[index])]
                                best_matrix[i].append(species_matrix[i][length-(j+1)])
            
            self.genomes = []
            length = len(best_matrix)
            for i in range(0,length):
                length2 = len(best_matrix[i])
                for j in range(0,length2):
                    self.genomes.append(best_matrix[i][j])
                    
            return self.genomes
                
            
