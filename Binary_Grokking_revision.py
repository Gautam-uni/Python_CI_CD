# Binary Grokking test
def Binary_grokking_revision(arr, item):
    low = 0
    high = len(arr) - 1
    while (low <= high):
        mid = (low + high) // 2
        guess = arr[mid]
        if(guess == item):
            return mid
        elif(guess < item):
            low = mid + 1
        else:
            high = mid - 1
    return None
list_1 = [1,2,5,6,8,9,12,14,18,22,26,34,45,445,4456,6778]
item_1 = 4456
print (len(list_1))
position_of_out = (Binary_grokking_revision(list_1, item_1))
print (f"the position of out is {position_of_out}")
# should return  4
