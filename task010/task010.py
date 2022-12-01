a=[int(i) for i in input().split()]
summa=0
for i in range(len(a)):
    if i%2 !=0:
        summa +=a[i]
print(summa)