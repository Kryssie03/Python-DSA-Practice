def duplicateElement(num: list)->int:
  seen = set()
  for i in num:
    if i in seen:
      return i
    seen.add(i)
  return -1
f = duplicateElement([1,2,3,5,4,7,6])
print(f)