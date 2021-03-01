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

mags, lons, lats, hover_texts = [], [], [], []

for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    hover_text = eq_dict["properties"]["place"]

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(hover_text)

print(mags[:10])
print(lons[:10])
print(lats[:10])


# Now bring in chart with plotly

data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "text": hover_texts,
        "marker": {
            "size": [5 * mag for mag in mags],
            "color": mags,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Magnitude"},
        },
    }
]

my_layout = Layout(title="Global Earthquakes")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="global_earthquakes.html")
