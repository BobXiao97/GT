import streamlit as st
from GTModel import *

st.set_page_config(layout='wide')
st.header('Matching Game')
st.subheader('Passenger 1')
col1,col2,col3,col4=st.columns(4)
dist1=col1.radio('Distance in km',[10,15,20],key='dist1')
transport1=col2.radio('Transport',['JustGrab','GrabTaxi','Hailing'],key='transport1')
alpha1=col3.number_input('Alpha',value=0.01,step=0.01,key='alpha1')
col4.write('Preference')
pref1_1=col4.number_input('Taxi 1',min_value=1,max_value=4,key='pref1_1',value=1)
pref1_2=col4.number_input('Taxi 2',min_value=1,max_value=4,key='pref1_2',value=2)
pref1_3=col4.number_input('Taxi 3',min_value=1,max_value=4,key='pref1_3',value=3)
pref1_4=col4.number_input('Taxi 4',min_value=1,max_value=4,key='pref1_4',value=4)

st.subheader('Passenger 2')
col5,col6,col7,col8=st.columns(4)
dist2=col5.radio('Distance in km',[10,15,20],key='dist2')
transport2=col6.radio('Transport',['JustGrab','GrabTaxi','Hailing'],key='transport2')
alpha2=col7.number_input('Alpha',value=0.01,step=0.01,key='alpha2')
col8.write('Preference')
pref2_1=col8.number_input('Taxi 1',min_value=1,max_value=4,key='pref2_1',value=2)
pref2_2=col8.number_input('Taxi 2',min_value=1,max_value=4,key='pref2_2',value=3)
pref2_3=col8.number_input('Taxi 3',min_value=1,max_value=4,key='pref2_3',value=4)
pref2_4=col8.number_input('Taxi 4',min_value=1,max_value=4,key='pref2_4',value=1)

st.subheader('Passenger 3')
col9,col10,col11,col12=st.columns(4)
dist3=col9.radio('Distance in km',[10,15,20],key='dist3')
transport3=col10.radio('Transport',['JustGrab','GrabTaxi','Hailing'],key='transport3')
alpha3=col11.number_input('Alpha',value=0.02,step=0.01,key='alpha3')
col12.write('Preference')
pref3_1=col12.number_input('Taxi 1',min_value=1,max_value=4,key='pref3_1',value=3)
pref3_2=col12.number_input('Taxi 2',min_value=1,max_value=4,key='pref3_2',value=1)
pref3_3=col12.number_input('Taxi 3',min_value=1,max_value=4,key='pref3_3',value=4)
pref3_4=col12.number_input('Taxi 4',min_value=1,max_value=4,key='pref3_4',value=2)

st.subheader('Passenger 4')
col13,col14,col15,col16=st.columns(4)
dist4=col13.radio('Distance in km',[10,15,20],key='dist4')
transport4=col14.radio('Transport',['JustGrab','GrabTaxi','Hailing'],key='transport4')
alpha4=col15.number_input('Alpha',value=0.02,step=0.01,key='alpha4')
col16.write('Preference')
pref4_1=col16.number_input('Taxi 1',min_value=1,max_value=4,key='pref4_1',value=3)
pref4_2=col16.number_input('Taxi 2',min_value=1,max_value=4,key='pref4_2',value=4)
pref4_3=col16.number_input('Taxi 3',min_value=1,max_value=4,key='pref4_3',value=2)
pref4_4=col16.number_input('Taxi 4',min_value=1,max_value=4,key='pref4_4',value=1)

st.subheader('Passenger 5')
col17,col18,col19,col20=st.columns(4)
dist5=col17.radio('Distance in km',[10,15,20],key='dist5')
transport5=col18.radio('Transport',['JustGrab','GrabTaxi','Hailing'],key='transport5')
alpha5=col19.number_input('Alpha',value=0.05,step=0.01,key='alpha5')
col20.write('Preference')
pref5_1=col20.number_input('Taxi 1',min_value=1,max_value=4,key='pref5_1',value=4)
pref5_2=col20.number_input('Taxi 2',min_value=1,max_value=4,key='pref5_2',value=2)
pref5_3=col20.number_input('Taxi 3',min_value=1,max_value=4,key='pref5_3',value=3)
pref5_4=col20.number_input('Taxi 4',min_value=1,max_value=4,key='pref5_4',value=1)

pref_list1=[pref1_1,pref1_2,pref1_3,pref1_4,5]
pref_list2=[pref2_1,pref2_2,pref2_3,pref2_4,5]
pref_list3=[pref3_1,pref3_2,pref3_3,pref3_4,5]
pref_list4=[pref4_1,pref4_2,pref4_3,pref4_4,5]
pref_list5=[pref5_1,pref5_2,pref5_3,pref5_4,5]
p1={'distance':dist1,'transport':transport1,'alpha':alpha1,'pref':pref_list1}
p2={'distance':dist2,'transport':transport2,'alpha':alpha2,'pref':pref_list2}
p3={'distance':dist3,'transport':transport3,'alpha':alpha3,'pref':pref_list3}
p4={'distance':dist4,'transport':transport4,'alpha':alpha4,'pref':pref_list4}
p5={'distance':dist5,'transport':transport5,'alpha':alpha5,'pref':pref_list5}

if st.button('Start Calculation'):
    proposals=solution(p1,p2,p3,p4,p5)
    result=post_processing(proposals)
    st.write(result)
