def containsDuplicate(num: list)-> bool:
  seen = set()
  n = len(num)
  for i in num:
    if i in seen:
      return True

    seen.add(i)
  return False
y = containsDuplicate([1,2,3,5,5,4,7,6])
print(y)