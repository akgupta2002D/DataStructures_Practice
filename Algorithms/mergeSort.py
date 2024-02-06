# Take a list, divide into half, then keep doing it.
# Then start comparing and adding the elements in order.

def merge(list):
    left_most_element = list[0]
    right_most_element = len(list) - 1
    middle_element = (left_most_element + right_most_element) // 2

    merge(left_most_element, middle_element)
    merge(middle_element, right_most_element)

def merge(left, right):
    
    # So, need to divide them and then compare something ( but what? ) and then merge them.
    return 