'''First, let’s break the sentence:

"Find the smallest divisor"
means → we need to find the smallest number (divisor) that we can use to divide the array elements so that a special condition is satisfied.

📌 The special condition:

You are given an array of numbers (example: [1, 2, 5, 9])

You are given a number called threshold (example: 6)

Rule: Divide each number in the array by the divisor → take the result and round UP (ceiling).

Add all these rounded values together.

👉 That sum should be less than or equal to threshold.

📌 Example (step by step)

Let’s say:

nums = [1, 2, 5, 9]
threshold = 6


We need to test divisors one by one.

✅ Try divisor = 1

Divide each number by 1, round up:

1 ÷ 1 = 1

2 ÷ 1 = 2

5 ÷ 1 = 5

9 ÷ 1 = 9
👉 Sum = 1 + 2 + 5 + 9 = 17 ❌ (not ≤ 6)

✅ Try divisor = 2

1 ÷ 2 = 0.5 → round up → 1

2 ÷ 2 = 1

5 ÷ 2 = 2.5 → round up → 3

9 ÷ 2 = 4.5 → round up → 5
👉 Sum = 1 + 1 + 3 + 5 = 10 ❌ (not ≤ 6)

✅ Try divisor = 3

1 ÷ 3 = 0.33 → round up → 1

2 ÷ 3 = 0.66 → round up → 1

5 ÷ 3 = 1.66 → round up → 2

9 ÷ 3 = 3
👉 Sum = 1 + 1 + 2 + 3 = 7 ❌ (not ≤ 6)

✅ Try divisor = 4

1 ÷ 4 = 0.25 → round up → 1

2 ÷ 4 = 0.5 → round up → 1

5 ÷ 4 = 1.25 → round up → 2

9 ÷ 4 = 2.25 → round up → 3
👉 Sum = 1 + 1 + 2 + 3 = 7 ❌ (still not ≤ 6)

✅ Try divisor = 5

1 ÷ 5 = 0.2 → round up → 1

2 ÷ 5 = 0.4 → round up → 1

5 ÷ 5 = 1

9 ÷ 5 = 1.8 → round up → 2
👉 Sum = 1 + 1 + 1 + 2 = 5 ✅ (YES, ≤ 6)

👉 So the smallest divisor = 5 ✅'''
import math

def smallestDivisor_bruteforce(nums, threshold):
    """
    Brute Force Approach:
    ---------------------
    - Try every possible divisor from 1 to max(nums).
    - For each divisor:
        → compute sum of ceil(num/divisor) for all nums.
        → if sum <= threshold → return divisor.
    - Stop at the first valid divisor.

    Time Complexity (TC): O(n * max(nums))  → very slow if numbers are big
    Space Complexity (SC): O(1)
    """
    for divisor in range(1, max(nums) + 1):   # check all possible divisors
        total = 0
        for num in nums:
            total += math.ceil(num / divisor) # divide & round up
        if total <= threshold:                # valid divisor found
            return divisor
    return -1  # should not happen if input is valid


# Example usage
nums1 = [1, 2, 5, 9]
threshold1 = 6
print("Brute Force:", smallestDivisor_bruteforce(nums1, threshold1))  # 5
import math

def smallestDivisor_optimal(nums, threshold):
    """
    Optimal Approach (Binary Search):
    ---------------------------------
    - Divisor can only be between 1 and max(nums).
    - Use binary search to minimize divisor:
        → mid = (low + high) // 2
        → compute sum with mid as divisor
        → if sum <= threshold → try smaller divisor (high = mid)
        → else → need bigger divisor (low = mid + 1)
    - At the end, low will be the smallest valid divisor.

    Time Complexity (TC): O(n * log(max(nums))) → much faster
    Space Complexity (SC): O(1)
    """
    low, high = 1, max(nums)

    while low < high:
        mid = (low + high) // 2

        # compute sum using this mid as divisor
        total = 0
        for num in nums:
            total += math.ceil(num / mid)

        if total <= threshold:
            high = mid   # try smaller divisor
        else:
            low = mid + 1  # need larger divisor

    return low  # smallest valid divisor


# Example usage
nums2 = [1, 2, 5, 9]
threshold2 = 6
print("Optimal:", smallestDivisor_optimal(nums2, threshold2))  # 5
