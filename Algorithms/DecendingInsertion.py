# Lets start with the insertion sort for ascending order

def InsertionSort(Array):
    for i in range(1, len(Array)):
        key = Array[i]
        j = i - 1
        while j >= 0 and key < Array[j]:
            Array[j + 1] = Array[j]
            j = j - 1
        Array[j + 1] = key
    print(Array)


def DecendingInsertion(Array):
    for i in range(1, len(Array)):
        key = Array[i]
        j = i - 1
        while j >= 0 and key > Array[j]:
            Array[j + 1] = Array[j]
            j = j - 1
        Array[j + 1] = key
    print(Array)
    return Array


InsertionSort([9, 5, 2, 1, 2])
DecendingInsertion([1, 2, 3, 4, 5])
print(len([1, 2, 3]))
