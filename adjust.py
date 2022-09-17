import numpy as np
import pandas as pd

for i in range(1,5):
    df=pd.read_csv(f'../p{i}-20ctv.csv')
    dc=df[['TRACK_ID','TIME','POSITION_X','POSITION_Y','VELOCITY_X','VELOCITY_Y','VELOCITY_M']]

    l=len(df)
    id=-1
    ox=0
    oy=0
    for j in range(0,l):
        if id!=dc['TRACK_ID'][j]:
            id=dc['TRACK_ID'][j]
            ox=dc['POSITION_X'][j]
            oy=dc['POSITION_Y'][j]
            dc['POSITION_X'][j]=0
            dc['POSITION_Y'][j]=0

        else:
            dc['POSITION_X'][j]-=ox
            dc['POSITION_Y'][j]-=oy

    
    
    dc.to_csv(f'../p{i}-20ctva.csv')
