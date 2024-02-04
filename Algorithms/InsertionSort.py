"""
The algorithm starts from left and checks the right element if it is smaller than the elements on the left to it, if the current element is smaller it moves an index until it reaches the begining of the list
"""


def insertionSort_twoElements(Array):
    # We have an array.
    # We start from the second element.
    current_element = Array[1]
    # We need to check with the next element on left.
    element_to_the_left = Array[0]
    # Take the first element and compare it to left element, there is no left element to move ot the next element.
    # Take the second element and compare it to the left element which is element_to_the_left.
    if element_to_the_left > current_element:
        # Swap the places of the current the element to the
        # But we lost the Array[0] all together, so it needs to saved.
        Array[0] = Array[1]
        Array[1] = element_to_the_left

    print(Array)


def insertionSort(Array):
    # The first element has nothing to compare to so we start from the second element which is at index 1 of the Array.
    for index in range(1, len(Array)):
        # Our current element will always be what i is.
        current_element = Array[index]
        # The left element will be the element next to the current element, which is i - 1.
        comparision_index = index - 1
        element_to_the_left = Array[comparision_index]
        # We don't know how many times we need to check the left element, so it is a indefinite loop. So we will use while.
        # We want to stop if the left element is lower than the index 0. And we need to stop when the left element smaller than the current element.
        # And we need a way for the element to keep checking if there are other left elements.
        print("Elements before sorting: ",
              element_to_the_left, current_element)
        print("Array before sorting: ", Array)
        while comparision_index >= 0 and element_to_the_left > current_element:
            print("Elements while sorting: ",
                  element_to_the_left, current_element)
            # If the left element is greater than we need to swap the places of current element and the left element. And, the comparision_index needs to go down by 1.
            # So, the comparision_index, the left element is set to be the current element. So our key is moved.
            Array[comparision_index] = current_element
            # But we need to swap the values of left element and key.
            Array[comparision_index + 1] = element_to_the_left
            # We reduce the comparision_index by one to show the next left element.
            comparision_index -= 1

            element_to_the_left = Array[comparision_index]

        print("Array after sorting: ", Array)

    print(Array)
    return Array


# insertionSort_twoElements([8, 4])
# insertionSort([4, 2, 1, 8, 3, 7])

# So, after looking at the real code and also going through the debugger to figure out what was happeninng in my code I realized, I was changing the element of the arrays every time the index changed. So, I realized I don't have to swap the current_element until it is the last call when either the current element is greater than the left element or the current element reaches the  zeroth index of the array.


def insertionSort2(Array):
    for i in range(1, len(Array)):
        current_element = Array[i]
        # index that records the movement through the list to compare the left elements is compare index
        compare_index = i - 1
        while compare_index >= 0 and current_element < Array[compare_index]:
            Array[compare_index + 1] = Array[compare_index]
            compare_index -= 1
        Array[compare_index + 1] = current_element
    print(Array)


# insertionSort2([7, 9, 3, 2, 1, 1])


def insertionsort3(Array):
    for i in range(1, len(Array)):
        key = Array[i]
        j = i - 1
        while j >= 0 and key < Array[j]:
            Array[j+1] = Array[j]
            j = j - 1
        Array[j+1] = key
    print(Array)


insertionsort3([7, 9, 3, 2, 1, 1])
