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
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

busca = input('Digite o nome do equipamento que deseja buscar: ')
for i in range(0,len(equipamentos)): # range() - Função que gera uma sequência de números, normalmente usada com for. Sintaxe: range(início, fim, passo)
    if busca == equipamentos[i]:
        print(f'Valor: {valores[i]}')
        print(f'Serial {seriais[i]}')