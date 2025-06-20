#!/usr/bin/python3
"""
0-island_perimeter
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.
    
    Args:
        grid (list): List of lists of integers where 0 is water and 1 is land
        
    Returns:
        int: Perimeter of the island
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # If cell is land
                # Check all 4 sides of the current land cell
                # Add 1 to perimeter for each adjacent water cell or boundary
                
                # Check up
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                    
                # Check down
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1
                    
                # Check left
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                    
                # Check right
                if j == cols-1 or grid[i][j+1] == 0:
                    perimeter += 1
                    
    return perimeter
