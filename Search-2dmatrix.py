'''You are given a 2D matrix (a grid of numbers) and a target value.
You need to check if the target exists in the matrix.

Step 1: Understand the matrix properties

Each row of the matrix is sorted in ascending order (from left to right).
Example: [1, 3, 5, 7] → numbers increase as you go right.

Each column is also sorted in ascending order top to bottom (sometimes, in some variations).

For some versions of the problem, the matrix may have all rows concatenated as a sorted 1D array.
Example:

matrix = [
  [1, 3, 5],
  [7, 9, 11],
  [13, 15, 17]
]


Reading row by row, it becomes: [1, 3, 5, 7, 9, 11, 13, 15, 17]

This helps us do a binary search on the entire matrix.

Step 2: Understand the target

You are given a number target (e.g., 9) and you need to return true if it exists in the matrix, or false if it does not.

Step 3: Example
Input:
matrix = [
  [1, 4, 7, 11],
  [2, 5, 8, 12],
  [3, 6, 9, 16],
  [10, 13, 14, 17]
]
target = 5

Output:
true'''
from typing import List

def search_bruteforce(matrix1,target):
    """
    Brute Force Approach:
    ---------------------
    - Loop through each row.
    - Check if the target exists in that row using 'in'.
    
    Time Complexity (TC): O(n * m) → n = rows, m = columns
    Space Complexity (SC): O(1)
    """
    for row in matrix1:
        if target in row:
            return True
    return False

# Example usage
matrix1 = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]
print("Brute Force:", search_bruteforce(matrix1, 9))   # Output: True
print("Brute Force:", search_bruteforce(matrix1, 8))   # Output: False
from typing import List

def search_optimized(matrix,target):
    """
    Optimized Approach:
    -------------------
    - Start from the top-right corner of the matrix.
    - Move left if current element > target.
    - Move down if current element < target.
    - Return True if found, else False.
    """

    # Step 1: Check if matrix is empty or has empty rows
    if not matrix or not matrix[0]:
        return False  # No elements to search

    # Step 2: Get number of rows and columns
    n = len(matrix)       # Total number of rows
    m = len(matrix[0])    # Total number of columns

    # Step 3: Start from top-right corner
    i = 0         # row index → start from first row
    j = m - 1     # column index → start from last column

    # Step 4: Loop until we go out of matrix bounds
    while i < n and j >= 0:

        # Step 4a: Check if current element equals target
        if matrix[i][j] == target:
            return True   # Target found

        # Step 4b: Current element is bigger than target
        elif matrix[i][j] > target:
            j -= 1        # Move left to smaller elements in the row

        # Step 4c: Current element is smaller than target
        else:
            i += 1        # Move down to larger elements in the column

    # Step 5: Target not found in entire matrix
    return False
matrix = [
    [1, 3, 5, 7],
    [8, 10, 12, 14],
    [15, 17, 19, 21]
]

print(search_optimized(matrix, 12))  # True → found
print(search_optimized(matrix, 6))   # False → not found
