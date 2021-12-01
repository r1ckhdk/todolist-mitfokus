###########################################################
#
# Lista to-do para processo seletivo de estágio Mitfokus
#
########################################### por R.H. ######

import csv
import pandas as pd
from datetime import datetime

###########################################################

dir_csv = ' '

class Agenda():

    def __init__(self):
        self.lista_main = []
        self.lista_criadas = []
        self.lista_progresso = []
        self.lista_completas = []
        self.lista_atrasadas = []

def menu():
    print('-' * 20)
    print('Bem vindo à sua lista de tarefas.')

    return escolher_comando()

def escolher_comando():
    print('-' * 20)
    print('1. Criar tarefa')
    print('2. Remover tarefa')
    print('3. Editar tarefa')
    print('4. Listar todas as tarefas')
    print('5. Listar tarefas filtradas por status')
    print('6. Alterar status (individualmente)')
    print('7. Alterar status (em lote)')
    print('8. Remover tarefas completas')
    print('9. Adiar tarefa')
    print('0. Sair do programa')
    print('-' * 20)

    comandos_menu = [1,2,3,4,5,6,7,8,9,0]

    while True:
        try:
            print('Digite o número do comando: ')
            comando = int(input(prompt))
        except ValueError:
            print('Erro! Digite um número válido.')
            continue
    
        if comando not in comandos_menu:
            print('Erro! Digite um número válido')
            continue
        else:
            break

    if comando == 1:
        criar_tarefa()

    elif comando == 2:
        remover_tarefa_id()

    elif comando == 3:
        editar_tarefa()

    elif comando == 4:
        listar_todas_main()

    elif comando == 5:
        listar_filtradas()

    elif comando == 6:
        mudar_status_ind()

    elif comando == 7:
        mudar_status_lote()

    elif comando == 8:
        remover_completas()

    elif comando == 9:
        adiar_tarefa()

    else:
        salvar_csv()
        print('Salvando e saindo do programa. Até mais!')

    return comando

def criar_tarefa():
    ## criar  loop pra sair
    print('-' * 20)
    print('Você escolheu: 1. Criar tarefa')
    print('-' * 20)
    nome = str(input("Digite um nome pra sua tarefa: "))
    descricao = str(input("Digite uma descrição para sua tarefa: "))
    # venc = pegar_venc()
    # temp = Tarefa(nome, descricao, venc)
    # lista_tarefas.append(temp)

    temp = {
        'nome': nome,
        'descricao': descricao,
        'status': 'Criada',
        'venc': pegar_venc(),
        'data': pegar_data()
    }

    agenda.lista_main.append(temp)
    
    print("Sua tarefa foi adicionada com sucesso. Deseja adicionar outra tarefa? (s/n)")
    r = input(prompt)
    if r == 's':
        criar_tarefa()
    else:
        menu()

def pegar_venc():
    print("Deseja adicionar uma data de vencimento à tarefa? (s/n)")
    v = input(prompt)
    
    if v == 's':
        venc = input("Insira a data de vencimento (dd/mm/aaaa): ")
    else:
        venc = None

    if venc == None:
        venc = 'não há'

    return venc

def pegar_data():

    data_hoje = datetime.today()
    data_criacao = data_hoje.strftime("%d/%m/%Y")
    return data_criacao

def remover_tarefa_id():
    print('Você escolheu: 2. Remover tarefa')
    print('-' * 20)

    listar_todas()
    while True:
        try:
            print('Qual o ID da tarefa que deseja remover?')
            indice = int(input(prompt))
        except ValueError:
            print('Erro! Digite um número válido')
            continue
        
        if indice > len(agenda.lista_main) - 1:
            print('Erro! Este índice não existe')
        else:
            break

    agenda.lista_main.pop(indice)
    
    print(f'A tarefa de ID {indice} foi removida com sucesso.')
    print('-' * 20)
    menu()

def editar_tarefa():
    listar_todas()
    
    while True:
        try:
            print('Qual o ID da tarefa que deseja editar?')
            indice = int(input(prompt))
        except ValueError:
            print('Erro! Digite um número válido')
            continue
        
        if indice > len(agenda.lista_main) - 1:
            print('Erro! Este índice não existe')
        else:
            break

    print('-' * 20)
    print('1. Nome')
    print('2. Descrição')
    print('3. Data de vencimento')

    comando = int(input('Qual campo deseja editar da tarefa? '))

    if comando == 1:
        campo = 'nome'
    
    elif comando == 2:
        campo = 'descricao'

    elif comando == 3:
        campo = 'venc'

    print('Digite sua edição. (Lembre-se que, ao editar o vencimento, utilize o formato dd/mm/aaaa)')
    edicao = input(prompt)
    agenda.lista_main[indice][campo] = edicao
    
    print('Sua tarefa foi editada com sucesso. Deseja editar outra tarefa? (s/n)')
    r = input(prompt)

    if r == 's':
        editar_tarefa()
    else:
        menu()

def mudar_status_ind():
    listar_todas()
    while True:
        try:
            print('Qual o ID da tarefa que deseja alterar o status?')
            indice = int(input(prompt))
        except ValueError:
            print('Erro! Digite um número válido')
            continue
        
        if indice > len(agenda.lista_main) - 1:
            print('Erro! Este índice não existe')
        else:
            break
    
    print('Para qual status deseja mudar a tarefa acima?')
    print('-' * 20)
    print('1. Criada')
    print('2. Em progresso')
    print('3. Completa')
    print('4. Atrasada')

    lista_comandos = [1,2,3,4]

    while True:
        try:
            comando = int(input('Digite o número correspondente: '))
        except ValueError:
            print('Erro! Digite um número válido.')
            continue
    
        if comando not in lista_comandos:
            print('Erro! Digite um número válido')
            continue
        else:
            break

    if comando == 1:
        agenda.lista_main[indice]
        agenda.lista_main[indice]['status'] = 'Criada'

    elif comando == 2:
        agenda.lista_main[indice]
        agenda.lista_main[indice]['status'] = 'Em progresso'

    elif comando == 3:
        agenda.lista_main[indice]
        agenda.lista_main[indice]['status'] = 'Completa'

    elif comando == 4:
        agenda.lista_main[indice]
        agenda.lista_main[indice]['status'] = 'Atrasada'

    print(f'O status da sua tarefa de número {indice} foi alterado com sucesso!')
    print('-' * 20)
    menu()

def mudar_status_lote():
    atualizar_listas()
    print('Qual grupo de tarefas deseja alterar o status? ')
    print('1. Criadas')
    print('2. Em progresso')
    print('3. Completas')
    print('4. Atrasadas')
    
    lista_comandos = [1,2,3,4]
    
    while True:
        try:
            comando_1 = int(input(prompt))
        except ValueError:
            print('Erro! Digite um número válido')
            continue

        if comando_1 not in lista_comandos:
            print('Erro! Digite um número válido')
        else:
            break

    print('Para qual status deseja alterá-los?')
    print('1. Criadas')
    print('2. Em progresso')
    print('3. Completas')
    print('4. Atrasadas')
    
    while True:
        try:
            comando_2 = int(input(prompt))
        except ValueError:
            print('Erro! Digite um número válio')
            continue

        if comando_2 not in lista_comandos:
            print('Erro! Digite um número válido')
        else:
            break

    if comando_2 == 1:
        status_att = 'Criada'
    
    elif comando_2 == 2:
        status_att = 'Em progresso'
    
    elif comando_2 == 3:
        status_att = 'Completa'

    elif comando_2 == 4:
        status_att = 'Atrasada'

    if comando_1 == 1:
        for tarefa in agenda.lista_criadas:
            tarefa['status'] = status_att

    elif comando_1 == 2:
        for tarefa in agenda.lista_progresso:
            tarefa['status'] = status_att

    elif comando_1 == 3:
        for tarefa in agenda.lista_completas:
            tarefa['status'] = status_att
    
    elif comando_1 == 4:
        for tarefa in agenda.lista_atrasadas:
            tarefa['status'] = status_att

    print('O status de suas tarefas foram alterados com sucesso.')
    menu()

def listar_todas():
    print('Lista de todas as tarefas')
    print('-' * 30)
    df = pd.DataFrame(agenda.lista_main)
    vazio = df.empty
    if vazio == True:
        print('A lista está vazia.')
    else:
        print(df)

    print('-' * 30)

def listar_todas_main():
    
    print('Lista de todas as tarefas')
    print('-' * 20)
    df = pd.DataFrame(agenda.lista_main)

    vazio = df.empty
    if vazio == True:
        print('A lista está vazia.')
    else:
        print(df)
    
    print('-' * 20)
    print('1. Voltar ao menu')
    print('2. Ver tarefas filtradas')

    lista_comandos = [1,2]

    while True:
        try:
            print('Digite o número do comando: ')
            comando = int(input(prompt))
        except ValueError:
            print('Erro! Digite um número válido.')
            continue
    
        if comando not in lista_comandos:
            print('Erro! Digite um número válido')
            continue
        else:
            break

    if comando == 1:
        menu()
    
    elif comando == 2:
        listar_filtradas()

def listar_filtradas():
    atualizar_listas()
    
    print('Qual desses filtros deseja aplicar na visualização?')
    print('-' * 20)
    print('1. Criadas')
    print('2. Em progresso')
    print('3. Completas')
    print('4. Atrasadas')

    lista_comandos = [1,2,3,4]

    while True:
        try:
            comando = int(input('Digite o número correspondente: '))
        except ValueError:
            print('Erro! Digite um número válido.')
            continue

        if comando not in lista_comandos:
            print('Erro! Digite um número válido')
            continue
        else:
            break
    
    if comando == 1:
        listar_criadas()
    
    if comando == 2:
        listar_progresso()
    
    if comando == 3:
        listar_completas()
    
    if comando == 4:
        listar_atrasadas()

    print('-' * 20)
    print('1. Voltar ao menu')
    print('2. Ver todas as tarefas')

    lista_comandos2 = [1,2]

    while True:
        try:
            print('Digite o número do comando: ')
            comando2 = int(input(prompt))
        except ValueError:
            print('Erro! Digite um número válido.')
            continue
    
        if comando2 not in lista_comandos2:
            print('Erro! Digite um número válido')
            continue
        else:
            break

    if comando2 == 1:
        menu()
    
    elif comando2 == 2:
        listar_todas_main()
    
def listar_completas():
    print('-' * 20)
    df = pd.DataFrame(agenda.lista_completas)
    vazio = df.empty
    if vazio == True:
        print('A lista está vazia.')
    else:
        print(df)    

def listar_progresso():
    print('-' * 20)
    df = pd.DataFrame(agenda.lista_progresso)
    vazio = df.empty
    if vazio == True:
        print('A lista está vazia.')
    else:
        print(df)    

def listar_atrasadas():
    print('-' * 20)
    df = pd.DataFrame(agenda.lista_atrasadas)
    vazio = df.empty
    if vazio == True:
        print('A lista está vazia.')
    else:
        print(df)

def listar_criadas():
    print('-' * 20)    
    df = pd.DataFrame(agenda.lista_criadas)
    vazio = df.empty
    if vazio == True:
        print('A lista está vazia.')
    else:
        print(df)

def atualizar_listas():
    completas = [t for t in agenda.lista_main if t['status'] == 'Completa']
    #for tarefa in completas:
    #    agenda.lista_completas.append(tarefa)
    agenda.lista_completas = completas
    
    progresso = [t for t in agenda.lista_main if t['status'] == 'Em progresso']
    #for tarefa in progresso:
    #    agenda.lista_progresso.append(tarefa)
    agenda.lista_progresso = progresso

    criadas = [t for t in agenda.lista_main if t['status'] == 'Criada']
    #for tarefa in criadas:
    #    agenda.lista_criadas.append(tarefa)
    agenda.lista_criadas = criadas

    atrasadas = [t for t in agenda.lista_main if t['status'] == 'Atrasada']
    #for tarefa in atrasadas:
    #    agenda.lista_atrasadas.append(tarefa)
    agenda.lista_atrasadas = atrasadas

def remover_completas():
    
    # aux = len(agenda.lista_main)

    # i = 0

    # while i < aux:
    #     if agenda.lista_main[i]['status'] == 'Completa':
    #         agenda.lista_main.remove(agenda.lista_main[i])

    #     else:
    #         i += 1 

    # for tarefa in agenda.lista_main:
    #     if tarefa['status'] == 'Completa':
    #         agenda.lista_main.remove(tarefa)

    # for i, j in enumerate(agenda.lista_main):
    #     if j['status'] == 'Completa':
    #         del agenda.lista_main[i]

    # index = next(index for index, tarefa in enumerate(agenda.lista_main)
    #          if tarefa['status'] == 'Completa')
    #             del agenda.lista_main[index]

    temp_list = [x for x in agenda.lista_main if x['status'] != 'Completa']
    agenda.lista_main = temp_list
    
    print('As tarefas completas foram removidas com sucesso.')
    menu()

def adiar_tarefa():
    listar_todas()
    
    while True:
        try:
            print('Qual o ID da tarefa que deseja editar?')
            indice = int(input(prompt))
        except ValueError:
            print('Erro! Digite um número válido')
            continue
        
        if indice > len(agenda.lista_main) - 1:
            print('Erro! Este índice não existe')
        else:
            break

    print('Digite a nova data de vencimento da tarefa (dd/mm/aaa)')
    nova_data = input(prompt)

    agenda.lista_main[indice]['venc'] = nova_data

    print('A data de vencimento da sua tarefa de ID {indice} foi atualizada.')

    menu()

def carregar_csv():
    with open(dir_csv, 'r') as f:
        reader = csv.DictReader(f)
        agenda.lista_main = list(reader)

def salvar_csv():
    with open(dir_csv, 'w', newline='') as f:
        fieldnames = ['nome','descricao','status','venc','data']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(agenda.lista_main)
        f.close()


###########################################################


prompt = '> '
agenda = Agenda()
carregar_csv()

saida = menu()
if saida == 0:
    exit()