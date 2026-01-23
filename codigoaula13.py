listaTarefa = []


def criaTarefa():
   tarefa_id = len(listaTarefa) + 1
   categoria = input('Categoria: ')
   descricao = input('Descricao: ')
   urgencia = input('Urgencia: ')
   diasRestante = input('Dias restante: ')
   status = 'Pendente'
   dictTarefa = {'ID': tarefa_id,'Categoria': categoria, 'Descrição': descricao, 'Urgência': urgencia, 'Dias restante': diasRestante,
                 'Status': status}
   listaTarefa.append(dictTarefa)


while True:
   print('1 Criar!')
   print('2 Alterar Status!')
   print('3 Listar Tarefa!')
   print('0 Sair!')
   opcao = int(input('Opcao:'))
   if opcao == 1:
       criaTarefa()
   elif opcao == 2:
       print('lista de taferas:')
       print('ID - Catgeoria - Descrição')
       for item in listaTarefa:
           print(item['ID'],' - ',item['Categoria'],' - ',item['Descrição'])
       idTarefa = int(input('Informar o ID da tarefa para atualizar o status: '))
       for item in listaTarefa:
           if item['ID'] == idTarefa:
               novo_Status = input('Informar o novo Status: ')
               if(novo_Status == 'Concluido'):
                   for tarefa in listaTarefa:
                       if tarefa['ID'] == idTarefa:
                           listaTarefa.remove(tarefa)
                           print("Tarefa Atualizado com sucesso!")
                           print("Tarefa removida!")
                           break
               else:
                   print('Tarefa atualizado com sucesso!')
                   item['Status'] = novo_Status
                   break
           else:
               print('ID invalido')
   elif opcao == 3:
       for item in listaTarefa:
           print(item)
   elif opcao == 0:
       break
   else:
       print('Opcao invalida!')
