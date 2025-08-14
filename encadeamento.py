#if - se tal condição for atendida, executa tal coisa
#elif - serve como alteranativa
#else - se não vai executar tal coisa
nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))
doenca = input('Suspeita de doença?').upper()
if idade >= 60:
    print(f'O paciente {nome} tem acesso prioritário pois sua idade é {idade}')
elif doenca == 'SIM'
    print(f'o paciente {nome} esta doente, deve ir para o centro cirurgico')
else:
        print(f'O paciente {nome} não tem acesso prioritário pois sua idade é {idade}') 