def explore(grid, y, x):
    """Recursively explores a grid, marking all connected zeroes (0) starting from (y, x)."""

    # Base case: If the current cell is not 0, return (avoid revisiting walls or already visited cells)
    if grid[y][x] != 0:
        return

    # Mark the current cell as visited (2) and print its coordinates
    print("visit", y, x)
    grid[y][x] = 2

    # Recursively explore in all four directions (up, down, left, right)
    explore(grid, y - 1, x)  # Up
    explore(grid, y + 1, x)  # Down
    explore(grid, y, x - 1)  # Left
    explore(grid, y, x + 1)  # Right


# Define a 2D grid where:
# 1 represents walls, 0 represents open spaces to explore.
grid = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

# Start exploring from the position (1,1), which is an open space (0).
explore(grid, 1, 1)

# Print the modified grid to see which cells were visited.
for row in grid:
    print(row)


