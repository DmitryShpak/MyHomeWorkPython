x = int(input('Введите значения числа x '))
y = int(input('Введите значения числа y '))
z = int(input('Введите значения числа z '))
if not(x or y or z)==(not x and not y and not z):
    print(True)
else:
    print(False)
