def missing(nums,k):
    n = len(nums)
    for i in range(n):
        if nums[k] <=  k:
            k += 1
        else:
            break
    return k

def  missing(nums,k):
    low = 0, high =  n-1
    while(low <= high):
        mid = low+high//2
        missing = 