import random

def random_grid(n_cols, n_rows, letters="ROGBY#"):
	cols = []
	for col_n in range(n_cols):
		row = []
		for row_n in range(n_rows):
			row.append(random.choice(letters))
		cols.append(row)
	return cols
	
def area_size(grid, col, row):
	visited = set()
	unvisited = [(col, row)]
	while len(unvisited) > 0:
		current = unvisited.pop()
		visited.add(current)
		x, y = current
		if x > 0 and grid[x-1][y] == grid[x][y] and (x - 1, y) not in visited:
			unvisited.append((x - 1, y))
		if x < len(grid) - 1 and grid[x + 1][y] == grid[x][y] and (x + 1, y) not in visited:
			unvisited.append((x + 1, y))
		if y > 0 and grid[x][y - 1] == grid[x][y] and (x, y - 1) not in visited:
			unvisited.append((x, y - 1))
		if y < len(grid[0]) - 1 and grid[x][y + 1] == grid[x][y] and (x, y + 1) not in visited:
			unvisited.append((x, y + 1))
	return len(visited)
		
def print_grid(grid):
	for y in range(len(grid[0])):
		print ''.join([x[y] for x in grid])
		
		
g = random_grid(10, 10)

print_grid(g)
