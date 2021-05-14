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
        CellAround.append(1) #esquerda
        CellAround.append(1) #vertical
        CellAround.append(1) #diagonal
      else:
        CellAround.append(0) #horizontal
        CellAround.append(1) #vertical
        CellAround.append(0) #diagonal
    else:
        CellAround.append(1) #esquerda
        CellAround.append(0) #vertical
        CellAround.append(0) #diagonal

    return CellAround

  def calculateAround(parametros):
    #calcula as celulas ao redor volta o maximo e o caminho para chegar no maximo


  def makeMatrizFromList(self):
    LinesForMatriz = []
    for i in self.list_a:
      for j in self.list_b:
        self.calculateAround(self.cellAroundExist(i[2],j[2])) #volta a lista de celulas ao redor e calcula o maior
        #calcular os valores para definir o maior valor


        
