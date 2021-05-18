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
  
  def getCellMatriz(self, a, b):
    return self.matriz[a][b]

  def cellAroundExist(self, posA, posB):
    CellAround =[] #é para guardar as celulas [horizontal, vertical, diagonal]
    if posA == 0 and posB == 0: 
      return [0,0,0]
    if posA >=1:
      if posB >=1:
        CellAround.append(self.getCellMatriz(posA-1, posB)) #esquerda
        CellAround.append(self.getCellMatriz(posA, posB-1)) #vertical
        CellAround.append(self.getCellMatriz(posA-1, posB-1)) #diagonal
      else:
        CellAround.append(0) #horizontal
        CellAround.append(self.getCellMatriz(posA, posB-1)) #vertical
        CellAround.append(0) #diagonal
    else:
        CellAround.append(self.getCellMatriz(posA-1, posB)) #esquerda
        CellAround.append(0) #vertical
        CellAround.append(0) #diagonal

    return CellAround

  def calculateAround(self,parametros, posA, posB):
    esquerda = vertical = diagonal = 0
    #calcula as celulas ao redor volta o maximo e o caminho para chegar no maximo
    if parametros[0] != 0:
      esquerda = parametros[0].getMax() + self.gap
    if parametros[1] != 0:
      vertical = parametros[1].getMax() + self.gap
    if self.list_a[posA] == self.list_b[posB]:
      diagonal = parametros[2].getMax() + self.match
    else:
      diagonal = parametros[2].getMax() + self.mismatch
    resultados = [esquerda,vertical,diagonal]     
    resultados.sort(reverse= True)
    caminho = []
    if resultados[0] == esquerda:
      caminho.append('-') 
    if resultados[0] == vertical:
      caminho.append('|') 
    if resultados[0] == diagonal:
      caminho.append('/') 
    return [resultados[0],caminho]

  def makeMatrizFromList(self):
    resultado = [] #vai contar max e caminho [maximo,[caminhos(-/|)]]
    for i in self.list_a:
      for j in self.list_b:
        resultado = self.calculateAround((self.cellAroundExist(i[2],j[2])), i[2], j[2]) #volta a lista de celulas ao redor e calcula o maior
        resultado.append(i[2])
        resultado.append(j[2])
        self.matriz[i[2]].append(celula(i[0],j[0],resultado))
      self.matriz.append(list)
        #calcular os valores para definir o maior valor


        
