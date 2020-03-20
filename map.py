import folium

# Create Map Object

m = folium.Map(location=[10.358,120.981], zoom_start=12)

m.save('map.html')