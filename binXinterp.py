import random
import time

'''Busca um elemento em uma lista, partindo sempre do meio do array e comparando as duas metades.'''
def buscaBinaria(lista, valor):
  tempoInicio = time.time()
  limiteSuperior = len(lista)-1
  limiteInferior = 0
  totalIteracoes = 0  

  while (limiteInferior <= limiteSuperior):
    totalIteracoes += 1
    meio = (limiteInferior + limiteSuperior)/2

    if (lista[meio] == valor):
      tempoFim = time.time() 
      return ["Achou", totalIteracoes,tempoFim-tempoInicio]
    elif (lista[meio] > valor): limiteSuperior = meio - 1
    else: limiteInferior = meio + 1

  tempoFim = time.time()
  return ["Nao achou", totalIteracoes, tempoFim-tempoInicio]

'''Busca um elemento numa lista, levando em consideracao uma distribuicao uniforme, calculando a posicao
onde o elemento se encontra a partir de seu valor e incrementando de 1 caso nao o encontre na primeira vez. '''
def buscaInterpolada(lista, valor):
  tempoInicio = time.time()
  limiteSuperior = len(lista)-1
  limiteInferior = 0
  totalIteracoes = 0  

  while (limiteInferior <= limiteSuperior) and (valor >= lista[limiteInferior]) and (valor <= lista[limiteSuperior]):
  	totalIteracoes += 1
    	fracao = float(valor - lista[limiteInferior]) / (lista[limiteSuperior] - lista[limiteInferior])
    	meio = int(limiteInferior + (limiteSuperior - limiteInferior) * fracao)

    	if (lista[meio] < valor): limiteInferior = meio + 1;
	elif (valor < lista[meio]): limiteSuperior = meio - 1;
    	else: tempoFim = time.time(); return ["Achou", totalIteracoes, tempoFim-tempoInicio]

  tempoFim = time.time();
  if (valor == lista[limiteInferior]): return ["Achou", totalIteracoes, tempoFim-tempoInicio]
  else: return ["Nao achou", totalIteracoes, tempoFim-tempoInicio]

'''Gera uma lista ordenada e sem repeticao de numeros aleatorios de zero a tamanhoDaLista*10.'''
def geraListaAleatoriaOrdenada(tamanho):
  lista = random.sample(range(tamanho*10), tamanho)
  lista.sort()
  return lista

'''Gera uma lista ordenada e sem repeticao que nao segue uma distribuicao uniforme. Ela e preenchida com zeros ate a metade e depois preenchida com valores de 1 ate tamanho/2.'''
def geraListaBinariaMelhor():
  tamanho = 10000
  lista = []
  num = 1
  for i in range(0,tamanho):
	if i < tamanho/2: lista.append(0)
	else: 
	  lista.append(num)
	  num += 1
  return lista

'''Gera uma lista ordenada e sem repeticao, de numeros pares, de tamanho 10000.'''
def geraListaInterpoladaMelhor():
  tamanho = 10000
  lista = []
  for i in range (0,tamanho):
	lista.append(i*2)
  return lista

def main():
  geradorLista = int(raw_input("Digite (1) para gerar uma lista aleatoria, (2) para um exemplo em que a busca binaria seja melhor e (3) para um exemplo cuja a interpolada seja melhor: "))

  lista = []
  if geradorLista == 1 : 
	tamanho = int(raw_input("Digite o tamanho pretendido para a lista: "))
	lista = geraListaAleatoriaOrdenada(tamanho)
  elif geradorLista == 2 : lista = geraListaBinariaMelhor()
  elif geradorLista == 3 : lista = geraListaInterpoladaMelhor()

  print lista

  valor = int(raw_input("Digite um valor a ser procurado na lista: "))

  print "Binaria"
  solBin = buscaBinaria(lista, valor)
  print solBin
  print "Interpolada"
  solInt = buscaInterpolada(lista, valor)
  print solInt


if __name__ == "__main__":
  main()
