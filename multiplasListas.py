equipamentos = [] #Em Python para fazer uma lista de utiliza []
valores = [] #Em Python para fazer uma lista de utiliza []
seriais = [] #Em Python para fazer uma lista de utiliza []
departamentos = [] #Em Python para fazer uma lista de utiliza []
resposta = "S" 
#repita enquanto a resposta for "S"
while resposta == "S":
    equipamentos.append(input("Equipamento: ")) # adciona na lista
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento"))
    resposta = input("Digite \"S\" para continuar: ").upper()

for i in range(0, len(equipamentos)): # range() - Função que gera uma sequência de números, normalmente usada com for. Sintaxe: range(início, fim, passo)
    print(f'Equipamento: {i + 1}')
    print(f'Nome: {equipamentos[i]}')
    print(f'Valor: {valores[i]}')
    print(f'Serial {seriais[i]}')
    print(f'Departamento: {departamentos[i]}')