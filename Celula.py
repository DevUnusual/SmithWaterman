class celula:
  def __init__(self, A, B):
    print('oi')
    CelLeft = A[2]
    CelDown = B[2]
    CelDiagonal = [0]
    if B[2] != 0:
      CelLeft = [A[2], (B[2]-1)]
    if A[2] != 0:
      CelDown = [(A[2]-1), B[2]]
    if B[2] != 0 and A[2] != 0:
      CelDiagonal = [(A[2]-1),(B[2]-1)]
    print("esquerda:"+ str(CelLeft) + "Abaixo: " + str(CelDown) + "diagonal" + str(CelDiagonal))