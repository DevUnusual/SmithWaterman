from Celula import celula

class Criarmatriz():
  def __init__(self, a,b, parametros):
    self.list_a = list(a)
    self.list_b = list(b)
    self.matriz =[]
    self.match = parametros[0]
    self.mismatch= parametros[1]
    self.gap = parametros[2]
    self.makeMatrizFromList()

  def cellAroundExist(self, posA, posB):
    CellAround =[] #é para guardar as celulas [horizontal, vertical, diagonal]
    if posA == posB == 0: return CellAround[0,0,0]
    if posA >=1:
      if posB >=1:
        CellAround.append(self.matriz[posA-1, posB]) #esquerda
        CellAround.append(self.matriz[posA, posB-1]) #vertical
        CellAround.append(self.matriz[posA-1, posB-1]) #diagonal
      else:
        CellAround.append(0) #horizontal
        CellAround.append(self.matriz[posA, posB-1]) #vertical
        CellAround.append(0) #diagonal
    else:
        CellAround.append(self.matriz[posA-1, posB]) #esquerda
        CellAround.append(0) #vertical
        CellAround.append(0) #diagonal

    return CellAround

  def calculateAround(parametros, posA, posB):
    #calcula as celulas ao redor volta o maximo e o caminho para chegar no maximo
  if parametros[0] != 0:
    esquerda = self.matriz[]
  if parametros[1] != 0:
  if parametros[2] != 0:

  def makeMatrizFromList(self):
    resultado = [] #vai contar max e caminho [maximo,[caminhos(-/|)]]
    LinesForMatriz = []
    for i in self.list_a:
      for j in self.list_b:
        resultado = self.calculateAround(self.cellAroundExist(i[2],j[2]), i, j) #volta a lista de celulas ao redor e calcula o maior
        #calcular os valores para definir o maior valor


        
