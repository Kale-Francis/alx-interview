# 0x01. Lockboxes

## Project Overview

This project focuses on a classic algorithmic problem involving graph traversal, often referred to as the "Lockboxes Problem". The core challenge is to determine if it's possible to open all `n` locked boxes, given that you start with the first box (box `0`) unlocked, and each box may contain keys to other boxes.

This problem serves as an excellent exercise in applying fundamental data structures and search algorithms to solve a practical connectivity problem.

## Concepts Explored

To successfully tackle this project, a solid understanding of the following concepts was crucial:

* **Graph Traversal (BFS/DFS):** The problem can be modeled as a graph where boxes are nodes and keys are directed edges. The goal is to check if all nodes are reachable from a starting node (box 0).
    * **Breadth-First Search (BFS):** This project's solution primarily utilizes a BFS-like approach, exploring all directly reachable boxes before moving to the next "layer" of boxes. This is achieved by maintaining a queue of keys to process.
    * **Depth-First Search (DFS):** An alternative approach, often implemented recursively or with an explicit stack.
* **Lists and List Manipulation:** Essential for representing the `boxes` structure and for dynamically managing the `keys_available` (queue/stack).
* **Sets:** Crucial for efficient tracking of `opened_boxes`. Sets provide `O(1)` average time complexity for adding elements and checking for existence, which is vital for preventing redundant processing and infinite loops in graph traversal.
* **Algorithmic Complexity (Big O Notation):** While not explicitly implemented in the code, understanding how to optimize for time complexity was key. The chosen BFS approach ensures that each box and key is processed at most once, leading to an efficient solution.

## Project Structure

The project directory `0x01-lockboxes` contains the following files:

* **`0-lockboxes.py`**: Contains the core logic for the `canUnlockAll` function. This is the main solution file for the project.
* **`main_0.py`**: A testing script provided by the project to verify the `canUnlockAll` function's behavior with various test cases. (Note: This is usually run from the terminal to check output).
* **`README.md`**: This file, providing an overview and documentation for the project.

## How to Run (Testing)

1.  **Navigate to the project directory:**
    ```bash
    cd alx-backend-javascript/0x01-lockboxes
    ```
2.  **Ensure files are executable:**
    ```bash
    chmod +x 0-lockboxes.py
    chmod +x main_0.py
    ```
3.  **Run the main test script:**
    ```bash
    ./main_0.py
    ```

## Example Usage and Expected Output

Running `main_0.py` will produce output similar to the following, demonstrating the function's ability to correctly determine if all boxes can be opened:

```bash
carrie@ubuntu:~/0x01-lockboxes$ ./main_0.py
True
True
False
Solution Approach (0-lockboxes.py)
The canUnlockAll function implements a Breadth-First Search (BFS) algorithm to traverse the boxes and collect keys.

Initialization:

num_boxes: Stores the total count of boxes to be opened.
opened_boxes (a set): Keeps track of all unique box indices that have been successfully opened. It starts with 0 as the initial unlocked box.
keys_available (a list used as a queue): Stores keys found in opened boxes that still need to be processed. It's initialized with all keys found in boxes[0].
Traversal Loop:

The while keys_available: loop continues as long as there are new keys to process.
In each iteration, a current_key is pop()ed from the front of the keys_available list (mimicking a queue).
Validation: It checks if current_key is a valid box index (within 0 and num_boxes - 1) and if the corresponding box has not been opened_boxes yet.
Unlocking and Collecting: If a key is valid and leads to a new, unopened box:
The current_key is added to opened_boxes.
All keys found inside boxes[current_key] are extend()ed into keys_available to be processed in subsequent iterations.
Final Determination:

After the loop finishes (meaning no more new boxes can be reached with the available keys), the function compares the number of boxes in opened_boxes with num_boxes.
If len(opened_boxes) == num_boxes, it means all boxes were successfully opened, and True is returned. Otherwise, False is returned.
This approach ensures that each box is processed at most once, providing an efficient solution to the problem.

Author
Kale-Francis
 https://github.com/Kale-Francis
 