def population_change(filename):
    population_data = {}

    with open(filename, 'r') as f:
        for line in f:
            country, year, population = line.strip().split(',')
            year = int(year)
            population = int(population)

            if country not in population_data:
                population_data[country] = []

            population_data[country].append(population)

    population_change = {}

    for country, data in population_data.items():
        if len(data) > 1:
            population_change[country] = data[-1] - data[0]

    return population_change

print(population_change("text.txt"))