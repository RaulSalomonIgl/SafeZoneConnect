import csv
from operator import attrgetter
import numpy as np

class Map:
    
    def getPoints(lat, lon, puntos, lstCords):
        lstCord = lstCords
        for cord in np.random.randn(puntos, 2) / [50, 50] + [lat, lon]:
            lstCord.append([cord[0], cord[1]])
        return lstCord