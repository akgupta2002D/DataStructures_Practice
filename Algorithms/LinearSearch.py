def LinearSearch(Array,item_to_find):
    for i in range(0, len(Array)):
        if Array[i] == item_to_find:
            print(f'{Array[i], "at index", i }')
            
        
LinearSearch([1,2,3,4,5,6],2)