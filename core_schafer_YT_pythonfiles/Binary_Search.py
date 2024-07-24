# Python program to do binary search on a list of numbers.
# Takes two inputs 1) List of Numbers 2) Search number


def binary_search(l, key):
    low = 0
    flag = 0
    high = len(l)-1
    mid = (low + high) // 2
    while low < high:
        #print(l,low,mid,high,key)
        if l[low] == key or l[high] == key or l[mid] == key:
            if l[low] == key:
                print(f"{key} is found in the list at {low} position.")
            elif l[high] == key:
                print(f"{key} is found in the list at {high} position.")
            else:
                print(f"{key} is found in the list at {mid} position.")
            flag = 1
            break
        elif key < l[high] and key > l[mid]:
            low = mid+1
            mid = (high + low) // 2
        elif key > l[low] and key < l[mid]:
            high = mid-1
            mid = (high + low) // 2
    if flag == 0:
        print(f"{key} not found in List.")


binary_search([1, 2, 3, 4, 5, 56,87], 2)
binary_search([1, 2, 3, 4, 5, 56,87], 9)

