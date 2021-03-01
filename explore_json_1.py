import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

infile = open("eq_data_1_day_m1.json", "r")
outfile = open("readable_eq_data.json", "w")

# The json.loaod() function converts the data into a format Python
# can work with, in this case a giant dictionary.

eq_data = json.load(infile)

json.dump(eq_data, outfile, indent=4)

# Explore the structure of the data.

all_eq_dicts = eq_data["features"]

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])


# Now bring in chart with plotly

data = [Scattergeo(lon=lons, lat=lats)]

my_layout = Layout(title="Global Earthquakes")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="global_earthquakes.html")
