#Runtime is O(nlogn)
def partition(start_index, end_index):
    global array
    pivot_value = array[end_index]
    temp_pivot = start_index
    for i in range(start_index, end_index):
        if array[i] <= pivot_value:
            array[temp_pivot], array[i] = array[i], array[temp_pivot]
            temp_pivot += 1
    array[temp_pivot], array[end_index] = array[end_index], array[temp_pivot]
    return temp_pivot

def Quick_Sort(start_index, end_index):
    global array
    if start_index < end_index:
        pivot_index = partition(start_index, end_index)
        Quick_Sort(start_index,pivot_index - 1)
        Quick_Sort(pivot_index + 1, end_index)

array = list(map(int, input().split()))

Quick_Sort( 0, len(array) - 1)
print(array)
