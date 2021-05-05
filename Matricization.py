def Criarmatriz(a, b):
  temporario = []
  matriz = []
  list_a = list(a)
  list_b = list(b)
  for i in list_a:
    for j in list_b:
      temporario.append(i + j)
    matriz.append(temporario)
    temporario = []
  return matriz