
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
