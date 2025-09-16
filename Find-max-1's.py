'''Problem Statement

You are given a binary matrix — a 2D array where each element is either 0 or 1.

Rows are sorted in non-decreasing order (all 0s appear before 1s in each row).

Task: Find the row index (0-based) that contains the maximum number of 1s.

Example
matrix = [
  [0, 0, 1, 1],  # row 0 → 2 ones
  [0, 1, 1, 1],  # row 1 → 3 ones ✅ maximum
  [0, 0, 0, 1]   # row 2 → 1 one
]


Row 0 → 2 ones

Row 1 → 3 ones → maximum

Row 2 → 1 one

Answer: 1 (row index with maximum 1s)'''
from typing import List

# ===============================
# Brute Force Approach
# ===============================
def rowWithMaxOnes_bruteforce(matrix):
    """
    Brute Force Approach:
    ---------------------
    - Loop through each row.
    - Count the number of 1s in that row using sum().
    - Keep track of the row with the maximum number of 1s.

    Time Complexity (TC): O(n * m) → n = number of rows, m = number of columns
    Space Complexity (SC): O(1)
    """
    max_ones = 0      # stores maximum number of 1s seen so far
    row_index = -1    # stores row index with maximum 1s

    for i, row in enumerate(matrix):  # loop through each row
        count = sum(row)               # count number of 1s in this row
        if count > max_ones:           # if current row has more 1s than previous maximum
            max_ones = count           # update max_ones
            row_index = i              # update row_index

    return row_index                  # return index of row with maximum 1s


# Example usage
matrix1 = [
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 1]
]
print("Brute Force:", rowWithMaxOnes_bruteforce(matrix1))  # Output: 1


# ===============================
# Optimized Approach (O(n + m))
# ===============================
def rowWithMaxOnes_optimized(matrix):
    """
    Optimized Approach:
    -------------------
    - Start from the top-right corner of the matrix.
    - Move left if the current element is 1 (maybe more 1s in this row).
    - Move down if the current element is 0 (move to next row).
    - Keep track of the row where we last moved left (this row has more 1s).

    Time Complexity (TC): O(n + m) → n = rows, m = columns
    Space Complexity (SC): O(1)
    """
    n = len(matrix)
    m = len(matrix[0])
    i = 0          # start at first row
    j = m - 1      # start at last column
    max_row = -1   # stores row with maximum 1s

    while i < n and j >= 0:
        if matrix[i][j] == 1:   # found a 1
            max_row = i         # update max_row to current row
            j -= 1              # move left to check for more 1s
        else:                   # found a 0
            i += 1              # move down to next row

    return max_row


# Example usage
matrix2 = [
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 1]
]
print("Optimized:", rowWithMaxOnes_optimized(matrix2))  # Output: 1
