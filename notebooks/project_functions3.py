import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_process(path) :
    dataLength = 9357
    data = pd.read_csv(path, sep=';', decimal=',', nrows=dataLength).dropna(axis=1, how='all')
    return data

def createNonMetaldf(df) :
    nonMetal = pd.DataFrame(df[['Date', 'CO(GT)', 'C6H6(GT)', 'NO2(GT)']])
    nonMetal = nonMetal.replace(-200, np.nan)
    return nonMetal

def getMeans(df) :
    m = [3]
    m[0] = dNonMetal['C6H6(GT)'].mean()
    m[1] = dNonMetal['NO2(GT)'].mean()
    m[2] = dNonMetal['CO(GT)'].mean()