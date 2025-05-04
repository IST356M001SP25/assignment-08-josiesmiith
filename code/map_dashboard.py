'''
map_dashboard.pyThis data dashboard will visualize the top locations on a heatmap.
Each location should plotted with circle  representing the amount of fines issued at that location.
If you use geopandas this will be very little code.

'''
import streamlit as st
import streamlit_folium as sf
import folium
import pandas as pd
import geopandas as gpd
# these constants should help you get the map to look better
# you need to figure out where to use them
CUSE = (43.0481, -76.1474)  # center of map
ZOOM = 14                   # zoom level
VMIN = 1000                 # min value for color scale
VMAX = 5000                 # max value for color scale

df = pd.read_csv('./cache/top_locations_mappable.csv')

st.title('Top Locations for Parking Tickets Within Syracuse')
st.write('This map shows the top locations with $1000 or more in total aggregate violation amounts for parking tickets in Syracuse, NY. The size of the circle represents the number of tickets issued at that location. The larger the circle, the more tickets were issued at that location.')

gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.lon, df.lat))
m = folium.Map(location=CUSE, zoom_start=ZOOM)
cuse_map = gdf.explore(gdf['amount'], m=m, 
                       cmap="magma",vmin=VMIN, vmax=VMAX, 
                       legend=True, legend_name='Amount',
                       marker_type = "circle",
                       marker_kwds = {"radius": 10, "fill": True},
)
sf.folium_static(cuse_map, width=800, height=600)