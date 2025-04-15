resp='s'
while resp=='s':
n1= int(input("Informe a sua primeira nota: "))
while n1 <0 or n1>10:
    n1=int(input("Digite a 1nota corretamente: "))

n2=int(input("Digite a nota2: "))
while n2 <0 or n2>10:
    n2= int(input("digite a 2nota corretamente: "))

media=(n1+n2)/2
print(media)
resp=input("Deseja fazer o calculo novamente (s/n): ")



