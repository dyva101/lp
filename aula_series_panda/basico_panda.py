import numpy as np
import pandas as pd
import exercicios_panda as ex

dicionario_1 = {"A": 4, "B": 2500, "C": 18, "D": 23}
dicionario_2 = {"W": 16, "X": 2500, "Y": 25 , "Z": 23}
 
ser_1 = pd.Series(dicionario_1)
ser_2 = pd.Series(dicionario_2)

print("\n\nMédia e Desvio Padrão:\n", ex.stats(ser_1))
print("\n\nFrequência:\n", ex.freq(ser_1))
print("\nIntersecção das Séries:\n", ex.overlap(ser_1, ser_2))
print("\nFiltro de elementos menos frequentes:\n", ex.freq_filter(ser_1))
print("\nConjunto Complementar à Intersecção:\n", ex.not_overlap(ser_1, ser_2))
print("\nMúltiplos de 5:\n", ex.mult(ser_2))