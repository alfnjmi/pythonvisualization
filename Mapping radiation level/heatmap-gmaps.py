import pandas as pd
import googlemaps
import gmaps
API_KEY = 'AIz...........' # Your Google API key

df=pd.read_csv('data_aelb.csv')  # read geocoded location from file

locations = df[['lat', 'lon']]        
# put latitide and longitude as a variable name 'locations'
val = df['dose'] 

data = df.filter(['lat', 'lon', 'dose'], axis=1)# put the weight into variable name 'val'

geocode_result = gm.geocode('Lembaga Perlesenan Tenaga Atom')[0]  # change the name into your city of interest

# coordinate of the location
center_lat=geocode_result['geometry']['location']['lat']
center_lng=geocode_result['geometry']['location']['lng']
print('center=',center_lat,center_lng)

def drawHeatMap(location, val, zoom, intensity, radius):
    # setting the data and parameters
    heatmap_layer = gmaps.heatmap_layer(locations, val, dissipating = True)
    heatmap_layer.max_intensity = intensity
    heatmap_layer.point_radius = radius
    # draw the heatmap into a figure
    fig = gmaps.figure()
    fig = gmaps.figure(center = [center_lat,center_lng], zoom_level=zoom)
    fig.add_layer(heatmap_layer)
    return fig
   
# parameters
zoom=18
intensity=1
radius=50

# call the function to draw the heatmap
drawHeatMap(locations, val, zoom, intensity, radius)
