import numpy as np
import pandas as pd
from numpy import arccos

for i in range(1,3):
    df=pd.read_csv(f'../p{i}-20ctvao.csv')
    dc=df[['TRACK_ID','TIME','POSITION_X','POSITION_Y','VELOCITY_X','VELOCITY_Y','VELOCITY_M','ANGLE']]

    dt=dc['TIME'][1]-dc['TIME'][0]

    dc['VELOCITY_ANGLE']=dc['ANGLE']/dt
    
    dc.to_csv(f'../p{i}-20ctvao.csv')
    #print(f'finish p{i}-20ctvao.csv')
