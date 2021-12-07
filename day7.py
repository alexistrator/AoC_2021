from statistics import mean, median

values = []
with open('ressources/day7.txt') as values_file:
        values = [value.split() for value in values_file]
        final_values = values[0][0].split(',')
        final_values = [int(value) for value in final_values]

final_values.sort()
counter = 0
for value in final_values:
    counter += abs(value-median(final_values))
print(counter)

# Part 2:
counter2 = 0
for value in final_values:
    counter2 += sum(range(abs(value - round(mean(final_values)-1))+1))
print(counter2)