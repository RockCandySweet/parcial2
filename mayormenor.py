num1 = int(input('Ingrese el primer numero'))
num2 = int(input('Ingrese el segundo numero'))

while num1 !=0:
    if num1 > num2:
        print(f'El numero mayor es {num1}')
        print(f'El numero menor es {num2}')
    elif num2 > num1:
        print(f'El numero mayor es {num2}')
        print(f'El numero menor es {num1}')
    break