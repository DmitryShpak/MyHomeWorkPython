n = input('Введите число ')
 
suma = 0
 
for digit in n:
    if digit.isdigit():
        suma += int(digit)
 
print("Сумма:", suma)