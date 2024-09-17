senha = 1234

tent = 0
cont = 0
insira = int(input("Insira sua senha: "))

if insira == 1234:
    print("acesso permitido")
else:
    while tent< 2:
        print("Senha incorreta")
        insira = int(input("insira sua senha novamente: "))
        tent += 1
        insira != senha