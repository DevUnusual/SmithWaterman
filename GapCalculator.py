def dnagap(t, gap):
  tempgap = []
  for i in range(0, len(t)):
    x= (i + 1) * gap
    tempgap.append(x)
  return tempgap

def count(x):
  contagem = []
  for i in range(0,len(x)):
    contagem.append((i))
  return contagem

def start(t:str, gap):
  dna=list(t)
  return zip(dna,dnagap(dna,gap), count(dna))