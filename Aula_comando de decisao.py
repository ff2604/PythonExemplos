#versão 2
aula="Curso"
print(bool(aula))  #retorna true devido ter conteudo

#aula=""
#print(bool(aula))   #retorna false devido nao ter conteudo

if aula:
    print("Posssui texto" + " \"" + aula + "\"")
else:
    print("variavel aula esta vazia")

print("===============================================================================")

a=10
b=5
res=0
op="-"

if a>b:
    print("Maior")
else:
    print("menor")

print("--------------------------------------")

if op == "+":
    res=a+b
elif op == "-":
    res= a-b
elif op == "*":
    res= a*b
elif op == "/":
    res= a/b 

if op != "+" and op != "-" and op != "*" and op != "/":
    print("Operador invalido")
else:
    print(res)

print("===============================================================================")