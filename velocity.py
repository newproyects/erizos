import numpy as np
import pandas as pd

for i in range(1,5):
    df=pd.read_csv(f'../p{i}-20ct.csv')
    dc=df[['TRACK_ID','TIME','POSITION_X','POSITION_Y']]

    vx=np.array([])
    vy=np.array([])

    l=len(df)
    id=-1
    for j in range(0,l):
        if id!=dc['TRACK_ID'][j]:
            id=dc['TRACK_ID'][j]
            vx=np.append(vx,0.0)
            vy=np.append(vy,0.0)
            
        else:
            vx=np.append(vx,(dc['POSITION_X'][j]-dc['POSITION_X'][j-1])/(dc['TIME'][j]-dc['TIME'][j-1]))
            vy=np.append(vy,(dc['POSITION_Y'][j]-dc['POSITION_Y'][j-1])/(dc['TIME'][j]-dc['TIME'][j-1]))
            
    
    dc['VELOCITY_X']=vx.tolist()
    dc['VELOCITY_Y']=vy.tolist()
    dc['VELOCITY_M']=np.sqrt(vx**2+vy**2).tolist()

    dc.to_csv(f'../p{i}-20ctv.csv')
