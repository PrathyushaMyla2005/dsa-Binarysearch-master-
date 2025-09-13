'''Problem Statement

You are given a sorted array of distinct integers and a target value.

If the target is found in the array → return its index.

If not found → return the index where it would be inserted in order (keeping array sorted).

📌 Example 1
Input: nums = [1,3,5,6], target = 5
Output: 2


Explanation: Target 5 is found at index 2'''
'''Step 1: Brute Force Approach (Linear Search)

Loop through the array.

If you find the target → return index.

If element > target → return that index (insert before).

If loop ends, return len(nums) (insert at end).

⏱ Time Complexity = O(N)
💾 Space Complexity = O(1)'''
def searchInsert(nums, target):
    # Loop through each element of the array
    for i in range(len(nums)):
        # If current element is greater than or equal to target
        # → This is the correct position to insert target
        if nums[i] >= target:
            return i   # return index immediately
    
    # If we finish loop and target is greater than all elements
    # → Insert at the end
    return len(nums)
# Example 1
nums = [1, 3, 5, 6]
target = 5
print(searchInsert(nums, target))  
# Output: 2 (because nums[2] == 5)
'''Step 2: Optimal Approach (Binary Search 🔥)

Since array is sorted, we can use Binary Search.

Idea:

Maintain two pointers: low = 0, high = len(nums) - 1.

While low <= high:

mid = (low + high) // 2

If nums[mid] == target → return mid

If nums[mid] < target → search right → low = mid + 1

If nums[mid] > target → search left → high = mid - 1

If not found, the correct insert position is at low.

👉 Trick: At the end, low always points to the correct insert index.

⏱ Time Complexity = O(log N)
💾 Space Complexity = O(1)'''
def searchInsert(nums, target):
    # Step 1: Initialize two pointers
    low, high = 0, len(nums) - 1   # search space = full array

    # Step 2: Standard Binary Search loop
    while low <= high:
        mid = (low + high) // 2    # middle index

        # Case 1: If target is found at mid
        if nums[mid] == target:
            return mid

        # Case 2: If target is greater, search right half
        elif nums[mid] < target:
            low = mid + 1

        # Case 3: If target is smaller, search left half
        else:
            high = mid - 1

    # Step 3: If not found, 'low' will be the insert position
    return low
nums = [1, 3, 5, 6]
target = 5
print(searchInsert(nums, target))  # Output: 2
