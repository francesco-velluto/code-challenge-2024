# Function to generate all possible paths
def generate_paths(grid, start, end, visited, path, paths):
    visited.add(start)
    if start == end:
        paths.append(path)
    else:
        for neighbor, tile_id in grid[start]:
            if neighbor not in visited:
                generate_paths(grid, neighbor, end, visited.copy(), path + [(neighbor, tile_id)], paths)

# Function to process the input data and find the optimal path
def find_optimal_path(W, H, GN, SM, TL, golden_points, silver_points, tiles):
    print("Parsing input...")
    grid = {}
    for i in range(W):
        for j in range(H):
            neighbors = []
            for tile, cost, tile_id in tiles:
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
                new_x, new_y = i + dx, j + dy
                if within_bounds((new_x, new_y), W, H):
                    neighbors.append(((new_x, new_y), tile_id))
            grid[(i, j)] = neighbors

    paths = []
    print("Generating paths...")
    for start in golden_points:
        for end in golden_points:
            if start != end:
                generate_paths(grid, start, end, set(), [(start, None)], paths)

    min_cost = float('inf')
    min_score = float('inf')
    optimal_path = None

    print("Finding optimal path...")
    for path in paths:
        cost = 0
        visited = set()
        for i in range(len(path) - 1):
            cost += dijkstra(grid, path[i][0], path[i + 1][0])
        score = calculate_score([point for point, _ in path], silver_points)
        if cost < min_cost or (cost == min_cost and score < min_score):
            min_cost = cost
            min_score = score
            optimal_path = path

    return optimal_path

# Function to write output to file
def write_output(file_name, path):
    with open(file_name, 'w') as f:
        for point, tile_id in path:
            f.write(f"{tile_id} {point[0]} {point[1]}\n")
    print("Output written to", file_name)
