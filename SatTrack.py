
from pyorbital.orbital import Orbital
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

plt.figure(figsize=(8, 8))
m = Basemap(projection='ortho', resolution=None, lat_0=50, lon_0=-100)
m.bluemarble(scale=0.5);

latLonAlt = []
orbit = Orbital("Suomi NPP")
currentTime = datetime.utcnow()
position = orbit.get_lonlatalt(currentTime)# sat position
print("Longitude, Latitude, Altitude.")
print(position)
latLonAlt.append(position)
Latitude = position[0]
Longitude = position[1]
Altitude = position[2]
