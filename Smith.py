import GapCalculator as gap
import Matricization as Matriz

dnaA = "tgcccaagtgctgccaaa"
dnaB = "gcctagtccatgatggta"
dnaA = gap.start(dnaA)
dnaB = gap.start(dnaB)
table = Matriz(dnaA, dnaB)

print(table)