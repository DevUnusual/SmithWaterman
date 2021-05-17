class celula:

  def __init__(self, A, B, parametros):
    self.letterA = A[0]
    self.letterB = B[0]
    self.Max = [parametros[0], parametros[1]]
    self.posicao = [parametros[2], parametros[3]]
  
  def setMax(self,parametros):
    self.Max = [parametros[0], parametros[1]]
  
  def getMax(self):
    return self.Max[0]
