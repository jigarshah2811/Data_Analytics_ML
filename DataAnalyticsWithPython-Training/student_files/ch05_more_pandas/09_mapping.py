"""
    09_mapping.py   -   This example uses the matplotlib toolkit extension called
                        basemap.  It acquires data remotely using the 3rd party
                        tool called requests and uses the json_normalize() function
                        to read the json data within the 'markers' property into a
                        DataFrame.  Latitude and longitude values are extracted and
                        plotted using a Basemap object which is given a background
                        image using the readshapefile() method.



"""
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import requests

url = 'http://inciweb.nwcg.gov/feeds/json/markers/'

statemap = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
        projection='lcc',lat_1=32,lat_2=45,lon_0=-95)
statemap.readshapefile('../resources/shapes/st99_d00', name='statemap', drawbounds=True)

data = requests.get(url).json()                     # get the data
df = json_normalize(data['markers'])                # using json_normalize() because read_json() will read a dict per record
for row in df.itertuples():                         # row is a namedtuple
    x, y = statemap(row.lng, row.lat)               # translate lat, lng into coords for a matplotlib plot
    statemap.plot(x, y, marker='o', color='Red')    # plot the points
plt.show()
