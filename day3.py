from day1 import read_one_value_lines
import pandas as pd

columns=['A', 'B','C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'L']
exploded = []

for line in read_one_value_lines('ressources/day3.txt'):
    exploded.append([int(line[i]) for i in range(len(line))])
gamma = ''.join(pd.DataFrame(exploded, columns=columns).mode().values.astype(str).tolist()[0])
epsilon = ''.join('1' if x == '0' else '0' for x in gamma)

print('result part 1: ' + str(int(gamma, 2) * int(epsilon,2)))

## PART 2:
df_o2 = pd.DataFrame(exploded, columns=columns)
df_co2 = pd.DataFrame(exploded, columns=columns)

for column in columns:
    if len(df_o2) < 2:
        break
    mode_o2 = df_o2.mode().max()
    df_o2 = df_o2[df_o2[column] == int(mode_o2[column])]
    print(len(df_o2))
o2 = int(''.join(df_o2.values.astype(str).tolist()[0]),2)

 
for column in columns:
    if len(df_co2) < 2:
        break

    mode_co2 =  df_co2.mode().min()
    thing = 1 if mode_co2[column] == 0 else 0
    df_co2 = df_co2[df_co2[column] == thing]
    print(len(df_co2))
co2 = int(''.join(df_co2.values.astype(str).tolist()[0]), 2)

print(df_o2)
print(df_co2)
print('o2: ' + str(o2))
print('co2: ' + str(co2))
print(o2*co2)
