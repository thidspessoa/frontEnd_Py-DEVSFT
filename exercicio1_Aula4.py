
## Resolvendo equação: 5x²+7x-1
""" x = float(input("Insira o valor de x: "))
print((x**2)*5 + (7 * x)- 1)
"""



##Alterando valor para -6
""" print(6*(1-2)) """



## Quadrado da soma de dois valores inteiros: (a+b)²
"""
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))

print((a**2)+(2*a*b)+b**2)
"""



## Operação com dois valores.
"""
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
operacao = input("Escolha qual será a operação a ser realizada (soma, subtração, divisão, multiplicação): ")

if (operacao == "soma" or operacao == "Soma"):
    print(num1+num2)
    if ((operacao == "soma" or operacao == "Soma") == True):
        print("\nVocê inseriu os valores de: %.2f e %.2f"%(num1, num2))
        print("\nE a operação escolhida foi: %s"%(operacao))
elif (operacao == "subtração" or operacao == "Subtração"):
    print(num1-num2)
    if((operacao == "subtração" or operacao == "Subtração") == True):
        print("\nVocê inseriu os valores de: %.2f e %.2f"%(num1, num2))
        print("\nE a operação escolhida foi: %s"%(operacao))
elif (operacao == "multiplicação" or operacao == "Multiplicação"):
    print(num1*num2)
    if((operacao == "Multiplicação" or operacao == "Multiplicação") == True):
        print("\nVocê inseriu os valores de: %.2f e %.2f"%(num1, num2))
        print("\nE a operação escolhida foi: %s"%(operacao))
elif (operacao == "divisão" or operacao == "Divisão"):
    print(num1/num2)
    if ((operacao == "divisão" or operacao == "Divisão")== True):
        print("\nVocê inseriu os valores de: %.2f e %.2f"%(num1, num2))
        print("\nE a operação escolhida foi: %s"%(operacao))
else:
    print("Operação inserida invalida, tente novamente.")
"""



## calcular media do aluno: 2º nota = peso 2
"""
a = float(input("Digite a sua primeira nota: "))
b = float(input("Digite a sua segunda nota: "))

print ((a+(b*2)/2))
"""



## Juros composto
"""
p =  10000 #Investimento inicial
n = 12 #Taxa de juros nominal
r = 0.08 #Número de vezes no ano
t = int(input("Digite o número t de anos: ")) #Número de anos

a = p*(1+(r/n))**(n*t)

print(" o valor do juros composto em %d anos é: %.2f"%(t, a))
"""



## Area o circulo

#formula igual o 6




## temperatura

#formula igual o 6



## Consumo de gasolina em quilometros por litro
km = int(input("Digite quantos quilometros foram percorridos: "))
gasolina = float(input("Digite quantos litros de gasolina: "))

print ("\nO consumo vai ser de: ", (km/gasolina),"km/L")





## Armazenar e printar
"""
a = "Eu"
b = "serei"
c = "um"
d = "cientista"
e = "de"
f = "dados!"

print ("%s %s %s %s %s %s"%(a,b,c,d,e,f))
"""


##CONCATENAR
"""
va1 = "Ju"
va2 = "line"
print (va1 + " " + va2)
"""