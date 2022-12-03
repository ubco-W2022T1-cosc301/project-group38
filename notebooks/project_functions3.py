import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_process(path) :
    dataLength = 9357
    data = (
        pd.read_csv(path, sep=';', decimal=',', nrows=dataLength)
        .dropna(axis=1, how='all')
        .replace(-200,np.nan)
        
    )
    data['Time'] = data['Time'].astype(str).apply(lambda x: x[0:2]).astype(int)
    return data

def createNonMetaldf(df) :
    benzConst = 1597
    noConst = 327
    coConst = 40
    df1 = (
        pd.DataFrame(df[['CO(GT)', 'C6H6(GT)', 'NO2(GT)']])
        .div({'CO(GT)':(coConst), 'C6H6(GT)':(benzConst), 'NO2(GT)':(noConst)})
    )
    
    nonMetal = (
        pd.DataFrame(df[['Date']])
        .merge(df1, left_index=True, right_index=True)
        .replace(-200, np.nan)
        #.melt(id_vars=['Date'], value_vars=['CO(GT)', 'C6H6(GT)', 'NO2(GT)'])   
    )
    
    
    return nonMetal

def getMeans(df) :
    m = [None] * 3
    m[0] = df['C6H6(GT)'].mean()
    print(m[0])
    m[1] = df['NO2(GT)'].mean()
    m[2] = df['CO(GT)'].mean()
    return m

# Get days that are immediately dangerous for NO2 concentration
def getImmDays(df) :
    filtered = (
        pd.DataFrame(df.loc[(df['Date'] == '03/02/2005') | (df['Date'] == '11/02/2005')])
        
    )
    return filtered