def rotate(arr, k):
    """
    O(1) space
    O(n*k) time
    """
    for i in xrange(k):
        j = len(arr) - 1
        while j > 0:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

def rotate2(arr, k):
    """
    O(n) space
    O(n) time
    """
    initial_arr = arr[-k:]
    final_arr = arr[0:-k]
    return initial_arr + final_arr

a, b = [1,2,3,4,5,6,7], [1,2,3,4,5,6,7]
ans = [5,6,7,1,2,3,4]

rotate(a, 3)
b = rotate2(b, 3)
print a, a == ans