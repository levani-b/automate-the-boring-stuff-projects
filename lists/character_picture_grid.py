

def main():
    grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
    

    rotated_grid = []
    num_rows = len(grid)
    num_cols = len(grid[0])

    
    for col in range(num_cols):
        new_row = []
        for row in range(num_rows - 1, -1, -1):  
            new_row.append(grid[row][col])
        rotated_grid.append(new_row)

    
    for row in rotated_grid:
        for cell in row:
            print(cell, end="")
        print()  

if __name__ == "__main__":
    main()
