def rev_array(arr: list,k: int)-> list:
  if k <= 1:
    return arr
  i = 0
  n = len(arr)
  while i < n:
    l = i
    r = min(i + k - 1, n - 1)
    while l < r:
      arr[l], arr[r] = arr[r], arr[l]
      l += 1
      r -= 1
    i += k
  return arr
h = rev_array([1,2,3,4,5,6,7,8],8)
print(h)