import itertools
import time
import xlwt

def calculate_distance(path, distances):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distances[path[i]][path[i + 1]]
    total_distance += distances[path[-1]][path[0]]  # Return to the starting city
    return total_distance

def tsp_bruteforce(distances):
    num_cities = len(distances)
    shortest_path = None
    shortest_distance = float('inf')

    # Generate all possible permutations of cities
    all_paths = itertools.permutations(range(num_cities))

    # Iterate through all permutations and calculate distances
    for path in all_paths:
        distance = calculate_distance(path, distances)
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_path = path

    return shortest_path, shortest_distance

def read_distance_matrix(filename):
    with open(filename, 'r') as file:
        num_cities = int(file.readline())
        distances = [[int(x) for x in line.split()] for line in file]
        return num_cities, distances

def save_to_excel(num_cities, average_time, output_file):
    book = xlwt.Workbook()
    sheet = book.add_sheet('TSP Results')

    sheet.write(0, 0, 'Number of Cities')
    sheet.write(0, 1, 'Average Time (seconds)')

    sheet.write(1, 0, num_cities)
    sheet.write(1, 1, average_time)

    book.save(output_file)

if __name__ == "__main__":
    filename = "cities.txt"
    num_cities, distances = read_distance_matrix(filename)

    num_runs = 10
    total_time = 0.0

    for i in range(num_runs):
        start_time = time.time()
        tsp_bruteforce(distances)
        end_time = time.time()
        total_time += (end_time - start_time)

    average_time = total_time / num_runs

    print("Number of cities:", num_cities)
    print("Average time over", num_runs, "runs:", average_time, "seconds")

    output_file = "tsp_results.xls"
    save_to_excel(num_cities, average_time, output_file)
    print("Results saved to", output_file)
