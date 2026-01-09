

# Reverse array solution (Reverse pattern)
rev_test = [2, 3, 4, 1, 6]
rev_test2 = [1, 2, 3, 4]

def reverseArray(a):
    result = []
    initial_index = len(a) - 1
    while (initial_index >= 0):
        result.append(a[initial_index])
        initial_index = initial_index - 1 
    print("result:", result)



# Find the largest element in the array (Linear Scan (Finding Extrema))
lg_test = [10, 5, 100, 2, 45]
lg_test2 = [10.9, 10.10]

def largestNumber(arg):
    if not arg:
        return 
    max_val = arg[0]
    for num in arg:
        if (num > max_val):
            max_val = num
    return max_val


# Reverse-In-place logic (Strong)
reverse_in_p_test = [1, 2, 3, 4, 5]

def reverseInPlace(a):
    left = 0
    right = len(a) - 1
    while left < right:
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1
    return a


# Palindrome Check
p_test = [1, 2, 3, 2, 1]
p_test2 = [1, 2, 3, 4]

def palindromeCheck(a):
    left = 0
    right = len(a) - 1
    while left < right:
        if a[left] != a[right]:
            return False
        left += 1
        right -= 1
    return True


# Two Sum in sorted array
def twoSumHashMap(nums, target):
    seen = {} # Our memory bank
    
    for num in nums:
        diff = target - num
        if diff in seen:
            # Your logic: We found the 'result' we were searching for!
            return [diff, num]
        # If not found, save the current number in our memory
        seen[num] = True 
    return []

ts_test = [2, 11, 7, 15]
target = 9


# in-place movement of zeros
ip_test = [0, 1, 0, 3, 12]
# output = [1, 3, 12, 0, 0]

def inPlaceMovement(a):
    writer = 0
    for reader in range(len(a)):
        if a[reader] != 0:
            # Swap them!
            a[writer], a[reader] = a[reader], a[writer]
            # Move the writer forward
            writer += 1
    return a


# Given an integer array nums, return True if any value appears at least twice in the array, and return Falseif every element is distinct.
def containsDuplicate(a):
    seen = {}
    for num in a:
        if num in seen:
            return True
        seen[num] = True
    return False


# Reverse Vowels of a String
