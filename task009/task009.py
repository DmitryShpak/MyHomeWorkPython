n=int(input())
numbers=range(-n,n+1)

with open('file.txt') as f:
    ids=f.read().split('\n')

prod = 1
for i in ids:
    prod*=numbers[i]
print(prod)