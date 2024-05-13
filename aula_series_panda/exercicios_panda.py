import numpy as np
import pandas as pd

def stats(series:pd.Series)->list:
    return [np.std(series.values),np.mean(series.values)]

def freq(series:pd.Series)->pd.Series:
    return pd.value_counts(series.values)

def mult(series):
    return series[series.values%5==0].index[0]

def freq_filter(series:pd.Series):
    mode = freq(series).sort_values(ascending=False).index[0]
    series[series.values!=mode] = 'Desconsiderar'
    return series

def frequencia(serie):
    return pd.value_counts(serie.values)

def overlap(serie_1, serie_2):
    return serie_1.loc[serie_1.values == serie_2.values].index

def not_overlap(serie_1, serie_2):
    not_overlap_1 = serie_1.loc[serie_1.values != serie_2.values].values
    not_overlap_2 = serie_2.loc[serie_1.values != serie_2.values].values
    
    not_overlap_total = np.concatenate([not_overlap_1, not_overlap_2])
    return not_overlap_total

