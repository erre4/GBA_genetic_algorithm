import operator

#speed_v is an array of len = number of victories each element i is the speed of the victory i (number of calls of the genomes to win)
#speed_l is an array of len = number of losses each element i is the speed of the victory i (number of calls of the genomes to win)
def fitness(speed_v, speed_l):
    v_sum = 0
    l_sum = 0
    for i in range(0,len(speed_v):
        v_sum += speed_v[i]
        
    for i in range(0,len(speed_l):
        l_sum += speed_l[i]
    
    return (len(speed_v)*v_sum - len(speed_l)*l_sum)/(v_sum*l_sum)
    


def adjusted_fitness(species_matrix):
    for i in range(0,len(species_matrix)):
        for j in range(0,len(species_matrix[i])):
            species_matrix[i][j].fitness /= len(species_matrix[i])

    return species_matrix


def best_genomes(remaining_genomes, species_matrix):
    best_matrix = []
    counter = 0
    for i in range(0,len(species_matrix)):
        best_matrix.append([])
        species_matrix[i] = sorted(species_matrix[i], key=operator.attrgetter('fitness'))
        length = len(species_matrix[i])
            for j in range(0,length):
                if counter < remaining_genomes:
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
                            if best_matrix[k][len(best_matrix[k])-1].fitness < best_matrix[index][len(best_matrix[index])-1].fitness:
                                index = k
                            
                    if(maximum == 1 and len(best_matrix[i]) == 0):        
                        if(species_matrix[i][length-(j+1)].fitness > minimum):
                            best_matrix[index][0] = []
                            best_matrix[i].append(species_matrix[i][length-(j+1)])
                            
                    elif(len(best_matrix[i]) < maximum and species_matrix[i][length-(j+1)].fitness > best_matrix[index][len(best_matrix[index])-1].fitness):
                        best_matrix[index] = best_matrix[0:len(best_matrix[index])]
                        best_matrix[i].append(species_matrix[i][length-(j+1)])
