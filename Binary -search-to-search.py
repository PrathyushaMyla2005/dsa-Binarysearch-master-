'''Problem Statement

You are given:

A sorted array (in ascending order).

A target value X.

👉 Task: Find the index of X in the array. If not found, return -1.

2. Example
Input: arr = [1, 3, 7, 9, 11, 12, 45], X = 11
Output: 4
Explanation: 11 is at index 4 (0-based indexing).
Best Case: O(1) → Found at first mid.

Worst Case: O(log n) → Keep halving until done.

Space Complexity: O(1).'''
def binary_search(arr, X):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # middle index

        if arr[mid] == X:
            return mid  # found
        elif arr[mid] < X:
            low = mid + 1  # move right
        else:
            high = mid - 1  # move left

    return -1  # not found


# Example usage
arr = [1, 3, 7, 9, 11, 12, 45]
X = 11
print(binary_search(arr, X))  # Output: 4
#. Optimal Python Code
'''ime Complexity:

Best case: O(1) (if found at first middle)

Worst case: O(log n) (keep halving until found)

Space Complexity:

Iterative: O(1)

Recursive: O(log n) (due to function call stack)

👉 Iterative method is optimal.'''
def binary_search(arr, X):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2  # middle index
        
        if arr[mid] == X:        # element found
            return mid
        elif arr[mid] < X:       # search right half
            low = mid + 1
        else:                    # search left half
            high = mid - 1
    
    return -1  # element not found


# Example
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
X = 23
print(binary_search(arr, X))  # Output: 5

