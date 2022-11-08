import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def load_and_process(path):
    df = ( pd.read_csv(path,sep=';')
        .drop(['Unnamed: 15','Unnamed: 16','NMHC(GT)'],axis=1)
        .dropna(how='any'))
    df = df[(df != -200).all(1)]
    
    return df

def setup_datetime(df: pd.DataFrame):
    df['datetime'] = pd.to_datetime(df['Date'], format="%d/%m/%Y")
    df['month'] = df['datetime'].dt.month_name()
    df['Time'] = df['Time'].astype(str).apply(lambda x : x[0:2]).astype(int)
    
    return df

def fixFormat(df):
    df['T'] = df['T'].astype(str).replace(",",".",regex=True).astype(float)
    df['RH'] = df['RH'].astype(str).replace(",",".",regex=True).astype(float)
    df['AH'] = df['AH'].astype(str).replace(",",".",regex=True).astype(float)
    
    return df

def _toCommonName(name):
    if name == 'PT08.S1(CO)':
        return "Tin Oxide"
    elif name == 'PT08.S2(NMHC)':
        return "Titanium Dioxide"
    elif name == 'PT08.S3(NOx)':
        return "Tungsten Oxide(NOx)"
    elif name == 'PT08.S4(NO2)':
        return "Tungsten Oxide(NO2)"
    elif name == 'PT08.S5(O3)':
        return "Indium Oxide"
    else:
        return "Unknown"
    
def _toMetalDataTbl(data: pd.DataFrame,colName: str):
    df = pd.DataFrame()
    df['T'] = data['T']
    df['RH'] = data['RH']
    df['AH'] = data['AH']
    df['Value'] = data[colName]
    df['Type'] = _toCommonName(colName)

    return df

def setup_metalData(df):
    metalData = pd.DataFrame(columns=['T','RH','AH','Value','Type'])
    metalData = pd.concat([metalData,
                        _toMetalDataTbl(df,"PT08.S1(CO)"),
                        _toMetalDataTbl(df,"PT08.S2(NMHC)"),
                        _toMetalDataTbl(df,"PT08.S3(NOx)"),
                        _toMetalDataTbl(df,"PT08.S4(NO2)"),
                        _toMetalDataTbl(df,"PT08.S5(O3)")
                        ])
    return metalData