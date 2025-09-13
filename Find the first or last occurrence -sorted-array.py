'''Problem: First and Last Occurrence in Sorted Array

You are given a sorted array (may contain duplicate elements) and a target number.

Find the first occurrence of the target.

Find the last occurrence of the target.

If the target is not present, return [-1, -1].

✅ Example 1
Input: nums = [2, 4, 4, 4, 6, 7], target = 4
Output: [1, 3]
First occurrence of 4 is at index 1.
👉 Last occurrence of 4 is at index 3.'''
'''Brute Force Idea

Since the array is sorted, we could use Binary Search (O(log N)),
but in brute force we will simply scan the array linearly:

Traverse the array from start to end.

If element equals target:

If first occurrence is not yet set → set it.

Keep updating last occurrence until the loop ends.

If element is never found → return [-1, -1].'''
def firstAndLastBrute(nums, target):
    # Step 1: Initialize first and last as -1
    first = -1
    last = -1

    # Step 2: Traverse the whole array
    for i in range(len(nums)):
        if nums[i] == target:
            # If first is still -1, this is the first occurrence
            if first == -1:
                first = i
            # Keep updating last occurrence every time we see target
            last = i

    # Step 3: Return the result
    return [first, last]
# Example 1
nums = [2, 4, 4, 4, 6, 7]
target = 4
print(firstAndLastBrute(nums, target))  
# Output: [1, 3]
#optimal 
def firstAndLastBinary(nums, target):
    # Helper function to find either first or last occurrence
    def findOccurrence(findFirst):
        low, high = 0, len(nums) - 1
        result = -1  # store the index of target if found

        while low <= high:
            mid = (low + high) // 2  # middle index

            if nums[mid] == target:
                result = mid   # target found
                if findFirst:
                    # Keep searching left part for earlier occurrence
                    high = mid - 1
                else:
                    # Keep searching right part for later occurrence
                    low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return result

    # First occurrence (searching towards left)
    first = findOccurrence(True)
    # Last occurrence (searching towards right)
    last = findOccurrence(False)

    return [first, last]


# -----------------------------
# Example Runs
# -----------------------------

# Example 1: Multiple occurrences
nums = [2, 4, 4, 4, 6, 7]
target = 4
print(firstAndLastBinary(nums, target))  
# Output: [1, 3] → first occurrence at index 1, last occurrence at index 3

# Example 2: Single occurrence
nums = [1, 2, 3, 4, 5]
target = 3
print(firstAndLastBinary(nums, target))  
# Output: [2, 2] → only one occurrence at index 2

# Example 3: Target not present
nums = [1, 2, 3, 4, 5]
target = 6
print(firstAndLastBinary(nums, target))  
# Output: [-1, -1] → target not found
'''✅ TC = O(log N)

📦 Space Complexity (SC)

We use only a few variables: low, high, mid, result, first, last.

No extra data structures (arrays, hashmaps, etc).

So:

✅ SC = O(1) (constant space)'''