import GapCalculator as gap
from Matricization import Criarmatriz as Matriz

dnaA = "tgcccaagtgctgccaaa"
dnaB = "gcctagtccatgatggta"
parametros = [1,-1,-2] #definir os parametros de calculo [match, mismatch, gap]
dnaA = gap.start(dnaA, parametros[2])
dnaB = gap.start(dnaB, parametros[2])
table = Matriz(dnaA, dnaB, parametros)

print(table)