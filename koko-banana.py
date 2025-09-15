import math   # we need math.ceil() to round up division

'''
Problem Statement (in simple words)
-----------------------------------
- We have piles of bananas.
- Koko eats at a speed "k" bananas per hour.
- She can only eat from one pile per hour.
- If pile < k, she just finishes it and the rest of the hour is wasted.
- We must find the *minimum speed k* so that she finishes all piles in h hours.
'''


def minEatingSpeed_bruteforce(piles, h):
    """
    Brute Force Approach
    --------------------
    - Try all speeds from 1 to max(piles).
    - For each speed, calculate total hours needed.
    - Return the first speed that allows finishing in <= h hours.
    """
    max_speed = max(piles)   # the maximum bananas in one pile = max possible speed

    # try all speeds from 1 up to max_speed
    for k in range(1, max_speed + 1):
        total_hours = 0   # reset hours for this speed

        # calculate how many hours needed at speed k
        for pile in piles:
            # math.ceil(pile/k) = hours required to finish this pile at speed k
            total_hours += math.ceil(pile / k)

        # check if this speed is enough
        if total_hours <= h:
            return k   # the first valid speed is the answer


# Example usage (Brute Force)
piles1 = [3, 6, 7, 11]
h1 = 8
print("Brute Force:", minEatingSpeed_bruteforce(piles1, h1))   # Output: 4



def minEatingSpeed_optimal(piles, h):
    """
    Optimal Approach (Binary Search)
    --------------------------------
    - Speeds range from 1 to max(piles).
    - Instead of testing all, we do binary search.
    - If mid speed works (hours <= h), try smaller speed.
    - Else, try bigger speed.
    """
    low, high = 1, max(piles)   # possible speed range

    # binary search loop
    while low < high:
        mid = (low + high) // 2   # guess the middle speed
        total_hours = 0

        # calculate hours needed at speed = mid
        for pile in piles:
            total_hours += math.ceil(pile / mid)

        # if Koko can finish in time with speed mid
        if total_hours <= h:
            high = mid   # try smaller speeds (move left)
        else:
            low = mid + 1   # need bigger speed (move right)

    # when loop ends, low == high → minimum valid speed
    return low


# Example usage (Optimal)
piles2 = [3, 6, 7, 11]
h2 = 8
print("Optimal:", minEatingSpeed_optimal(piles2, h2))   # Output: 4
 