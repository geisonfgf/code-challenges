def max_diff(arr):
  max_diff = arr[1] - arr[0]
  min_element = arr[0]
  for i in xrange(1, len(arr)):
      if arr[i] - min_element > max_diff:
          max_diff = arr[i] - min_element
      if arr[i] < min_element:
           min_element = arr[i]              
  return max_diff

if __name__ == '__main__':
    arr = [1, 2, 6, 80, 100]
    print "Expected result:", 99
    print "Maximum difference is:", max_diff(arr)
