import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


fire_file2 = open("US_fires_9_14.json", "r")
fire2 = json.load(fire_file2)

lats, lons, brightnesses = [], [], []

for item in fire2:
    lat = item["latitude"]
    lon = item["longitude"]
    brightness = item["brightness"]

    if brightness > 450:
        lats.append(lat)
        lons.append(lon)
        brightnesses.append(brightness)

data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "marker": {
            "size": [0.025 * b for b in brightnesses],
            "color": brightnesses,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "brightness"},
        },
    }
]

my_layout = Layout(title="US Fires - 9/14/2020 through 9/20/2020")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="california_fires2.html")
