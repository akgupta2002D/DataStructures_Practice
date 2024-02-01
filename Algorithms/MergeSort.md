Algorithm: Merge Sort
Definition:
    The algorithm divides the list in half and sorts the halves, but before it sorts, it divides them to single element.
    For examples
                             [6, 5, 3, 1, 8, 7, 2, 4]                   Main List
                           /                          \
                  [6, 5, 3, 1]                    [8, 7, 2, 4]          Divided into half
                 /           \                   /           \
           [6, 5]           [3, 1]         [8, 7]           [2, 4]      Further Divided
          /     \           /     \       /     \           /     \
        [6]    [5]        [3]    [1]    [8]    [7]        [2]    [4]    Division to single elements which are self sorted.
          \     /           \     /       \     /           \     /
          [5, 6]           [1, 3]         [7, 8]           [2, 4]       Two are compared and merged
              \             /                 \             /
                [1, 3, 5, 6]                    [2, 4, 7, 8]            Each of the two are compared and merged into four 
                          \                      /
                         [1, 2, 3, 4, 5, 6, 7, 8]                       The left is compared to the right to be sorted