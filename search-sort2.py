"""
Problem: Search in Rotated Sorted Array II

An array `nums` is sorted in ascending order but rotated at some pivot.
The array may contain duplicates.
A target integer `target` is given.
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: True


Task: 
- Return True if target exists in the array, otherwise return False.
"""

# ---------------- Brute Force Approach ----------------
def search_brute(nums, target):
    """
    Brute Force Approach:
    - Check each element in the array one by one.
    - Return True if target is found, else return False.

    Time Complexity (TC): O(n) --> may check all elements
    Space Complexity (SC): O(1) --> constant space
    """
    for i in range(len(nums)):       # Loop over all indices
        if nums[i] == target:        # Compare current element with target
            return True              # If found, return True
    return False                     # Target not found after full loop


# ---------------- Optimal Approach ----------------
def search_optimal(nums, target):
    """
    Optimal Approach:
    - Modified binary search to handle rotated sorted array with duplicates.
    - Each step decides which half is sorted and narrows down the search.
    
    Time Complexity (TC): O(log n) average, O(n) worst-case (due to duplicates)
    Space Complexity (SC): O(1)
    """
    low, high = 0, len(nums) - 1    # Initialize search boundaries

    while low <= high:               # Continue while search space is valid
        mid = (low + high) // 2     # Find middle index

        if nums[mid] == target:     # Check if mid element is the target
            return True             # Found target → return True

        # Handle duplicates
        if nums[low] == nums[mid] == nums[high]:
            low += 1                # Skip duplicate on left
            high -= 1               # Skip duplicate on right

        # Left half is sorted
        elif nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:  # Target lies in left half
                high = mid - 1                 # Search left
            else:                               # Target not in left half
                low = mid + 1                  # Search right

        # Right half is sorted
        else:
            if nums[mid] < target <= nums[high]:  # Target lies in right half
                low = mid + 1                   # Search right
            else:                               # Target not in right half
                high = mid - 1                  # Search left

    return False    # Target not found after search completes


# ---------------- Example Usage ----------------
nums = [2,5,6,0,0,1,2]
target = 0
print("Brute Force Result:", search_brute(nums, target))    # True
print("Optimal Result:", search_optimal(nums, target))      # True

nums2 = [2,5,6,0,0,1,2]
target2 = 3
print("Brute Force Result:", search_brute(nums2, target2))  # False
print("Optimal Result:", search_optimal(nums2, target2))    # False
