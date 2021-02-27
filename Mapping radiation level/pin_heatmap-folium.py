import folium
import pandas as pd
from folium.plugins import HeatMap

df = pd.read_csv('data_aelb.csv')
data = df.filter(['lat','lon','dose'], axis=1) #or data = pd.Dataframe(df, columns=['lat', 'lon', 'dose'])

lat = data['lat'].values
lon = data['lon'].values
dose = data['dose'].values

##Creating map with pins

m1 = folium.Map(location=[2.89795, 101.754386], #location at the center of the map
                zoom_start=20, prefer_canvas=True) #max zoom_start=18

# Changing the background map type
folium.TileLayer('openstreetmap').add_to(m1)
folium.TileLayer('stamentoner').add_to(m1)
folium.TileLayer('stamenwatercolor').add_to(m1)
folium.TileLayer('cartodbpositron').add_to(m1)
folium.TileLayer('cartodbdark_matter').add_to(m1)
folium.LayerControl().add_to(m1
                            )
# Adding each home as a marker to the map
for index, row in data.iterrows():
    
    # Changing the color based on dose values
    if row['dose'] < 0.150:
        color = '#205e52'  #setting the colour
    elif row['dose'] >= 0.150 and row['dose'] < 0.200:
        color = '#32684d'    #setting the colour
    elif row['dose'] >= 0.200 and row['dose'] < 0.225:
        color = '#447349'    #setting the colour
    elif row['dose'] >= 0.225 and row['dose'] < 0.250:
        color = '#567e44'     #setting the colour
    elif row['dose'] >= 0.250 and row['dose'] < 0.275:
        color = '#688840'     #setting the colour
    elif row['dose'] >= 0.275 and row['dose'] < 0.300:
        color = '#7a923b'     #setting the colour
    elif row['dose'] >= 0.300 and row['dose'] < 0.325:
        color = '#8b9d37'     #setting the colour
    elif row['dose'] >= 0.325 and row['dose'] < 0.350:
        color = '#9da732'     #setting the colour
    elif row['dose'] >= 0.350 and row['dose'] < 0.375:
        color = '#afb22d'     #setting the colour
    elif row['dose'] >= 0.375 and row['dose'] < 0.400:
        color = '#c1bd29'     #setting the colour
    else:
        color = '#d3c724'   #setting the colour
        
    popup_text = "Latitude: {}<br> Longitude: {}<br> Dose: {:.3f}μSv/h" #Arrangement of popup text
    popup_text = popup_text.format(row["lat"],
                                   row["lon"],
                                   row["dose"])   

    folium.CircleMarker([row['lat'], row['lon']],
                        radius=5, #minimum radius=1
                        color=color,
                        fill=True,
                        popup = popup_text,
                       ).add_to(m1)
    
    
import branca.colormap as cm

step = cm.StepColormap(
    ['#205e52', '#32684d', '#447349', '#567e44', '#688840', '#7a923b', '#8b9d37', '#9da732', '#afb22d', '#c1bd29', '#d3c724'],
    vmin=0.150, vmax=0.450,
    index=[0.150, 0.200, 0.225, 0.250, 0.275, 0.300, 0.325, 0.350, 0.375, 0.400, 0.450],
    caption='Dose (μSv/h)'
).add_to(m1)

m1.save('mapping_final.html') #saving the result into html format

##Creating heatmap

m2 = folium.Map(location=[2.89795, 101.754386], #location at the center of the map
                zoom_start=17, prefer_canvas=True) #max zoom_start=18

# Setting the background map type
folium.TileLayer("Mapbox Bright").add_to(m2)

# Plotting the heatmap
heat_data = [[row['lat'],row['lon'], row['dose']] for index, row in data.iterrows()]

# Adding the heatmap to the map
HeatMap(heat_data).add_to(m2)

m2.save("Mapping_heatmap.html") #saving the result into html format
