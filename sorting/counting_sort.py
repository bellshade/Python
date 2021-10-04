#Runtime is O(n)
def Counting_Sort(arr):
    lst = [0 for i in range(26)]
    for char in arr:
        lst[ord(char) - 97] += 1
    sorted_str = ''
    for i in range(26):
        sorted_str += lst[i]*chr(97+i)
        
    return sorted_str

array = list(map(int, input().split()))

Counting_Sort(array)
