import heapq

# Parse input file
def parse_input(file_name):
    with open(file_name, 'r') as f:
        W, H, GN, SM, TL = map(int, f.readline().split())
        golden_points = [tuple(map(int, f.readline().split())) for _ in range(GN)]
        silver_points = [tuple(map(int, f.readline().split())) for _ in range(SM)]
        tiles = [(line.split()[0], int(line.split()[1]), int(line.split()[2])) for line in f.readlines()]
    return W, H, GN, SM, TL, golden_points, silver_points, tiles

# Function to calculate the distance between two points
def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# Function to check if a point is within grid bounds
def within_bounds(point, W, H):
    return 0 <= point[0] < W and 0 <= point[1] < H

# Dijkstra's algorithm to find the shortest path
def dijkstra(grid, start, end):
    queue = [(0, start)]
    visited = set()
    distances = {start: 0}
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if current_vertex == end:
            return distances[end]
        if current_vertex in visited:
            continue
        visited.add(current_vertex)
        for neighbor, weight in grid[current_vertex]:
            distance = current_distance + weight
            if distance < distances.get(neighbor, float('inf')):
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return float('inf')

# Function to generate all possible paths
def generate_paths(grid, start, end, visited, path, paths):
    visited.add(start)
    if start == end:
        paths.append(path)
    else:
        for neighbor, _ in grid[start]:
            if neighbor not in visited:
                generate_paths(grid, neighbor, end, visited.copy(), path + [neighbor], paths)

# Function to calculate the score of a path
def calculate_score(path, silver_points):
    score = 0
    visited = set()
    for point in path:
        if point in silver_points and point not in visited:
            score += silver_points[point]
            visited.add(point)
    return score

# Function to process the input data and find the optimal path
def find_optimal_path(W, H, GN, SM, TL, golden_points, silver_points, tiles):
    print("Parsing input...")
    grid = {}
    for i in range(W):
        for j in range(H):
            neighbors = []
            for tile, cost, _ in tiles:
                dx, dy = 0, 0
                if '3' in tile:
                    dx += 1
                if '5' in tile:
                    dy += 1
                if '6' in tile:
                    dx += 1
                    dy -= 1
                if '7' in tile:
                    dx += 1
                    dy += 1
                if '9' in tile:
                    dx -= 1
                    dy += 1
                if '6' in tile:
                    dx -= 1
                if 'A' in tile:
                    dx -= 1
                    dy -= 1
                if 'A5' in tile:
                    dx -= 1
                    dy += 1
                if 'B' in tile:
                    dx -= 1
                    dy -= 1
                if 'C' in tile:
                    dy -= 1
                if 'C3' in tile:
                    dx += 1
                    dy -= 1
                if 'D' in tile:
                    dx += 1
                if 'E' in tile:
                    dx += 1
                    dy -= 1
                    dy += 1
                if 'F' in tile:
                    dx += 1
                    dy -= 1
                    dy += 1
                    dy += 1
                new_x, new_y = i + dx, j + dy
                if within_bounds((new_x, new_y), W, H):
                    neighbors.append(((new_x, new_y), cost))
            grid[(i, j)] = neighbors

    paths = []
    print("Generating paths...")
    for start in golden_points:
        for end in golden_points:
            if start != end:
                generate_paths(grid, start, end, set(), [start], paths)

    min_cost = float('inf')
    min_score = float('inf')
    optimal_path = None

    print("Finding optimal path...")
    for path in paths:
        cost = 0
        visited = set()
        for i in range(len(path) - 1):
            cost += dijkstra(grid, path[i], path[i + 1])
        score = calculate_score(path, silver_points)
        if cost < min_cost or (cost == min_cost and score < min_score):
            min_cost = cost
            min_score = score
            optimal_path = path

    return optimal_path

# Function to write output to file
def write_output(file_name, path):
    with open(file_name, 'w') as f:
        for tile in path:
            f.write(f"{tile[0]} {tile[1]} {tile[2]}\n")
    print("Output written to", file_name)

# Main function
def main():
    input_file = "input.txt"
    output_file = "output.txt"

    print("Parsing input file...")
    W, H, GN, SM, TL, golden_points, silver_points, tiles = parse_input(input_file)

    optimal_path = find_optimal_path(W, H, GN, SM, TL, golden_points, dict(zip(silver_points, [score for _, _, score in silver_points])), tiles)

    write_output(output_file, optimal_path)

if __name__ == "__main__":
    main()
