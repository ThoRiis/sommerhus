import pandas as pd
from altair.vegalite.v4.api import value
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st



def _max_width_():
        max_width_str = f"max-width: 1000px;"
        st.markdown(
            f"""
        <style>
        .reportview-container .main .block-container{{
            {max_width_str}
        }}
        </style>    
        """,
            unsafe_allow_html=True,
        )

_max_width_()

################################################
#
#
# Initializing
#
#
################################################





st.sidebar.title('Inputs')


lejeindtægter = st.sidebar.number_input('Lejeindtægter',value= 50000)
ejerudgifter = st.sidebar.number_input('Ejerudgifter',value= 10000)
vedligehold = st.sidebar.number_input('Vedligeholdelsesudgifter',value= 5000)
finansieringsomkostninger = st.sidebar.number_input('Finansieringsomkostninger',value= 5000)
forbrugsomkostninge = st.sidebar.number_input('forbrugsomkostninge',value= 5000)


Salgspris = st.sidebar.number_input('Salgspris',value= 200000)

data_sommerhus = { 

        'lejeindtægter':[lejeindtægter],
        'ejerudgifter':[ejerudgifter*-1],
        'vedligehold':[vedligehold*-1],
        'finansieringsomkostninger':[finansieringsomkostninger*-1],
        'forbrugsomkostninge':[forbrugsomkostninge*-1]

                }


df_sommerhus = pd.DataFrame.from_dict(data_sommerhus)

try:

    df_sommerhus['skat'] = max((lejeindtægter -43000)*0.4*0.5,0)
    df_sommerhus['profit'] = lejeindtægter -lejeindtægter - ejerudgifter - vedligehold -finansieringsomkostninger -forbrugsomkostninge -df_sommerhus['skat']
except:
    pass


st.title('Sommerhusberegner')





#plot

y_values = df_sommerhus[[
    'lejeindtægter',
    'ejerudgifter',
    'vedligehold',
    'finansieringsomkostninger',
    'forbrugsomkostninge',
    'skat',
    'profit',
    ]].copy()




fig = go.Figure(go.Waterfall(
            #name = "20", orientation = "v",
            measure = ["relative","relative", "relative","relative","relative", "relative", "total"],
            x =["leje<br>indtægt","Ejerudgift","Vedligehold", "Finansiering" ,"Forbrug","skat", "profit"] ,
            textposition = "outside",
            text = y_values.values,
            y = y_values.iloc[0],
            connector = {"line":{"color":"rgb(63, 63, 63)"}},
            )
            )
fig.update_layout(
            autosize=True,
            plot_bgcolor="#F9F9F9",
            paper_bgcolor="#F9F9F9",
            width=1100,height=600

            )




st.plotly_chart(fig)

