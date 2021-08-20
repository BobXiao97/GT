p1={'distance':10,'transport':'JustGrab','alpha':0.01,'pref':[1,2,3,4,5]}
p2={'distance':10,'transport':'GrabTaxi','alpha':0.01,'pref':[2,3,4,1,5]}
p3={'distance':15,'transport':'JustGrab','alpha':0.02,'pref':[3,1,4,2,5]}
p4={'distance':15,'transport':'GrabTaxi','alpha':0.02,'pref':[3,4,2,1,5]}
p5={'distance':20,'transport':'Hailing','alpha':0.05,'pref':[4,2,3,1,5]}
# t5就是那辆不存在的汽车

import pandas as pd
from copy import deepcopy
from copy import copy
import numpy as np
from collections import Counter

# 乘客要花多少钱
def fee_calculation(passenger):
    distance=passenger['distance']
    transport=passenger['transport']
    if transport=='JustGrab':
        if distance==10:
            fee=11.3
        if distance==15:
            fee=14.3
        if distance==20:
            fee=19.3
    if transport=='GrabTaxi':
        if distance==10:
            fee=13.8
        if distance==15:
            fee=17.8
        if distance==20:
            fee=21.9
    if transport=='Hailing':
        if distance==10:
            fee=9.8
        if distance==15:
            fee=13.8
        if distance==20:
            fee=17.9
    return fee

# 司机能赚多少钱
def earning(passenger):
    distance=passenger['distance']
    transport=passenger['transport']
    if transport=='JustGrab':
        if distance==10:
            fee=7.5
        if distance==15:
            fee=9.2
        if distance==20:
            fee=12.4
    if transport=='GrabTaxi':
        if distance==10:
            fee=12.0
        if distance==15:
            fee=15.2
        if distance==20:
            fee=18.6
    if transport=='Hailing':
        if distance==10:
            fee=8.3
        if distance==15:
            fee=11.5
        if distance==20:
            fee=14.9
    return fee

# 乘客最后的总花费（钱+alpha*时间）
def passenger_cost(passenger):
    distance=passenger['distance']
    alpha=passenger['alpha']
    if distance==10:
        cost=fee_calculation(passenger)+alpha*(163+557+240)
    if distance==15:
        cost=fee_calculation(passenger)+alpha*(230+790+360)
    if distance==20:
        cost=fee_calculation(passenger)+alpha*(320+1179+600)
    return round(cost,1)

# 求得最后分配的方式
def solution(p1,p2,p3,p4,p5):
    passenger_list=['p1','p2','p3','p4','p5']
    taxi_list=['t1','t2','t3','t4','t5']
    p1_fee=fee_calculation(p1)
    p2_fee=fee_calculation(p2)
    p3_fee=fee_calculation(p3)
    p4_fee=fee_calculation(p4)
    p5_fee=fee_calculation(p5)
    fee_list=[p1_fee,p2_fee,p3_fee,p4_fee,p5_fee]
    fee_sort=deepcopy(fee_list)
    fee_sort.sort(reverse=True)

    taxi_pref_list=[0,0,0,0,0]
    for i in range(len(fee_sort)):
        for j in range(len(fee_list)):
            if fee_sort[i]==fee_list[j]:
                taxi_pref_list[j]=i+1
    taxi_pref_dict={}
    for k in range(len(taxi_pref_list)):
        key='p'+str(k+1)
        taxi_pref_dict[key]=[taxi_pref_list[k]]*5
    taxi_df=pd.DataFrame(taxi_pref_dict)
    taxi_df.index=taxi_list

    passenger_df=pd.DataFrame({'p1':p1['pref'],'p2':p2['pref'],'p3':p3['pref'],'p4':p4['pref'],'p5':p5['pref']})
    passenger_df.index=taxi_list 

    passenger_available={taxi:passenger_list for taxi in taxi_list}
    waiting_list=[]
    proposals={}
    while len(waiting_list)<len(taxi_list):
        for taxi in taxi_list:
            if taxi not in waiting_list:
                passenger = passenger_available[taxi]
                best_choice = taxi_df.loc[taxi][taxi_df.loc[taxi].index.isin(passenger)].idxmin()
                proposals[(taxi, best_choice)]=(taxi_df.loc[taxi][best_choice],passenger_df.loc[taxi][best_choice])
        overlays = Counter([key[1] for key in proposals.keys()])
        for passenger in overlays.keys():
            if overlays[passenger]>1:
                pairs_to_drop = sorted({pair: proposals[pair] for pair in proposals.keys() if passenger in pair}.items(), key=lambda x: x[1][1])[1:]

                for p_to_drop in pairs_to_drop:
                    del proposals[p_to_drop[0]]
                    _passenger = copy(passenger_available[p_to_drop[0][0]])
                    _passenger.remove(p_to_drop[0][1])
                    passenger_available[p_to_drop[0][0]] = _passenger
        waiting_list = [taxi[0] for taxi in proposals.keys()]
    return proposals

# 把前面的结果调整下变成一个Dataframe
def post_processing(proposals):
    passenger_list=['p1','p2','p3','p4','p5']
    key=list(proposals.keys())
    val=list(proposals.values())
    taxi_result=[0,0,0,0,0]
    pref_list=[0,0,0,0,0]
    for i in range(len(key)):
        for j in range(len(passenger_list)):
            if key[i][1]==passenger_list[j]:
                taxi_result[j]=key[i][0]
                pref_list[j]=val[i][1]
    cost_list=[passenger_cost(p1),passenger_cost(p2),passenger_cost(p3),passenger_cost(p4),passenger_cost(p5)]
    index=taxi_result.index('t5')
    taxi_result[index]=None
    pref_list[index]=None
    cost_list[index]=None
    result=pd.DataFrame({'Taxi':taxi_result,'Pref':pref_list,'Cost':cost_list})
    result.index=passenger_list
    return result




