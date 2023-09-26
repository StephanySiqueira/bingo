import random

lista = list(range(1,91))

for c in range(len(lista) -1, 0, -1):
   j = random.randint(0,c)
   lista[c], lista[j] = lista[j], lista[c]

numeros = []

while True:
   print("""
      1- Numeros Bingo
      2- ver numeros que ja foram 
      3-finalizar
   """)
   escolha = input("Escolha uma opção: ")

   if escolha == "1":
      if lista:
         numero_sorteado = lista.pop()
         numeros.append(numero_sorteado)
         print(f"O número sorteado é: {numero_sorteado}")
      else:
         print("Todos os números já foram chamados!")

   elif escolha == "2":

      if lista:
         print("Números que já foram chamados:")
         print(numeros)
      else:
         print("Nenhum número foi chamado")

   elif escolha == "3":
      print("Jogo de bingo finalizado.")
      break

   else:
      print("Opção inválida. Escolha 1, 2 ou 3.")
