def dnagap(t):
  tempgap = []
  for i in range(0, len(t)):
    x= (i + 1) * -2
    tempgap.append(x)
  return tempgap

def count(x):
  contagem = []
  for i in range(0,len(x)):
    contagem.append((i))
  return contagem

def start(t:str):
  dna=list(t)
  return zip(dna,dnagap(dna), count(dna))