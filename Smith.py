import GapCalculator as gap
from Matricization import Criarmatriz

dnaA = "tgcccaagtgctgccaaa"
dnaB = "gcctagtccatgatggta"
dnaA = gap.start(dnaA)
dnaB = gap.start(dnaB)
table = Criarmatriz(dnaA, dnaB)

print(table)