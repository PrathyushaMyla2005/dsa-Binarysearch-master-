'''Problem Statement (in simple words)

You are given a 2D matrix with these conditions:

Each row is sorted in ascending order.

The first integer of each row is greater than the last integer of the previous row.
(So if you read the matrix row by row, it looks like one big sorted array).

Task: Check if a given target number exists in the matrix.
Return True if it’s found, else False.

🔹 Example
Matrix = [
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 60]
]

Target = 3   → Output: True
Target = 13  → Output: False
'''
def searchMatrix_bruteforce(matrix, target):
    """
    Brute Force Approach:
    ---------------------
    - Just check each element one by one.
    - If any element == target → return True.
    - If after checking all elements, not found → return False.

    Why this approach:
    - Simple and beginner-friendly.
    - Useful first step before optimization.

    Time Complexity (TC): O(m * n)   → we may check all elements
    Space Complexity (SC): O(1)      → no extra memory used
    """
    for row in matrix:              # Loop over each row
        for element in row:         # Loop over each element in the row
            if element == target:   # Compare with target
                return True         # Found
    return False                    # Not found after full scan


# Example usage
matrix1 = [
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 60]
]
print("Brute Force:", searchMatrix_bruteforce(matrix1, 3))   # True
print("Brute Force:", searchMatrix_bruteforce(matrix1, 13))  # False
def searchMatrix_optimal(matrix, target):
    """
    Optimal Approach (Binary Search):
    ---------------------------------
    - Treat matrix as a sorted 1D array of size (m*n).
    - Use binary search on this virtual array.
    - Convert index back into (row, col):
        row = mid // n
        col = mid % n

    Why this approach:
    - Matrix is sorted like a 1D array → binary search is best.
    - Much faster than brute force.

    Time Complexity (TC): O(log(m*n))   → binary search
    Space Complexity (SC): O(1)         → constant space
    """
    if not matrix or not matrix[0]:
        return False  # Handle empty matrix case

    m, n = len(matrix), len(matrix[0])   # rows, cols
    low, high = 0, m * n - 1             # virtual 1D array boundaries

    while low <= high:
        mid = (low + high) // 2          # middle index in 1D array
        row = mid // n                   # map mid to row
        col = mid % n                    # map mid to col
        value = matrix[row][col]         # actual element

        if value == target:
            return True                  # Found target
        elif value < target:
            low = mid + 1                # Search right half
        else:
            high = mid - 1               # Search left half

    return False                         # Not found


# Example usage
matrix2 = [
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 60]
]
print("Optimal:", searchMatrix_optimal(matrix2, 3))   # True
print("Optimal:", searchMatrix_optimal(matrix2, 13))  # False
