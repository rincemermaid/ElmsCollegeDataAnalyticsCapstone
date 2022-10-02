import geopandas as gpd
import matplotlib.pyplot as plt
gdf = gpd.read_file('./cb_2019_25_place_500k.shp')
gdf.plot()
print(gdf)