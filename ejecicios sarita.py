numero1=int(input("Digite el numero1: "))
numero2=int(input("Digite el numero2: "))
numero3=int(input("Digite el numero3: "))

if numero1<numero2 and numero2<numero3:
    print(f"El numero menor es: {numero1}")
elif numero2<numero1 and numero3<numero2:
    print(f"El numero menor es: {numero1}")
elif numero2<numero1 and numero1<numero3:
    print(f"El numero menor es: {2}")
elif numero2<numero3 and numero3<numero1:
    print(f"El numero menor es: {numero2}")
elif numero3<numero2 and numero3<numero1:
    print (f"El numero menor es: {numero3}")
elif numero3<numero1 and numero1<numero2:
    print (f"El numero menor es: {numero3}")
elif numero1==numero2 and numero3<numero2:
    print(f"El numero menor es {numero3}")
elif numero1<numero2 and numero2==numero3:
    print(f"El numero menor es: {numero1}")
elif numero1<numero2 and numero2==numero3:
    print(f"Hay dos numeros menores iguales: {numero2},{numero3}")
elif numero1==numero2 and numero2<numero3:
    print(f"Hay dos numeros menores iguales: {numero1},{numero2}")
elif numero1==numero2==numero3:
    print(f"Todos los numeros son iguales")