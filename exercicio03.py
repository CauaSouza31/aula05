x=0
soma=0
qtd=int(input("Digite a quantidade de alunos: "))
while x<qtd:
    valor=int(input("Digite nota dos alunos: "))
    soma+=valor
    x+=1
media=soma/qtd
print(media)

