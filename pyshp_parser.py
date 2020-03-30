# from osgeo import ogr
# file = ogr.Open("my_shapefile.shp")
# shape = file.GetLayer(0)
# #first feature of the shapefile
# feature = shape.GetFeature(0)
# first = feature.ExportToJson()
# print first # (GeoJSON format)
# {"geometry": {"type": "LineString", "coordinates": [[0.0, 0.0], [25.0, 10.0], [50.0, 50.0]]}, "type": "Feature", "properties": {"FID": 0.0}, "id": 0}


import shapefile
shape = shapefile.Reader("shp/city.shp")
#first feature of the shapefile
feature = shape.shapeRecords()[0]
first = feature.shape.__geo_interface__
print(first) # (GeoJSON format)
# {'type': 'LineString', 'coordinates': ((0.0, 0.0), (25.0, 10.0), (50.0, 50.0))}
