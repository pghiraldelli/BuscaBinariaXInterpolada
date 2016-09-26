import numpy

def buscaBinaria(lista, valor):
  limiteSuperior = len(lista)-1
  limiteInferior = 0
  totalIteracoes = 0  

  while (limiteInferior <= limiteSuperior):
    totalIteracoes += 1
    meio = (limiteInferior + limiteSuperior)/2

    if (lista[meio] == valor): 
      return [True, totalIteracoes]
    elif (lista[meio] > valor): limiteSuperior = meio - 1
    else: limiteInferior = meio + 1

  return [False, totalIteracoes]

def buscaInterpolada(lista, valor):
  limiteSuperior = len(lista)-1
  limiteInferior = 0
  totalIteracoes = 0  

  while (limiteInferior <= limiteSuperior) and (valor >= lista[limiteInferior]) and (valor <= lista[limiteSuperior]):
    totalIteracoes += 1
    fracao = (valor - lista[limiteInferior]) // (lista[limiteSuperior] - lista[limiteInferior])
    meio = limiteInferior + (limiteSuperior - limiteInferior) * fracao

    if (lista[meio] == valor): 
      return [True, totalIteracoes]
    elif (lista[meio] > valor): limiteSuperior = meio - 1
    else: limiteInferior = meio + 1

  return [False, totalIteracoes]

def geraListaAleatoriaOrdenada(tamanho):
  lista = numpy.random.randint(0, tamanho, tamanho)
  lista.sort()
  return lista

def main():
  lista = geraListaAleatoriaOrdenada(100)
  print lista
  print "Binaria"
  solBin = buscaBinaria(lista, 9)
  print solBin
  print "Interpolada"
  solInt = buscaInterpolada(lista, 9)
  print solInt


if __name__ == "__main__":
  main()
