'''
Crear un programa que pida dos numeros y obtenga como resultado cual de ellos es par o si ambos lo son
'''
num1= int(input("Ingrese un numero: "))
num2= int(input("Ingrese otro numero: "))

if ((num1%2 ==0) and (num2%2 ==0)): 
    print("Ambos son pares")
elif ((num1%2 ==0) and (num2%2 !=0)):
    print(f"{num1} Es par")
    print(f"{num2} Es impar")
elif ((num1%2 !=0) and (num2%2 ==0)):
    print(f"{num1} Es impar")
    print(f"{num2} Es par")
else:
    print("Los dos numeros son impares")
    