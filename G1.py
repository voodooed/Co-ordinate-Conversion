import math


# Coverting Geodetic Co-ordinate System to Cartesian Co-ordinate System
#Assuming random values to check the algorithm and program

a = 6378137.0 
b = 6356752.3142
f = 0.00335281066

esq = (2*f) - (f*f) # Calculating Square of Eccentricity(e) - e^2

pi = 22/7
phia = 43.26286*(pi/180) # degree to radian

lama = -89.99505*(pi/180) # degree to radian

ha = 1382.618

sa = math.pow(math.sin(phia),2)
dna = math.sqrt(1-(esq*sa))

na = a/dna


xa = (na + ha) * math.cos(phia) * math.cos(lama)
ya = (na + ha) * math.cos(phia) * math.sin(lama)
za = (na*(1-esq)+ha) * math.sin(phia)

print("The Cartesian( X, Y, Z ) coordinates are:")
print("X = {}, Y = {}, Z = {}".format(xa,ya,za))


# Coverting Cartesian Co-ordinate System to Geodetic Co-ordinate System
#Assuming random values to check the algorithm and program


edsq = esq/(1-esq) # (e')^2

x = 12046.5808
y = -4649394.0826
z = 4353160.0634

n = 6388194.760275498

finallamb = math.atan(y/x)  # Final Value of Lambda λ

r = math.sqrt(x**2+y**2)

phio = math.atan((z*(1+edsq))/r) # initial value of phi (Φ)0

def valuephi(phi):

    phi = math.atan((z+(n*esq*(math.sin(phi))))/r)
    
    return phi

phii = valuephi(phio) # value of Φi
phii1 = valuephi(phii) # value of Φi+1

flag = 0

while(flag != 1):

    if((phii-phii1)>=1.45) :             # Taking the acceptable difference between the succesive value less than 3 seconds
        print("0")
        phii = phii1
        phii1 = valuephi(phii)
    
    else:

        finalphi = phii1 ## final value of phi
        flag = 1

sa = math.pow(math.sin(finalphi),2)
dna = math.sqrt(1-(esq*sa))

na = a/dna

h = (r/math.cos(finalphi)) - na # value of h


print("The geodetic coordinates after conversion are as follows: ")
print("The value of Geodetic latitude Φ is: {} degrees".format(math.degrees(finalphi)))
print("The value of geodetic longitude λ is: {} degrees".format(math.degrees(finallamb)))
print("The value of height h is: {} meters".format(h))