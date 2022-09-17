import numpy as np
import pandas as pd
from numpy import arccos

for i in range(4,5):
    df=pd.read_csv(f'../p{i}-20ctva.csv')
    dc=df[['TRACK_ID','TIME','POSITION_X','POSITION_Y','VELOCITY_X','VELOCITY_Y','VELOCITY_M']]

    l=len(df)
    id=-1
    c=0
    a=np.array([])
    for j in range(0,l):
        if id!=dc['TRACK_ID'][j]:
            id=dc['TRACK_ID'][j]
            c=0
            a=np.append(a,0)
            ##print("salto de traqueo")
            
        elif c<1:
            c+=1
            a=np.append(a,0)

        else:
            #print("puntos:")
            #print(f"({dc['POSITION_X'][j-2]},{dc['POSITION_Y'][j-2]})")
            #print(f"({dc['POSITION_X'][j-1]},{dc['POSITION_Y'][j-1]})")
            #print(f"({dc['POSITION_X'][j]},{dc['POSITION_Y'][j]})")

            p=np.array([dc['POSITION_X'][j-1],dc['POSITION_Y'][j-1]])
            v1=np.array([dc['POSITION_X'][j-2],dc['POSITION_Y'][j-2]])-p
            v2=np.array([dc['POSITION_X'][j],dc['POSITION_Y'][j]])-p

            #print("vectores:")
            #print(f"{v1}")
            #print(f"{v2}")
            if np.linalg.norm(v1)!=0 and np.linalg.norm(v2)!=0 and v1[0]!=v2[0] and v1[1]!=v2[1]:
                a=np.append(a,arccos(np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))))
            else:
                a=np.append(a,0)

            """
            try:
                vv=np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
                o=arccos(vv) if np.linalg.norm(v1)!=0 and np.linalg.norm(v2)!=0 else 0.0
            except RuntimeWarning:
                print(f"valor invalido: {np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))}")
                
            print("angulo:")
            print(f"{o}\n")
            """

    dc['ANGLE']=a.tolist()
    
    dc.to_csv(f'../p{i}-20ctvao.csv')
    #print(f'finish p{i}-20ctvao.csv')
