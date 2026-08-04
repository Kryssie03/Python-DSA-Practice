def searchInsert(nums: list, target: int) -> int:
  if nums == []:
    print("list must not be empty")
  n = len(nums)
  for i in range(n):
    if target <= nums[i]:
      return i
  
  return n