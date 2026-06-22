def remove(num: list,index: int)->list:
  n = len(num)
  if index < 0 or index >= n:
    raise IndexError('List index out of range')
  for i in range(index,n-1,1):
      num[i] = num[i+1]
  num[-1:] = []
  return num
p = remove([1,2,3,4,5,6],2)
print(p)