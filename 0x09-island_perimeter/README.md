0x09. Island Perimeter
Project Overview
This project, part of the ALX Interview preparation, focuses on solving the "Island Perimeter" problem using Python. The task is to create a function that calculates the perimeter of a single island in a grid, where the grid is represented as a 2D list of integers. The grid consists of 0s (representing water) and 1s (representing land), with the island being a connected group of land cells surrounded by water.
The goal is to compute the perimeter by counting the number of exposed edges of land cells, where an edge is exposed if it is adjacent to a water cell or lies on the grid's boundary. This project tests algorithmic thinking, 2D array manipulation, and conditional logic.
Requirements

Environment: Ubuntu 20.04 LTS using Python 3 (version 3.4.3)
Editors: vi, vim, or emacs
File Format:
All files must end with a newline.
The first line of Python files must be #!/usr/bin/python3.
Code must follow PEP 8 style (version 1.7).
Files must be executable.


Constraints:
No external modules can be imported.
All functions must be documented.
The grid is rectangular, with width and height not exceeding 100.
The grid is completely surrounded by water.
There is only one island, with no "lakes" (water inside the island not connected to the surrounding water).



Task Description
0. Island Perimeter

File: 0-island_perimeter.py
Objective: Implement a function def island_perimeter(grid): that returns the perimeter of the island in the given grid.
Grid Description:
0 represents a water cell.
1 represents a land cell.
Each cell is a square with a side length of 1.
Cells are connected horizontally or vertically (not diagonally).


Output: The function returns an integer representing the total perimeter of the island, calculated by summing the exposed edges of all land cells.

Example
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

Running the function with this grid returns 12, as the island's perimeter is the sum of all exposed edges of the land cells.
Repository Structure

GitHub Repository: alx-interview
Directory: 0x09-island_perimeter
Files:
0-island_perimeter.py: Contains the implementation of the island_perimeter function.
README.md: This file, providing an overview of the project.



How It Works
The island_perimeter function:

Iterates through each cell in the grid using nested loops.
For each land cell (1), checks its four adjacent sides (up, down, left, right).
Adds 1 to the perimeter for each side that is either:
Adjacent to a water cell (0), or
On the grid's boundary (e.g., top edge where i == 0).


Returns the total perimeter.

Usage

Save the code in 0-island_perimeter.py.
Ensure the file is executable (chmod +x 0-island_perimeter.py).
Test the function using a main file, such as:#!/usr/bin/python3
island_perimeter = __import__('0-island_perimeter').island_perimeter
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Output: 12


Run the script: ./main.py.

Author
[Kale Franis]
License
This project is part of the ALX Interview preparation and is provided for educational purposes.
