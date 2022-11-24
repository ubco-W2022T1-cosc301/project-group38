import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def load_and_clean(path):
    col=['DATE','TIME','CO_GT','PT08_S1_CO','NMHC_GT','C6H6_GT','PT08_S2_NMHC',
     'NOX_GT','PT08_S3_NOX','NO2_GT','PT08_S4_NO2','PT08_S5_O3','T','RH','AH']

    r=list(np.arange(len(col)))

    AirQuality=pd.read_csv(path,sep=";",header=None,skiprows=1,names=col,na_filter=True,
                   na_values="na",usecols=r)
    
    AirQuality.dropna(how='any',inplace=True)
    
    AirQuality =  AirQuality[( AirQuality != -200).all(1)]

    return AirQuality

def fix_Time(AirQuality: pd.DataFrame):
    AirQuality['DATE']=pd.to_datetime(AirQuality.DATE, format='%d/%m/%Y')
    AirQuality['MONTH']= AirQuality['DATE'].dt.month  
    AirQuality['HOUR']=AirQuality['TIME'].apply(lambda x: int(x.split('.')[0]))
    
    return AirQuality

def fix_Data(AirQuality):
    AirQuality['CO_GT']=AirQuality['CO_GT'].astype(str).replace(",",".",regex=True).astype(float)
    AirQuality['T'] = AirQuality['T'].astype(str).replace(",",".",regex=True).astype(float)
    AirQuality['RH'] = AirQuality['RH'].astype(str).replace(",",".",regex=True).astype(float)
    AirQuality['AH'] = AirQuality['AH'].astype(str).replace(",",".",regex=True).astype(float)
    AirQuality['C6H6_GT'] = AirQuality['C6H6_GT'].astype(str).replace(",",".",regex=True).astype(float)
    
    return AirQuality
