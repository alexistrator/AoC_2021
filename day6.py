from day1 import read_one_value_lines

values = [int(v) for v in read_one_value_lines('ressources/day6.txt')[0].split(',')]

def growing_population(periods:int):
    population_over_time = []
    population_over_time.append(values)
    for p in range(periods):
        prev_period = population_over_time[p].copy()
        next_period = []
        for value in prev_period:
            value -= 1
            if value >= 0:
                next_period.append(value)
            else:
                next_period.append(6)
                next_period.append(8)
        print(len(next_period) - len(prev_period))
        population_over_time.append(next_period)
    
    return population_over_time

# part 2
# thx benny

def growing_population_big(periods:int):
    population = [values.count(i) for i in range(9)]
    for period in range(periods):
        new_pop=[0]*9
        for i in range(len(population)):
            new_pop[(i-1)%9] = population[i]
        new_pop[6] += new_pop[8]
        population = new_pop
    return sum(population)
            
            
        

        

     

print(growing_population_big(256))
