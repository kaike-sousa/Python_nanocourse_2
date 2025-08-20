# 1. Criando uma função simples
def saudacao():
    print("Olá, seja bem-vindo!")

# Usando a função
saudacao()


# 2. Função com parâmetro
def saudacao_nome(nome): #função que recebe valores na hora que é chamada.
    print(f"Olá, {nome}, seja bem-vindo!")

# Chamando a função passando um valor
saudacao_nome("Kaike")


# 3. Função com retorno
def soma(a, b):
    return a + b

resultado = soma(5, 7)
print("A soma é:", resultado)


# 4. Função com múltiplos retornos
def dividir(dividendo, divisor):
    quociente = dividendo // divisor
    resto = dividendo % divisor
    return quociente, resto

q, r = dividir(10, 3)
print("Quociente:", q, "Resto:", r)


# 5. Função com valor padrão
def apresentar(nome, idade=18):
    print(f"Nome: {nome}, Idade: {idade}")

apresentar("Kaike")       # Usa idade padrão = 18
apresentar("Vih", 20)     # Usa valor passado


# 6. Função que recebe vários valores (*args)
def media(*notas):
    soma = 0
    for n in notas:
        soma += n
    return soma / len(notas)

print("Média:", media(7, 8, 9, 10))


# 7. Função para organizar lógica do programa
def menu():
    print("1 - Somar dois números")
    print("2 - Ver média de notas")
    print("3 - Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        print("Resultado:", soma(a, b))

    elif opcao == "2":
        qtd = int(input("Quantas notas você deseja digitar? "))
        notas = []
        for i in range(qtd):
            notas.append(float(input(f"Digite a {i+1}ª nota: ")))
        print("Média:", media(*notas))

    elif opcao == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
