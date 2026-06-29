def Samepat(num,pat):
  n = len(num)
  p = len(pat)
  num_to_pat = {}
  pat_to_num = {}
  if n != p:
    return False
  for i in range(n):
    cn = num[i]
    cp = pat[i]
    if cn in num_to_pat:
      if num_to_pat[cn] != cp:
        return False
    if cp in pat_to_num:
      if pat_to_num[cp] != cn:
        return False
    pat_to_num[cp] = cn

    num_to_pat[cn] = cp
  return True
