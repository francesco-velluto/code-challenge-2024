import heapq

# Function to parse input
def parse_input():
    # Parse grid dimensions
    w, h = map(int, input().split())
    
    # Parse tile types and costs
    tile_costs = {}
    for _ in range(10):
        tile_id, cost = input().split()
        tile_costs[tile_id] = int(cost)
    
    # Parse silver point values
    silver_points = {}
    s = int(input())
    for _ in range(s):
        tile_id, value = input().split()
        silver_points[tile_id] = int(value)
    
    return w, h, tile_costs, silver_points

# Function to initialize grid
def initialize_grid(w, h):
    grid = []
    for _ in range(h):
        row = input().split()
        grid.append(row)
    return grid

# Function to find all golden points
def find_golden_points(grid):
    golden_points = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'G':
                golden_points.append((i, j))
    return golden_points

# Function to calculate the score of a path
def calculate_path_score(path, silver_points):
    score = 0
    visited = set()
    for tile in path:
        i, j = tile
        tile_id = grid[i][j]
        if tile in visited:
            score += 2 * silver_points.get(tile_id, 0)
        else:
            score += silver_points.get(tile_id, 0)
            visited.add(tile)
    return score

# Function to perform Dijkstra's Algorithm
def dijkstra(grid, start, tile_costs):
    directions = {
        '3': [(0, 1)],
        '5': [(1, 0)],
        '6': [(0, 1), (1, 0)],
        '7': [(0, 1), (1, 0)],
        '9': [(-1, 0), (1, 0)],
        '96': [(-1, 0), (0, 1)],
        'A': [(-1, 0)],
        'A5': [(-1, 0), (1, 0)],
        'B': [(-1, 0), (0, 1), (0, -1)],
        'C': [(-1, 0), (1, 0)],
        'C3': [(-1, 0), (1, 0)],
        'D': [(-1, 0), (1, 0), (0, 1)],
        'E': [(-1, 0), (1, 0), (0, 1)],
        'F': [(-1, 0), (1, 0), (0, 1)],
    }
    
    pq = [(0, start)]
    visited = set()
    distances = {start: 0}
    
    while pq:
        cost, node = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        
        for di, dj in directions[grid[node[0]][node[1]]]:
            ni, nj = node[0] + di, node[1] + dj
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                new_cost = cost + tile_costs[grid[ni][nj]]
                if (ni, nj) not in distances or new_cost < distances[(ni, nj)]:
                    distances[(ni, nj)] = new_cost
                    heapq.heappush(pq, (new_cost, (ni, nj)))
    
    return distances

# Function to find the minimum cost path from start to all golden points
def find_minimum_paths(grid, golden_points, tile_costs):
    min_paths = {}
    for start in golden_points:
        distances = dijkstra(grid, start, tile_costs)
        for end, cost in distances.items():
            min_paths.setdefault(end, []).append((start, cost))
    return min_paths

# Main function
def main():
    w, h, tile_costs, silver_points = parse_input()
    grid = initialize_grid(w, h)
    golden_points = find_golden_points(grid)
    min_paths = find_minimum_paths(grid, golden_points, tile_costs)
    
    min_cost = float('inf')
    min_score = float('inf')
    
    for end, paths in min_paths.items():
        for start, cost in paths:
            score = calculate_path_score((start, end), silver_points)
            if cost < min_cost or (cost == min_cost and score < min_score):
                min_cost = cost
                min_score = score
                
    final_score = sum(min_score) - min_cost
    print(final_score)

if __name__ == "__main__":
    main()
