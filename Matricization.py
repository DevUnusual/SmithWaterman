from Celula import celula

class Criarmatriz():
  def __init__(self, a,b, parametros):
    self.list_a = list(a)
    self.list_b = list(b)
    self.matriz =[]
    self.makeMatrizFromList()

  def cellAroundExist(self, posA, posB):
    CellAround =[] #é para guardar as celulas [horizontal, vertical, diagonal]
    if posA == posB == 0: return CellAround[0,0,0]
    if posA >=1:
      if posB >=1:
        CellAround.append(self.matriz[posA, (posB-1)]) #esquerda
        CellAround.append(self.matriz[(posA-1), posB]) #vertical
        CellAround.append(self.matriz[(posA-1), (posB-1)]) #diagonal
      else:
        CellAround.append(0) #horizontal
        CellAround.append(self.matriz[(posA-1), posB]) #vertical
        CellAround.append(0) #diagonal
    else:
        CellAround.append(self.matriz[posA, (posB-1)]) #esquerda
        CellAround.append(0) #vertical
        CellAround.append(0) #diagonal

    return CellAround

  def calculateHorizontal():

  def calculateVertical():
  def calculateDiagonal():

  def makeMatrizFromList(self):
    CellAround =[0,0,0] #é para guardar as celulas ao redor se existir
    LinesForMatriz = []
    for i in self.list_a:
      for j in self.list_b:
        CellAround = self.cellAroundExist(i[2],j[2])
        #calcular os valores para definir o maior valor


        
