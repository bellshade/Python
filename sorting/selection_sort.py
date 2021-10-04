#Runtime is O(n²)
def Selection_Sort(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[j] < array[i]:
                array[j], array[i] = array[i], array[j]
    
array = list(map(int, input().split()))

Selection_Sort(array)
print(array)
