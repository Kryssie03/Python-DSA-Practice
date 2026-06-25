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



# To Remove First Occurence
def removeFirstOccurence(num: list, target: int)-> list:
  for i,n in enumerate(num):
    if n == target:
      remove(num,i)
      break

  return num
z = removeFirstOccurence([1,2,3,4,5,5,6],5)
print(z)