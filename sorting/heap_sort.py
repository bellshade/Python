#Runtime is O(nlogn)
def DFS(array, i, n, min_till_now):
    if i < n:
        x1 = DFS(array, 2*i+1, n, min_till_now)
        x2 = DFS(array, 2*i+2, n, min_till_now)
        if array[x1] <= array[min_till_now] and array[x1] <= array[x2]:
            min_till_now = x1
        elif array[x2] <= array[x1] and array[x2] <= array[min_till_now]:
            min_till_now = x2
        if array[i] < array[min_till_now]:
            return i
    return min_till_now

def Heap_Sort(array, size):
  count = 0
  for indx in range(size):
      minimum = DFS(array, indx, size, indx)
      if minimum != indx:
          array[indx], array[minimum] = array[minimum], array[indx]
          count += 1
  return array

size = int(input())
array = list(map(int, input().split()))
sorted_list = Heap_Sort(array, size)
print(*sorted_list)
