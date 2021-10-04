#Runtime is O(n²)
def Bubble_Sort(array, length):
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    
array = list(map(int, input().split()))

Bubble_Sort(array, len(array))
print(array)
