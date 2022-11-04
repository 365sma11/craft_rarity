import requests
import json
import streamlit as st
import pandas as pd
import plotly_express as px
import csv
import base64
st.set_page_config(page_title="Craft Rarity Multiplier",layout='wide')

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    opacity:1;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

def plot(dataframe):
    #x_axis_val= st.selectbox('Select X-Axis Value', options=df.columns)
    #y_axis_val= st.selectbox('Select Y-Axis Value', options=df.columns)
    plot = px.scatter(dataframe,x='RANK', y='RARITY SCORE', width=1000, height=1000, color='Model', )
    #plot = px.scatter(dataframe,x=x_axis_val, y='y_axis_val', width=600, height=600, color='MODEL')
    plot.update_layout(legend_font_size=20)

    plot.update_layout(
        yaxis = dict(
        tickfont = dict(size=20)))
    plot.update_layout(
        xaxis = dict(
        tickfont = dict(size=20)))
    plot.update_xaxes(
        title_font = {"size": 20})
    plot.update_yaxes(
        title_font = {"size": 20})
    plot.update_layout({
        'plot_bgcolor': 'rgba(71, 71, 71, 0.5)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',})

    

    st.plotly_chart(plot)
    

set_background('craft.png')
st.title ('Crafts Rarity - Model Multiplier Compare')
st.sidebar.title("MODEL MULTIPLIER")
options=st.sidebar.radio('MODEL MULTIPLIER',options=['NO MULTIPLIER','5X','10X','25X','50X','100X'])



if options == 'NO MULTIPLIER':
    df=pd.read_csv("crafts_rank1x.csv")
    plot(df)

elif options == '5X':
    df=pd.read_csv("crafts_rank5x.csv")
    plot(df)

elif options == '10X':
    df=pd.read_csv("crafts_rank10x.csv")
    plot(df)

elif options == '25X':
    df=pd.read_csv("crafts_rank25x.csv")
    plot(df)

elif options == '50X':
    df=pd.read_csv("crafts_rank50x.csv")
    plot(df)

elif options == '100X':
    df=pd.read_csv("crafts_rank100x.csv")
    plot(df)



