import folium
import pandas as pd

class Map:
    def __init__(self):
        self.df = pd.read_csv("C:\\Users\\Administrator\\Downloads\\Volcanoes.txt")
        self.lat = list(self.df['LAT'])
        self.lon = list(self.df['LON'])
        self.elev = list(self.df['ELEV'])
        self.map = folium.Map(tiles="Stamen Terrain")
        self.fg1 = folium.FeatureGroup(name="Volcanos")
        self.fg2 = folium.FeatureGroup(name="Population")

    def color(self,el):
        if el < 1000:
            return "green"
        elif 1000 <= el < 3000:
            return "orange"
        else:
            return "red"

    def create_volcano_map(self):
        for lt, lo, el in zip(self.lat, self.lon, self.elev):
            self.fg1.add_child(folium.CircleMarker(location=[lt, lo], popup=str(el)+ " m", radius=7,
                                             fill_color=self.color(el), color='grey', fill_opacity=0.7))

    def show_world_population(self):
        self.fg2.add_child(folium.GeoJson(data=open("C:\\Users\\Administrator\\Downloads\\world.json", "r", encoding='utf-8-sig').read(),
                                    style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 1000000 else 'orange'
                                    if 1000000 <= x['properties']['POP2005'] < 2000000 else 'red'}))

    def save_data(self):
        self.map.add_child(self.fg1)
        self.map.add_child(self.fg2)
        self.map.add_child(folium.LayerControl())
        self.map.save("map.html")

map = Map()
map.create_volcano_map()
map.show_world_population()
map.save_data()

