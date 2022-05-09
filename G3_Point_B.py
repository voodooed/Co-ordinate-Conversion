import math
import numpy as np

# For Point B

# Converting from Astronomical Co-ordinate to Ellipsoidal Co-ordinate

aphi = math.radians(26.75059) # Value of Astronomic Latitude
alam = math.radians(78.47535) # Value of Astronomic Longitude
h = 291.5  # Orthometric Height

n = -57.5207  # Geoid Undulation
xi = math.radians(0.0001170278) # Defelection of Meridian
no = math.radians(0.00008916667) # Deflection of Prime Verticle

gphi = aphi-xi # Geodetic latitude
glam = alam-(no/math.cos(gphi)) # Geodetic Longitude
gh = h+n # Geodetic Height

#Converting Corresponding Ellipsodial Co-ordinate to Cartesian Co-ordinate

a = 6378137.0 # Assumed Value of Semi Major Axis
b = 6356752.3142 # Assumed Value of Semi Minor Axis
f = 0.00335281066 # Assumed Value of Flattening

esq = (2*f) - (f*f) # Calculating Square of Eccentricity(e2)

sa = math.pow(math.sin(gphi),2)
dna = math.sqrt(1-(esq*sa))

na = a/dna # Value of ROC in the prime vertical plane

x = (na + gh) * math.cos(gphi) * math.cos(glam)
y = (na + gh) * math.cos(gphi) * math.sin(glam)
z = (na*(1-esq)+gh) * math.sin(gphi)

#Converting Corresponding Cartesian Co-ordinate to Topocentric Co-ordinate System

#Calculating the Rotation Matrix R
r = np.matrix([

                [-math.sin(glam), math.cos(glam), 0],
                [-math.sin(gphi)*math.cos(glam), -math.sin(gphi)*math.sin(glam), math.cos(gphi) ],
                [math.cos(gphi)*math.cos(glam), math.cos(gphi)*math.sin(glam), math.sin(gphi)]


 ])

cart_mat = np.matrix([
                       [x],
                       [y],
                       [z]
 ])


topo_cord = r * cart_mat

print("The Topocentric Co-ordinates e,n,u are: ")
print("e = {}, n = {}, u = {}".format(topo_cord[0],topo_cord[1],topo_cord[2]))