class celula:

  def __init__(self, A, B, parametros):
    self.FoundLeft = False
    self.Foundtop = False
    self.FoundDiagonal = False
    
    self.A = A
    self.B = B
    self.mismatch = parametros[0]
    self.match = parametros[1]
    self.gap = parametros[2]
    self.CelLeft = A[2]
    self.CelDown = B[2]
    self.CelDiagonal = [0]
    if B[2] != 0:
      self.CelLeft = [A[2], (B[2]-1)]
      self.FoundLeft = True
    if A[2] != 0:
      self.CelDown = [(A[2]-1), B[2]]
      self.FoundTop = True
    if B[2] != 0 and A[2] != 0:
      self.CelDiagonal = [(A[2]-1),(B[2]-1)]
      self.FoundDiagonal = False
    self.Caminho =[] # < pela esquerda, / diagonal, | vertical
    self.Resultados = self.calculate(self) #primeiro campo pela esquerda, segundo pela diagonal e terceiro vertical
    self.MaiorResultado = self.Resultados.pop
    print("esquerda:"+ str(self.CelLeft) + "Abaixo: " + str(self.CelDown) + "diagonal" + str(self.CelDiagonal))
  
  def calculate(self):
    if not self.FoundLeft:
      self.Resultados.append(self.A[2] + self.gap)
    else:
      self.Resultados.append() 