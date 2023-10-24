# Um aplicativo de gerenciamento de tarefas em Python
# Bibliotecas para Interface
import tkinter as tk
from tkinter import messagebox

# Uma lista para armazenar as tarefas
tarefas = []

# Uma função para cadastrar uma tarefa
def cadastrar_tarefa():
  # Solicitar os dados da tarefa ao usuário
  descricao = input("Digite a descrição da tarefa: ")
  data = input("Digite a data de vencimento da tarefa (dd/mm/aaaa): ")
  prioridade = int(input("Digite a prioridade da tarefa (1 - baixa, 2 - média, 3 - alta): "))

  # Validar a prioridade da tarefa
  if prioridade < 1 or prioridade > 3:
    print("Prioridade inválida. Digite um número entre 1 e 3.")
    return

  # Criar um dicionário para representar a tarefa
  tarefa = {"descricao": descricao, "data": data, "prioridade": prioridade}

  # Adicionar a tarefa à lista de tarefas
  tarefas.append(tarefa)

  # Exibir uma mensagem de confirmação
  print("Tarefa cadastrada com sucesso!")

# Uma função para visualizar as tarefas
def visualizar_tarefas():
  # Verificar se a lista de tarefas está vazia
  if len(tarefas) == 0:
    print("Não há tarefas cadastradas.")
    return

  # Ordenar as tarefas por prioridade (do maior para o menor)
  tarefas.sort(key=lambda t: t["prioridade"], reverse=True)

  # Exibir as tarefas com seus respectivos índices
  print("Tarefas cadastradas:")
  for i, t in enumerate(tarefas):
    print(f"{i+1} - {t['descricao']} - {t['data']} - {t['prioridade']}")

# Uma função para atualizar uma tarefa
def atualizar_tarefa():
  # Verificar se a lista de tarefas está vazia
  if len(tarefas) == 0:
    print("Não há tarefas cadastradas.")
    return

  # Solicitar o índice da tarefa que será atualizada ao usuário
  indice = int(input("Digite o número da tarefa que será atualizada: ")) - 1

  # Validar o índice da tarefa
  if indice < 0 or indice >= len(tarefas):
    print("Índice inválido. Digite um número entre 1 e", len(tarefas))
    return

  # Solicitar os novos dados da tarefa ao usuário para atualização da tarefa
  descricao = input("Digite a nova descrição da tarefa: ")
  data = input("Digite a nova data de vencimento da tarefa (dd/mm/aaaa): ")
  prioridade = int(input("Digite a nova prioridade da tarefa (1 - baixa, 2 - média, 3 - alta): "))

  # Validar a prioridade da tarefa
  if prioridade < 1 or prioridade > 3:
    print("Prioridade inválida. Digite um número entre 1 e 3.")
    return

  # Atualizar os dados da tarefa na lista de tarefas
  tarefas[indice]["descricao"] = descricao
  tarefas[indice]["data"] = data
  tarefas[indice]["prioridade"] = prioridade

  # Exibir uma mensagem de confirmação
  print("Tarefa atualizada com sucesso!")

# Uma função para excluir uma tarefa
def excluir_tarefa():
   # Verificar se a lista de tarefas está vazia
   if len(tarefas) == 0:
     print("Não há tarefas cadastradas.")
     return

   # Solicitar o índice da tarefa que será excluída ao usuário
   indice = int(input("Digite o número da tarefa que será excluída: ")) -1

   # Validar o índice da tarefa
   if indice <0 or indice >= len(tarefas):
     print("Índice inválido. Digite um número entre 1 e", len(tarefas))
     return

   # Remover a tarefa da lista de tarefas
   del(tarefas[indice])

   # Exibir uma mensagem de confirmação
   print("Tarefa excluída com sucesso!")

# Uma função para exibir o menu de opções
def exibir_menu():
  print("Aplicativo de Gerenciamento de Tarefas")
  print("Escolha uma opção:")
  print("1 - Cadastrar tarefa")
  print("2 - Visualizar tarefas")
  print("3 - Atualizar tarefa")
  print("4 - Excluir tarefa")
  print("0 - Sair")

# Uma variável para armazenar a opção escolhida pelo usuário
opcao = -1

# Um laço de repetição para executar o aplicativo até que o usuário digite 0
while opcao != 0:
  # Exibir o menu de opções
  exibir_menu()

  # Solicitar a opção ao usuário
  opcao = int(input("Digite a sua opção: "))

  # Executar a função correspondente à opção escolhida
  if opcao == 1:
    cadastrar_tarefa()
  elif opcao == 2:
    visualizar_tarefas()
  elif opcao == 3:
    atualizar_tarefa()
  elif opcao == 4:
    excluir_tarefa()
  elif opcao == 0:
    print("Obrigado por usar o aplicativo GerenMatch!")
  else:
    print("Opção inválida. Digite um número entre 0 e 4.")