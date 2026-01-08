

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

print(reverseInPlace(reverse_in_p_test))


