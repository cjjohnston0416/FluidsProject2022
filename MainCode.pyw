# Main Code Fluid Term Project
# laminar flow of Air
#Particle Size Range 0.01 to 100 micron (Must pick 3)
#Velocity
import math;
import pickle;
from matplotlib import pyplot as plt;
#Fields
V = 0.1; #M/s
Height = 0.02; #m
Length = 0.2; #m
S = 2000;# Density Ratio
N = 50.0; # to 200 trajectories
densityA = 1.225;
gravity = 9.81;# m/s^2
Cc = 1.2; #correction coefficient
k = 0.000000000000000000000138;
Temp = 293.0;# Temp in Kelvin
mu = 0.0000181;#m^2/s
d = 0.00005;
mass2 = 0.00000000128281700;
x2 = [];
#Function
def Dissifutivity(string):
   if string == 'True':
       Diss = (k*Temp*Cc)/(3* math.pi * mu * d);
       beta = Cc/(3 *3.14*mu*d);
       reynolds = (2 * densityA * V * Height)/mu;
       mass = (3*math.pi * mu * d)/Cc;

       print("Dissifutivity = %30.3E" % (Diss));
       print(" = %30.3E" % (beta));
       print(reynolds);
       print(mass);
       for x in range(1,30):
           y = math.sqrt( 2* Diss * (x*2));
           x2.append(y);
       print(x2);
       plt.plot(x2);
       plt.show();
       return;




string = input('Enter True to begin:');
Dissifutivity(string);

