corretasenha= "12345"
tent=0
lm_tent=3
while tent < lm_tent:
    senha = input("Digite a senha: ")
    if senha==corretasenha:
        print("Senha Correta! acesso libarado")
        break
    else:
        tent +=1
        print(F"Senha incorreta. Tentativas restantes: {tent - lm_tent}")
else:
    print("Senha bloqueada. Numero maximo de tentativas exedido.")




