import sqlite3
import folium
import pandas as pd

def maps(b):
    conn = sqlite3.connect("mydatabase_2.db")
    df = pd.read_sql("SELECT * FROM coordinates", conn) 
    
    def color_change(yavka):
        if(yavka < 30):
            return('green')
        elif(30 <= yavka < 60):
            return('orange')
        else:
            return('red')
    
    def popup_html(i):
        html = '<h5> УИК № {}</h5>'.format(df.iloc[i,0])
        html += '<br><b> Амосов Михаил Иванович </b>: {} %'.format(b.iloc[i,15])
        html += '<br><b> Беглов Александр Дмитриевич </b>: {} %'.format(b.iloc[i,16])
        html += '<br><b> Тихонова Надежда Геннадьевна </b>: {} %'.format(b.iloc[i,17])
        html += '<br><b> Явка </b>: {} %'.format(b.iloc[i,19])
        return html

    
    map = folium.Map(location=[59.976040,30.45], 
                 tiles= 'cartodbpositron',
                 zoom_start = 11.5)

    tooltip = 'Click me!'

    for i in range(b.shape[0]):
        folium.Marker(location=[df.iloc[i,1],df.iloc[i,2]],
                  popup = folium.Popup(popup_html(i), max_width=700, height=250),
                  icon=folium.Icon(color = color_change(b.iloc[i,19]), icon='cloud')).add_to(map)
    
    map.save("Результаты_выборов.html")