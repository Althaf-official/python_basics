import random

# Define the dimensions of the maze
WIDTH = 10
HEIGHT = 10

# Define the possible directions
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Initialize the maze grid
maze = [['#' for _ in range(WIDTH)] for _ in range(HEIGHT)]

# Recursive backtracking algorithm to generate the maze
def generate_maze(x, y):
    maze[y][x] = ' '  # Mark the current cell as visited

    random.shuffle(directions)
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < WIDTH and 0 <= ny < HEIGHT and maze[ny][nx] == '#':
            mx, my = x + dx // 2, y + dy // 2
            maze[my][mx] = ' '  # Mark the cell between the current and next cell as visited
            generate_maze(nx, ny)

# Solve the maze using recursive backtracking
def solve_maze(x, y):
    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or maze[y][x] != ' ':
        return False  # Out of bounds or not a valid path

    if x == WIDTH - 1 and y == HEIGHT - 1:
        maze[y][x] = 'E'  # Mark the exit of the maze
        return True

    maze[y][x] = '*'  # Mark the current path

    # Try all possible directions
    random.shuffle(directions)
    for dx, dy in directions:
        if solve_maze(x + dx, y + dy):
            return True

    maze[y][x] = ' '  # Dead end, backtrack
    return False

# Generate and solve the maze
generate_maze(0, 0)
solve_maze(0, 0)

# Print the maze
for row in maze:
    print(' '.join(row))
