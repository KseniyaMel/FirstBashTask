import pandas as pd
import numpy as np
from numpy import mean
from numpy import std
import matplotlib.pyplot as plt
import plotly.offline as offline
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff


def reganal(n1,n2,b):
    x = []
    y = []
    for i in b.iloc[:,n1]:
        x.append(i)
    for j in b.iloc[:,n2]:
        y.append(j)
    
    x = np.array(x)
    y = np.array(y)

    denominator = x.dot(x) - x.mean()*x.sum()
    a = (x.dot(y) - y.mean()*x.sum()) / denominator
    с = (y.mean()*x.dot(x) - x.mean()*x.dot(y)) / denominator

    yath = a*x + с
    return yath

def anomal(n,b):
    data_mean, data_std = mean(b[n]), std(b[n])
    cut_off = data_std * 3
    lower, upper = data_mean - cut_off, data_mean + cut_off
    outliers = [x for x in b[n] if x < lower or x > upper]
    print('Количество аномальных чисел распределения "',n, '" : %d' % len(outliers))
    outliers_removed = [x for x in b[n] if x > lower and x < upper]
    print('Количество нормальных чисел распределения "',n,'" : %d' % len(outliers_removed))
    return(len(outliers))
    
    
def gf(b):
    
    fig1 = go.Figure()

    fig1.add_trace(go.Scatter(
            x = b['Амосов Михаил Иванович'], 
            y = b['Явка'],
            name = 'Амосов Михаил Иванович',
            mode = 'markers',
            marker_color='#18F018'))
    fig1.add_trace(go.Scatter(
            x = b['Амосов Михаил Иванович'],
            y = reganal(12,18,b),
            marker_color='#18F018',
            name = 'Количество аномальных чисел распределения "Амосов Михаил Иванович" : %d' % anomal('Амосов Михаил Иванович',b)))

    fig1.add_trace(go.Scatter(
            x = b['Беглов Александр Дмитриевич'], 
            y = b['Явка'],
            name = 'Беглов Александр Дмитриевич',
            mode = 'markers',
            marker_color='#F01818',
            legendgroup="group2"))
    fig1.add_trace(go.Scatter(
            x = b['Беглов Александр Дмитриевич'], 
            y = reganal(13,18,b),
            name = 'Количество аномальных чисел распределения "Беглов Александр Дмитриевич" : %d' % anomal('Беглов Александр Дмитриевич',b),
            marker_color='#F01818',
            legendgroup="group2"))

    fig1.add_trace(go.Scatter(
            x = b['Тихонова Надежда Геннадьевна'], 
            y = b['Явка'],
            name = 'Тихонова Надежда Геннадьевна',
            mode = 'markers',
            marker_color='#F018F0',
            legendgroup="group3"))
    fig1.add_trace(go.Scatter(
            x = b['Тихонова Надежда Геннадьевна'], 
            y = reganal(14,18,b),
            name = 'Количество аномальных чисел распределения "Тихонова Надежда Геннадьевна" : %d' % anomal('Тихонова Надежда Геннадьевна',b),
            marker_color='#F018F0',
        legendgroup="group3"))
            
    fig1.update_layout(title='Зависимость количества голосов за кандидата от явки')
    fig1.write_html('Зависимость_количества_голосов_за_кандидата_от_явки.html', auto_open=True)



    fig2 = go.Figure()

    fig2.add_trace(go.Scatter(
            x = b['Явка'], 
            y = b['Число избирателей, внесенных в список избирателей на момент окончания голосования'], 
            name = 'Явка',
            mode = 'markers',
            marker_color='#18F018',
            legendgroup="group4"))
    fig2.add_trace(go.Scatter(
            x = b['Явка'],
            y = reganal(18,1,b),
            marker_color='#18F018',
            name = 'Количество аномальных чисел распределения "Явка" : %d' % anomal('Явка',b),
            legendgroup="group4"))

    fig2.update_layout(title='Зависимость явки от количества избирателей на участке')
    fig2.write_html('Зависимость_явки_от_количества_избирателей_на_участке.html', auto_open=True)


    group_labels = ['Явка'] # name of the dataset
    x = [b['Явка']]
    fig = ff.create_distplot(x, group_labels, show_hist=False)
    fig.update_layout(title='Зависимость явки и количества избирательных участков')
    fig.write_html('Зависимость_явки_и_количества_избирательных_участков.html', auto_open=True)
