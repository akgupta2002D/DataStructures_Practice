# We always look at the middle element.
# If the target element is lower than the middle element of the list, we change the range;
# The initial index remains the same, the final index is now the middle.

def BinarySearch(list, target):
    initialIndex = 0
    finalIndex = len(list) - 1

    # for i in list: Don't use for loop, because we don't know how many iterations we require.
    while initialIndex <= finalIndex:
        midIndex = (initialIndex + finalIndex)//2
        if target < list[midIndex]:
            finalIndex = midIndex - 1
        elif target > list[midIndex]:
            initialIndex = midIndex + 1
        else:
            return midIndex
    return -1


list = [1, 2, 3, 4, 5, 6, 7, 8]
target = 2

print(BinarySearch(list, target))
