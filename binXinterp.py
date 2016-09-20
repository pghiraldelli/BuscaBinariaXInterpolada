
def buscaBinaria(lista, valor):
  limiteSuperior = len(lista)-1
  limiteInferior = 0
  
  while (limiteInferior < limiteSuperior):
    meio = (limiteInferior + limiteSuperior)/2
    if (lista[meio] == valor): 
      print "achei" 
      return 
    elif (lista[meio] > valor): limiteSuperior = meio
    else: limiteInferior = meio

  print "nao achei"
  return -1

def main():
  lista = [1,4,9,20,30,31]
  buscaBinaria(lista, 0)


if __name__ == "__main__":
  main()