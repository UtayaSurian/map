import folium
import pandas as pd

class Map:
    """
    To create map data that shows happiest states that ranked in Malaysia according to FreeMalaysiaToday
    Source Data: https://www.freemalaysiatoday.com/category/leisure/money/2022/09/16/top-10-states-and-territories-ranked-by-happiness-with-salary/

    :parameter
    None
    
    Methods:
        color: To pick color based on ranking score
        create_map: To create map based on Folium and adding styles

    """
    def __init__(self):
        df_happiest_state = pd.read_csv("C:\\Users\\Administrator\\Downloads\\happiest_state.txt")
        self.lat = list(df_happiest_state['lat'])
        self.lon = list(df_happiest_state['lon'])
        self.rank = list(df_happiest_state['rank'])

    def color(self,rank):
        if rank > 8:
            return 'green'
        elif 6.5 <= rank < 8:
            return 'orange'
        else:
            return 'red'


    def create_map(self):
        map = folium.Map(tiles='Stamen Terrain')
        fg1 = folium.FeatureGroup("Happiest State")
        for lt, lo, rk in zip(self.lat, self.lon, self.rank):
            fg1.add_child(folium.Marker(location=[lt,lo],popup=str(rk),
                                             icon=folium.Icon(self.color(rk))))

        map.add_child(fg1)
        map.save('happiest_state.html')

mp = Map()
mp.create_map()