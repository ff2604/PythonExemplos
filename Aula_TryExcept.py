x=10

try:
    print(x)
except NameError:
    print("X mão definido")
except:
    print("Erro desconhecido")
else:
    print("Dudo certo")
finally:
    print("Fim do tratamento")


#gerando um Exception ou erro
num=-1
if num < 1:
    raise Exception("Valor nao permitido")
