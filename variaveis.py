#input - serve para fazer interação com o usuário, pegando uma resposta 
nome = input('Digite o seu nome: ')
empresa = input('Digite o nome da empresa: ')

#int - trata de numeros inteiros
#float - trata de numeros com decimais
quant_funcionarios = int(input('Digite a quantidade de funcionário: '))
media_mensalidade = float(input('Digite o a média da mensalidade: '))

#concatenação
print(f'O {nome} trabalha na {empresa}')
print(f'A media da mensalidade é {media_mensalidade}')

#o type aborda os tipos de dados das variáveis, tipo string, bolleano e number
print('TIPOS DE DADOS')
print('O tipo da variável nome é', type(nome))
print('O tipo da variável empresa é', type(empresa))
print('O tipo da variável quantidade de funcionários é', type(quant_funcionarios))
print('O tipo da variável media mensalidade é', type(media_mensalidade))