'''A sorted array of integers nums.

Every element appears exactly twice, except for one element which appears only once.

Task:

Find and return the element that appears only once.
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Explanation: All elements appear twice except 2.
Input: nums = [3,3,7,7,10,11,11]
Output: 10
Explanation: 10 appears only once.
'''
def single_element_brute(nums):
    """
    Brute force approach to find the single element in a sorted array.
    
    Why this approach:
    - Array is sorted, so duplicates appear next to each other.
    - Scan in pairs: first mismatch is the single element.
    - If all pairs match, last element is single.
    
    Time Complexity (TC): O(n) --> check each element at most once
    Space Complexity (SC): O(1) --> constant space, no extra array used
    """
    n = len(nums)  # Get the length of the array

    # Step 1: Traverse array in steps of 2 (check each pair)
    for i in range(0, n-1, 2):  # i = 0, 2, 4, ...
        if nums[i] != nums[i+1]:  # If current element != next element
            return nums[i]        # Found single element

    # Step 2: If all pairs matched, single element is last element
    return nums[-1]


# Example usage
nums1 = [1,1,2,3,3,4,4,8,8]
print("Single element (brute):", single_element_brute(nums1))  # Output: 2

nums2 = [3,3,7,7,10,11,11]
print("Single element (brute):", single_element_brute(nums2))  # Output: 10
def single_element_optimal(nums):
    """
    Binary search approach to find the single element in a sorted array.
    
    Time Complexity (TC): O(log n) --> binary search
    Space Complexity (SC): O(1) --> constant space
    """
    low, high = 0, len(nums) - 1
    
    while low < high:
        mid = (low + high) // 2
        
        # Make sure mid is even, because pairs start at even index
        if mid % 2 == 1:
            mid -= 1
        
        # Check the pair starting at mid
        if nums[mid] == nums[mid + 1]:
            # Pair is correct → single element is in right half
            low = mid + 2
        else:
            # Pair is broken → single element is in left half (including mid)
            high = mid
    
    # After loop, low == high → pointing to the single element
    return nums[low]
nums1 = [1,1,2,3,3,4,4,8,8]
print("Single element:", single_element_optimal(nums1))  # Output: 2
