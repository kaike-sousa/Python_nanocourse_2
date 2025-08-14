
## **1. Variáveis e Tipos de Dados**

""" 1. Crie um programa que peça:

   * Seu nome
   * Sua idade
   * Sua altura
    Em seguida, exiba uma frase com essas informações.
    """

nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))
altura = float(input('Digite o sua altura: '))
print(f'nome = {nome}, idade = {idade}, altura = {altura}')


""" 2. Peça ao usuário o valor de um produto e um desconto em porcentagem.
    Mostre o valor final com desconto aplicado.
    """

valor_produto = float(input('Insira o valor do produto: '))
valor_descontado = valor_produto * 0.10
valor_final = valor_produto - valor_descontado
print(f'O valor teve um desconto de 10%, então ficou {valor_final}')

""" 3. Solicite dois números e mostre:

   * A soma
   * A subtração
   * A multiplicação
   * A divisão """

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
print(f'A soma é {numero1 + numero2}')
print(f'A subtração é {numero1 - numero2}')
print(f'A multiplicação é {numero1 * numero2}')
print(f'A divisão é {numero1/ numero2}')

## 2. `input()` e Conversão de Tipos

""" 4. Peça ao usuário para digitar um número inteiro e um número decimal.
    Converta corretamente e exiba a soma dos dois. """
inteiro = int(input('Digite o número inteiro: '))
decimal = float(input('Digite o número decimal: '))

print(f'A soma é {inteiro + decimal}')

#5. Peça ao usuário um número e mostre o **dobro**, o **triplo** e a **raiz quadrada** dele.
numero =  int(input('Digite o número: '))
print(f'O dobro é {numero * 2}, o triplo é {numero * 3}, a raiz é {numero ** 0.5}')


## **3. `type()` e Concatenação**

""" 6. Solicite o nome de uma cidade e mostre:

   * O nome todo em maiúsculas
   * O nome todo em minúsculas
   * Quantas letras tem (desconsiderando espaços) """

cidade = input('Digite o nome da cidade: ')
print(f'maiusculoa = {cidade.upper()}')
print(f'minuscula = {cidade.lower()}')
quantidade = len(cidade)
print(f'letras = {quantidade} ')


#7. Peça ao usuário dois números, mostre os dois valores e os tipos de dados que eles possuem.
print('Tipo inteiro = ', type(inteiro))
print('Tipo decimal = ', type(decimal)) 


## **4. Estruturas Condicionais**

""" 8. Peça a idade de uma pessoa e diga se ela é:

   * Criança (0 a 12 anos)
   * Adolescente (13 a 17 anos)
   * Adulto (18 a 59 anos)
   * Idoso (60 anos ou mais)
"""
idade_pessoas = int(input('Insira sua idade: '))
if idade_pessoas > 0 and idade_pessoas < 13:
    print('Criança')
elif idade_pessoas > 12 and idade_pessoas < 18:
    print('Adolescente')
elif idade_pessoas > 17 and idade_pessoas < 60:
    print('Adulto')
else: 
    print('idoso')

#9. Solicite dois números e informe qual deles é maior, ou se são iguais.

solicitacao1 = float(input('Insira um número: '))
solicitacao2 = float(input('Insira o segundo número: '))

if solicitacao1 > solicitacao2:
    print('O primeiro número é maior')
elif solicitacao1 == solicitacao2:
    print('Os números são iguais')
else:
    print('O segundo número é maior')

#10. Peça ao usuário um número e informe se ele é **par** ou **ímpar**.
par_impar = int(input('insira um número: '))
if par_impar % 2 == 0:
    print(f'O número {par_impar} é par')
else:
    print(f'O número {par_impar} é impar')

## **5. `if`, `elif`, `else`**

""" 11. Peça o nome, idade e se a pessoa está grávida (resposta SIM ou NÃO).
    Se for idoso ou grávida, exibir “Atendimento prioritário”. Caso contrário, “Aguardar na fila comum”. """
nome_paciente = input('Digite o seu nome: ')
idade_paciente = int(input('Digite a sua idade: '))
gravida = input('Você está grávida?').upper()

if idade_paciente > 60 or gravida == 'SIM':
    print('Atendimento prioritário')
else:
    print('Aguardar na fila comum')


""" 12. Peça três notas de um aluno e calcule a média.
    * Média >= 7: aprovado
    * Média >= 5 e < 7: recuperação
    * Média < 5: reprovado
"""

nota_aluno1 = int(input('Escreva a sua primeira nota: '))
nota_aluno2 = int(input('Escreva a sua segunda nota: '))
nota_aluno3 = int(input('Escreva a sua terceira nota: ' ))

media= (nota_aluno1 + nota_aluno2 + nota_aluno3)/ 3

if media >= 7:
    print('aprovado')
elif media  >= 5 and media < 7:
    print('recuperação')
else:
    print('reprovado')

## **6. `while`**

#13. Peça ao usuário um número e faça a contagem até 100, somando 5 a cada passo.
numero_while =  int(input('Escreva um número: '))
while numero_while < 100: 
    print(numero_while)
    numero_while += 5
print('Fim do laço')

#14. Solicite um número positivo. Caso o número digitado seja negativo, continue pedindo até que ele digite um valor válido.

numero_positivo =  int(input('Escreva um número positivo: '))
while numero_positivo < 0:
    print('O numero inserido é negativo')
    numero_positivo =  int(input('Escreva um número positivo: '))
print(f'O número positivo inserido foi: {numero_positivo}')


## **7. `for` e `range()`**

#15. Peça um número e mostre a tabuada dele de 1 a 10.
numero_for = int(input('Escreva um número: '))
for tabuada in range(1,11,1):
    print(f'{numero_for} x {tabuada} = {numero_for * tabuada}')
print('Fim do for')

#16. Mostre todos os números pares de 0 a 50.
for numeros_pares in range(0,51,2):
    print(numeros_pares)
print('Fim do for')

#17. Solicite dois números e mostre todos os números entre eles.
numero_for1 = int(input('Escreva um número: '))
numero_for2 = int(input('Escreva o segundo número: '))
for numeros_entre_for in range(numero_for1, numero_for2, 1):
    print(numeros_entre_for)
print('Fim do for')
