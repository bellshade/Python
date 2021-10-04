#Runtime is O(n²)
def insert(array, index, n):
    while index > 0:
        if array[index - 1] < array[index]:
            break
        array[index - 1], array[index] = array[index], array[index - 1]
        index -= 1

def Insertion_Sort(array, n):
    for i in range(1,n):
        if array[i] < array[i - 1]:
            insert(array, i, n)

array = list(map(int, input().split()))
Insertion_Sort(array, len(array))
