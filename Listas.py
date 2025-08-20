inventario = [] #Em Python para fazer uma lista de utiliza []
resposta = "S" 
#repita enquanto a resposta for "S"
while resposta == "S":
    inventario.append(input("Equipamento: ")) # adciona na lista
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Número Serial: ")))
    inventario.append(input("Departamento"))
    resposta = input("Digite \"S\" para continuar: ").upper()

for i in inventario:
    print(i)