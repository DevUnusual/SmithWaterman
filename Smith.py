import GapCalculator as gap
# from Celula import celula

dnaA = "tgcccaagtgctgccaaa"
dnaB = "gcctagtccatgatggta"
dnaA = gap.start(dnaA)
dnaB = gap.start(dnaB)

def Criarmatriz(a, b):
  temporario = []
  matriz = []
  for i in a:
    print("i" + str(i))
    for j in b:
      print('j'+ str(j))
      temporario.append(i + j)
    # print(temporario)
    matriz.append(temporario)
    temporario = []
  return matriz
table = Criarmatriz(dnaA, dnaB)
print(table)