#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import statistics as st
import matplotlib.pyplot as plt
import plotly.offline as offline
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff

from web3 import Web3 
web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/fbff721384cf4ceb95fcf8c18a249f95"))

def graf(text):
    x=[]
    for i in range(1000):
        x.append(i)
    fig1 = go.Figure(data=[go.Bar( 
                             y=df[text], 
                             x=x, 
                             hovertext=['27% market share', '24% market share', '19% market share'])])
    fig1.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.6)
    fig1.update_layout(title_text=text)
    fig1.show()
    fig1.write_html(text+'.html', auto_open=True)

St = 8921400
End = 8922400
allprice = []
allpercent = []
allcommission = []
allkontr = []

for i in range(St, St+End):
    block = web3.eth.getBlock(i)
    commission = 0
    kontr = 0
    for trans in block['transactions']:
        tr = web3.eth.getTransaction(trans)
        tr_r = web3.eth.getTransactionReceipt(trans)
        commission += web3.fromWei(tr_r['gasUsed']*tr['gasPrice'], 'ether')
        if tr['input'] != '0x':
            kontr += 1
    allkontr.append(kontr)
    allcommission.append(float(commission))
    price = 2+commission
    allprice.append(float(price)+2*len(block.uncles)/32)
    allpercent.append(float((commission/price)*100))

d = {'Commission': allcommission,'All Priсe': allprice, 'Percent': allpercent, 'All contracts': allkontr}
df = pd.DataFrame(d)

graf('Commission')
graf('Percent')

Result = {'Математическое ожидание': df.Commission.mean(), 
          'Медиана': df.Commission.median(), 
          'Среднеквадратичное отклонение': df.Commission.std(),
          'Дисперсия': df.Commission.var(),
          'Размах':max(df['Commission']) - min(df['Commission'])}