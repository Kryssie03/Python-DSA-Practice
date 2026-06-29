def pair(num: list)-> tuple:
  i = 0
  M1 = float('-inf')
  M2 = float('-inf')
  M3 = float('+inf')
  M4 = float('+inf')
  if len(num) < 2:
    return None
  for j in range(len(num)):
    if num[j] > M1:
      M2 = M1
      M1 = num[j]
    elif num[j] > M2:
      M2 = num[j]
    if num[j] < M3:
      M4 = M3
      M3 = num[j]
    elif num[j] < M4:
      M4 = num[j]
  max_mul = M1 * M2
  min_mul = M3 * M4

  if max_mul > min_mul:
    return (M1,M2)
  return (M3,M4)