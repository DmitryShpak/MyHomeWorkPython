print('Введите значения числа x ')
x = int(input())
print('Введите значения числа y ')
y = int(input())
print('Введите значения числа z ')
z = int(input())
if not(x or y or z)==(not x and not y and not z):
    print(True)
else:
    print(False)