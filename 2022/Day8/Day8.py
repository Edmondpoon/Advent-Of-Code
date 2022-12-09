import sys

def part1():
    grid = []
    fd = open(sys.argv[1], 'r')

    while True:
        line = fd.readline()
        if not line:
            break

        grid.append([int(num) for num in line.strip()])

    ROWS = len(grid)
    COLS = len(grid[0])

    visible = (ROWS * 2) + (COLS * 2) - 4
    
    # check cols from top
    for col in range(1, COLS - 1):
        height = grid[0][col]
        for row in range(1, ROWS - 1):
            if grid[row][col] > height:
                height = grid[row][col]
                visible += 1
                grid[row][col] *= -1
            elif grid[row][col] == height:
                pass

    # checks cols from bottom
    for col in range(COLS - 2, 0, -1):
        height = grid[-1][col]
        for row in range(ROWS - 2, 0, -1):
            if grid[row][col] > height:
                height = grid[row][col]
                visible += 1
                grid[row][col] *= -1

            elif grid[row][col] * -1 > height:
                height = grid[row][col] * -1

            elif grid[row][col] == height or grid[row][col] * -1 == height:
                pass

    # checks rows from left
    for row in range(1, ROWS - 1):
        height = grid[row][0]
        for col in range(1, COLS - 1):
            if grid[row][col] > height:
                height = grid[row][col]
                visible += 1
                grid[row][col] *= -1

            elif grid[row][col] * -1 > height:
                height = grid[row][col] * -1

            elif grid[row][col] == height or grid[row][col] * -1 == height:
                pass

    # checks rows from right
    for row in range(ROWS - 2, 0, -1):
        height = grid[row][-1]
        for col in range(COLS - 2, 0, -1):
            if grid[row][col] > height:
                height = grid[row][col]
                visible += 1
                grid[row][col] *= -1

            elif grid[row][col] * -1 > height:
                height = grid[row][col] * -1

            elif grid[row][col] == height or grid[row][col] * -1 == height:
                pass


    return visible 
    


def dfs(grid, row, col):
    score = 1
    
    for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        temp = [row + direction[0], col + direction[1]]
        val = 0
        while -1 < temp[0] < len(grid) and -1 < temp[1] < len(grid[0]) and grid[temp[0]][temp[1]] < grid[row][col]:
            temp[0] += direction[0]
            temp[1] += direction[1]
            val += 1

        if val > 0:
            if -1 < temp[0] < len(grid) and -1 < temp[1] < len(grid[0]):
                val += 1
            score *= val
        else:
            return 0

    return score

    
def part2():
    grid = []
    fd = open(sys.argv[1], 'r')

    while True:
        line = fd.readline()
        if not line:
            break

        grid.append([int(num) for num in line.strip()])

    ROWS = len(grid)
    COLS = len(grid[0])
    
    score = 0

    for row in range(ROWS):
        for col in range(COLS):
            score = max(score, dfs(grid, row, col))

    return score

    
    


score = part1()
print(score)

score = part2()
print(score)
