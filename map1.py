import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
# loc = list(data["LOCATION"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'

#Creating map object
map = folium.Map(location=[38.91, -77.001], zoom_start=10, tiles='Stamen Terrain')


fg = folium.FeatureGroup(name="My Map")
#add objects to map dir(folium), help(folium.Marker)
# coord_list = [[38.91, -77.00], [37.54, -77.43], [38.98, -76.49]]
# for coord in coord_list:

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup= str(el)+"m", icon=folium.Icon(color=color_producer(el))))

#loading json data
fg.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read())))

map.add_child(fg)
map.save("Map1.html")
