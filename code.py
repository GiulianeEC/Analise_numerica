'''A atividade é construir um programa em Python que solucione um sistema linear utilizando qualquer um dos métodos propostos no livro. 
Você deverá implementar todos os métodos em Python e o usuário escolhe qual método ele quer usar para resolver o seu problema. 
A atividade será avaliada em 5.0 pontos extracurriculares.'''

import numpy as np

#valores da matriz A
A = [[10, 5, -4, 4],[7, 30, 3, 33],[-4, 3, 7, 3],[4, 33, 3, 29]]
#valores do vetor b
b = [13, 74, 5, 85]

def começar():
  calcular  = 's'
  main()
  while calcular == 's':
    calcular = input('\nDeseja calcular novamente? (s- sim e n - não)')
    if calcular == 's':
      main()
    elif calcular == 'n':
      print('FIM')
      break
    else:
      print('\nOpção invalida - parada forçada -  fim\n ')
      break

def substituicoes_retroativas(A, b):
  # ordem da matriz A
  n = len(b)
  # inizializa o vetor x, com ordem n e valor 0
  x = [0]*n
  for i in range(n-1, -1, -1):
    soma = 0
    for j in range(i+1, n):
      soma = soma + A[i][j]*x[j]
    x[i] = (b[i] - soma)/A[i][i]

  return x

def substituicoes_sucessivas(A, b):
  # ordem matriz A
  n = len(b)
  # inizializa o vetor x, com ordem n e valor 0
  x = [0]*n
  for i in range(0, n):
    soma = 0
    for j in range(0, i):
      soma = soma + A[i][j]*x[j]
    x[i] = (b[i] - soma)/A[i][i]
  return x

def eliminacao_gauss(A, b):
  n = len(b)
  for k in range(0, n-1):
    for i in range(k+1, n):
      m = - A[i][k]/A[k][k]
      for j in range(k+1, n):
        A[i][j] = m * A[k][j] + A[i][j]
      b[i] = m * b[k] + b[i]
      A[i][k] = 0
  x = substituicoes_retroativas(A, b)
  return x

def decomposicao_LU(A,b):
  # armazena a ordem da matriz
  n = len(b)
  # cria matriz de zeros n*n
  L = np.zeros(shape=(n, n))
  for i in range(0, n):
    L[i][i] = 1

  for k in range(0, n-1):
    for i in range(k+1, n):
      m = - A[i][k]/A[k][k]
      L[i][k] = -m
      for j in range(k+1, n):
        A[i][j] = m * A[k][j] + A[i][j]
      A[i][k] = 0

    y = substituicoes_sucessivas(L, b)
    x = substituicoes_retroativas(A, y)
    return x

def decomposicao_cholesky(A, b):
  v = np.linalg.eigvals(A)
  for i in range(len(A)):
    if v[i] < 0:
      print("\nNao e possivel utilizar esse metodo ...\n\n")
      return -1
  # cria matriz L do tamanho de A
  L = np.zeros_like(A)
    # n recebe ordem de A
  n = len(A)
  for j in range(n):
    for i in range(j, n):
      if i == j:
        L[i][j] = np.sqrt(A[i][j]-np.sum(L[i, :j]**2))
      else:
        L[i][j] = (A[i][j] - np.sum(L[i, :j]*L[j, :j]))/L[j][j]

    y = substituicoes_sucessivas(L, b)
    x = substituicoes_retroativas(L.transpose(), y)
    return x

def main():
  print('1 - Eliminação de Gauss || 2 - Decomposicao LU ||3 - Decomposicao de Choelesky \n')
  escolha = int(input('Escolha o metodo desejado:   '))
  if escolha == 1:
      x = eliminacao_gauss(A,b)
  elif escolha == 2:
      x = decomposicao_LU(A,b)
  elif escolha == 3:
      x = decomposicao_cholesky(A,b)
  else:
    print("opção invalida!! ")
  return print("\nSolucao:\n", x)
  


if __name__ == '__main__':
  começar()
  
