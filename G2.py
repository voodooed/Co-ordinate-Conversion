import math


# Converting from Astronomical Co-ordinate to Ellipsoidal Co-ordinate

aphi = math.radians(20.17222) # Value of Astronomic Latitude
alam = math.radians(78.33639) # Value of Astronomic Longitude
h = 510.63 # Orthometric Height

n = -39.5  # Geoid Undulation
xi = math.radians(0.0001086667) # Defelection of Meridian
no = math.radians(0.00006083333) # Deflection of Prime Verticle

gphi = aphi-xi # Geodetic latitude
glam = alam-(no/math.cos(gphi)) # Geodetic Longitude
gh = h+n # Geodetic Height

print("The Ellipsodal Cordinates of the point are:")
print("Geodetic Latitude(ϕ) is {} degrees".format(math.degrees(gphi)))
print("Geodetic Latitude(λ) is {} degrees".format(math.degrees(glam)))
print("Geodetic Height(h) is {} meters".format(gh))

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

print("The Cartesian( X, Y, Z ) coordinates are:")
print("The Geocentric coordinates are: X = {}, Y = {}, Z = {}".format(x,y,z))

