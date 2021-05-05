import GapCalculator as gap
# from Celula import celula

dnaA = "tgcccaagtgctgccaaa"
dnaB = "gcctagtccatgatggta"
dnaA = gap.start(dnaA)
dnaB = gap.start(dnaB)

def Criarmatriz(a, b):
  temporario = []
  matriz = []
  list_a = list(a)
  list_b = list(b)
  for i in list_a:
    print("i" + str(i))
    for j in list_b:
      print('j'+ str(j))
      temporario.append(i + j)
    matriz.append(temporario)
    temporario = []
  return matriz
table = Criarmatriz(dnaA, dnaB)
print(table)
