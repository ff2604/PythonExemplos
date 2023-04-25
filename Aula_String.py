
print("===============================================================================")

print("Primero " + " Segundo")
print(1+2)

variavel=1
print(variavel)

print("Valor :" + str(variavel) + str(" - Tipo:") + str(type(variavel)))

print("===============================================================================")


curso="Curso de Python "
print("/" + curso + "/")
print(curso[0:5])

print(len(curso))
print("/" + curso.strip()+ "/")

print(curso.lower())
print(curso.upper())
print(curso.replace("Python","C#"))

a=curso.split(" ")
print(a[1])

res="Python" in curso
print(res)

res="Python" not in curso
print(res)

print("===============================================================================")

cidade="Belo Horizonte"
dia = 15
mes = "Dezembro"
ano=2019
canal="Curso"
data="{}, {} de {} de {} \n\"{}\""

print(data.format(cidade,dia,mes,ano,canal))

# \n muda de linha    \r return    \'     \t              \b volta
print("===============================================================================")

aula="Curso"
print(bool(aula))  #retorna true devido ter conteudo

#aula=""
#print(bool(aula))   #retorna false devido nao ter conteudo

if aula:
    print("Posssui texto" + " \"" + aula + "\"")
else:
    print("variavel aula esta vazia")

print("===============================================================================")
#impressaõ na mesma linha
print('t', end="")
print('e', end="")
print('s', end="")
print('t', end="")
print('e')
#--------------------------------------------------------------------------------












