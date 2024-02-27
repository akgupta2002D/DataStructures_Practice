
# So, lets imagine I need to keep track of these fibonacchi numbers and then add it to get the sum at that index.
# What can we do?
# Idea 1: Was to add it to a sum, but we end up adding multiple things that we shouldn't
# Idea 2: We need to add the fibonacchi numbers as we calculate them and return when same calculation is needed. Called memoization, one of the paradigm of dynamic Programming.

def fiboWithMemory(n, memoryList={}):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in memoryList:
        # print(memoryList[n])
        return memoryList[n]
    memoryList[n] = fiboWithMemory(
        n-1, memoryList) + fiboWithMemory(n-2, memoryList)
    print(f'{n} : {memoryList[n]}')
    return memoryList[n]


# This function gives me the nth term of the fibonachi sequence. Not the sum till that function.
def fibonachiGeneral(n):
    array = []
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonachiGeneral(n-1) + fibonachiGeneral(n-2)


print(fibonachiGeneral(10))

fiboWithMemory(10)
