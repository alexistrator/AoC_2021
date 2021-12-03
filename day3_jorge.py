def get_most_common_bits(arr):
    count = len(arr)
    item_size = len(arr[0])
    result = [0 for _ in range(item_size)]
    for line in arr:
        for i in range(item_size):
            result[i] += int(line[i])

    return ''.join(("0" if x < count / 2 else "1" for x in result))


def day3_2():
    with open("ressources/day3.txt") as file:
        data = [x.rstrip() for x in file]
        nr_of_bits = len(data[0])

        oxygen_values = data.copy()
        for i in range(nr_of_bits):
            most_common_bits = get_most_common_bits(oxygen_values)
            oxygen_values = [x for x in oxygen_values if x[i] == most_common_bits[i]]
            if len(oxygen_values) == 1:
                break

        for i in range(nr_of_bits):
            most_common_bits = get_most_common_bits(data)
            data = [x for x in data if x[i] != most_common_bits[i]]
            if len(data) == 1:
                break

        oxygen = int(''.join(oxygen_values), 2)
        co2 = int(''.join(data[0]), 2)
        print(data[0]) 
        print(oxygen)
        print(co2)
        print(oxygen * co2)


if __name__ == '__main__':
    day3_2()
