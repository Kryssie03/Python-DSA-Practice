def reverse(num: list)-> list:
    i = 0
    j = len(num) - 1
    while i < j:
        num[i],num[j] = num[j],num[i]
        i += 1
        j -= 1
    return num

num = [1,2,3,4,5,6]
z = reverse(num)
print(z)