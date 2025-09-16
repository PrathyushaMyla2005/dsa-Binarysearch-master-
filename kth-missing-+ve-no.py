'''Kth Missing Positive Number
Problem Statement

You are given a sorted array of positive integers (strictly increasing) and an integer k.
Your task is to find the kth missing positive number.

Step 1: Understand the Problem

The array is sorted and only contains some positive integers.

We want the k-th positive integer that is NOT present in the array.

Example 1:arr = [2, 3, 4, 7, 11]
k = 5
Missing numbers: [1, 5, 6, 8, 9, 10, ...]
The 5th missing = 9

Output → 9'''
from typing import List

# ===============================
# Brute Force Approach
# ===============================
def findKthPositive_bruteforce(arr: List[int], k: int) -> int:
    """
    Brute Force Approach:
    ---------------------
    - Start from number 1 and keep counting missing numbers.
    - If a number is not in arr, reduce k by 1.
    - When k becomes 0, return that number.

    Time Complexity (TC): O(n + k)
    Space Complexity (SC): O(1)
    """
    missing_count = 0    # how many missing numbers we found
    current = 1          # start checking from 1
    i = 0                # pointer for arr

    while True:
        # If current number matches arr[i], skip it (not missing)
        if i < len(arr) and arr[i] == current:
            i += 1
        else:
            # current is missing
            missing_count += 1
            if missing_count == k:   # found kth missing
                return current
        current += 1
arr1 = [2, 3, 4, 7, 11]
print("Brute Force:", findKthPositive_bruteforce(arr1, 5))  # Output: 9
from typing import List

# ===============================
# Optimized Approach (Binary Search)
# ===============================
def findKthPositive_optimized(arr: List[int], k: int) -> int:
    """
    Optimized Approach:
    -------------------
    - Use Binary Search to find the smallest index where missing numbers >= k.
    - Formula: missing(i) = arr[i] - (i + 1)
      (because if no numbers missing until index i, arr[i] should be i+1).
    - After binary search, compute result.

    Time Complexity (TC): O(log n)
    Space Complexity (SC): O(1)
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        missing = arr[mid] - (mid + 1)

        if missing < k:   # need more missing numbers
            left = mid + 1
        else:
            right = mid - 1

    # After loop, left is the position where kth missing lies
    return left + k
arr2 = [2, 3, 4, 7, 11]
print("Optimized:", findKthPositive_optimized(arr2, 5))  # Output: 9
