"""
Problem: Search in Rotated Sorted Array I

An array of integers `nums` is sorted in ascending order but rotated at some pivot.
A target integer `target` is given.

Task: Find the index of the target in the array.
If the target does not exist, return -1.

Example:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
"""

# ---------------- Brute Force Approach ----------------
def search_brute(nums, target):
    """
    Brute force approach:
    - Scan the array from start to end.
    - Compare each element with the target.
    - Return the index if found, else return -1.

    Time Complexity (TC): O(n) --> check each element once
    Space Complexity (SC): O(1) --> no extra space used
    """
    for i in range(len(nums)):
        if nums[i] == target:   # Check current element
            return i            # Found target, return index
    return -1                   # Target not found after full scan

# Example usage of brute force
nums = [1, 4, 6, 7, 8, 9]
target = 3
print("Brute Force Result:", search_brute(nums, target))  # Output: -1


# ---------------- Optimal Approach ----------------
def search_optimal(nums, target):
    """
    Optimal approach:
    - Use modified binary search because the array is rotated but partially sorted.
    - Each step, find which half is sorted.
    - Decide which half to continue searching.
    
    Time Complexity (TC): O(log n) --> binary search halves the search space
    Space Complexity (SC): O(1) --> constant space
    """
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2   # Middle index
        
        if nums[mid] == target:   # Found target
            return mid

        # Check if left half is sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:  # Target in left half
                high = mid - 1
            else:                                 # Target in right half
                low = mid + 1
        # Right half is sorted
        else:
            if nums[mid] <= target <= nums[high]:  # Target in right half
                low = mid + 1
            else:                                  # Target in left half
                high = mid - 1

    return -1  # Target not found

# Example usage of optimal approach
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print("Optimal Result:", search_optimal(nums, target))  # Output: 4
