import numpy as np
import pandas as pd

for i in range(1,5):
    df=pd.read_csv(f'../p{i}-20ctvao.csv')
    dc=df[['TRACK_ID','TIME','POSITION_X','POSITION_Y','VELOCITY_X','VELOCITY_Y','VELOCITY_M','ANGLE']]

    dt=dc['TIME'][1]-dc['TIME'][0]

    a=np.array([])

    l=len(df)
    id=-1
    for j in range(0,l):
        if id!=dc['TRACK_ID'][j]:
            id=dc['TRACK_ID'][j]
            a=np.append(a,0.0)
            
        else:
            a=np.append(a,(dc['ANGLE'][j]-dc['ANGLE'][j-1]))
            
    
    dc['VELOCITY_ANGLE']=a/dt

    dc.to_csv(f'../p{i}-20ctvaow.csv')
