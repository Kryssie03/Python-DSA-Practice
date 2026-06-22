def insert(num=list,val=int,index=int)->list:

  num.append(None)
  n = len(num)
  for i in range(n-1,index,-1):
      num[i]= num[i-1]
  num[index] = val
  return num
z = insert([1,3,4,5,6],2,1)
print(z)