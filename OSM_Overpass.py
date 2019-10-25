# pip install overpass
import overpass

api = overpass.API(timeout=600, debug=True)

response = api.get('node["tourism"="alpine_hut"](41.836828,-5.009766,54.977614,29.267578);out 2;', responseformat="geojson")

# filtering for 50 points only
responseNew = response[0:51]
print(responseNew)