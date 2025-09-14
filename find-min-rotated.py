'''Given:

An array of integers nums which is sorted in ascending order but rotated at some pivot.

There are no duplicates in this array.

Task:

Find and return the minimum element in the array.

🔹 Key Points

Rotated Sorted Array:

Original sorted array: [0, 1, 2, 4, 5, 6, 7]

Rotated at pivot index 3 → [4, 5, 6, 7, 0, 1, 2]

Observation:

In a rotated array, one part is always sorted.

The minimum element is the only element where the previous element is greater than it, or it’s the first element if the array is not rotated.

Goal:

Find minimum efficiently using binary search, ideally O(log n) time.

🔹 Examples

Example 1:

Input: nums = [3, 4, 5, 1, 2]
Output: 1
Explanation: Array rotated at index 3, minimum element is 1.


Example 2:

Input: nums = [4, 5, 6, 7, 0, 1, 2]
Output: 0
Explanation: Minimum element is 0.'''
# Brute Force Approach to find minimum in rotated sorted array
def min_val(nums):
    """
    - Traverse the array.
    - Keep track of the minimum element.
    - Return the minimum element.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:   # Edge case: empty array
        return None

    min_element = nums[0]  # Initialize with first element

    for i in range(1, len(nums)):
        if nums[i] < min_element:  # Found smaller element
            min_element = nums[i]  # Update min

    return min_element  # Return the smallest element


# Example usage
nums = [9, 12, 13, 0, 1]
print("Minimum element:", min_val(nums))  # Output: 0
# Optimal Approach to find minimum in Rotated Sorted Array
def find_min(nums):
    """
    Binary Search Approach:
    - Exploit the fact that the array is rotated and partially sorted.
    - Compare middle element with the last element to decide which half contains the minimum.
    
    Time Complexity (TC): O(log n)
    Space Complexity (SC): O(1)
    """
    if not nums:  # Edge case: empty array
        return None

    low, high = 0, len(nums) - 1  # Initialize pointers

    while low < high:  # Continue until low meets high
        mid = (low + high) // 2  # Find middle index

        # If mid element is greater than high element, minimum is in right half
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            # Minimum is in left half (including mid)
            high = mid

    # After loop, low == high, pointing to minimum element
    return nums[low]


# Example usage
nums = [9, 12, 13, 0, 1]
print("Minimum element (optimal):", find_min(nums))  # Output: 0

nums2 = [4,5,6,7,0,1,2]
print("Minimum element (optimal):", find_min(nums2))  # Output: 0
