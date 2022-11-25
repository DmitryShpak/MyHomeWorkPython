n=int(input('Введите номер координатной четверти (от 1 до 4)'))
if n==1:
    print('x [0,inf],y [0,inf]')
elif n==2:
    print('x [-inf,0],y [0,inf]')
elif n==3:
    print('x [-inf,0],y [-inf,0]')
elif n==4:
    print('x [0,inf],y [-inf,0]')