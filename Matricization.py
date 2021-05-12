from Celula import celula

class Criarmatriz():
  def __init__(self, a,b):
    self.list_a = list(a)
    self.list_b = list(b)
    matrizFromDna = self.makeMatrizFromList(self.list_a, self.list_b)
    return matrizFromDna
  
  def makeMatrizFromList(a,b):
    for i in a:
      for j in b:
        
