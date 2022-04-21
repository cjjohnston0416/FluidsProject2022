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
#k = 0.000000000000000000000138;
k = 0.000000000000000138;
Temp = 293.0;# Temp in Kelvin
mu = 0.0000181;#m^2/s
d1 = 0.00000001;
d2 = 0.00005;
d3 = 0.0001
mass2 = 0.00000000128281700;
x1 = [];
x2 = [];
x3 = [];
xaxis = [];
#Function
def Dissifutivity(string):
   if string == 'True':
       #small size 
       Diss1 = (k*Temp*Cc)/(3* math.pi * mu * d1);
       beta1 = Cc/(3 *3.14*mu*d1);
       reynolds1 = (2 * densityA * V * Height)/mu;
       mass1 = (3*math.pi * mu * d1)/Cc;

       print("Dissifutivity = %30.3E" % (Diss1));
       print(" = %30.3E" % (beta1));
       print(reynolds1);
       print(mass1);
       for x in range(0,30):
           x = x * .0001;
           y = math.sqrt( 2* Diss1 * (x*2));
           x1.append(y);
       print(x1);

       #medium size
       Diss2 = (k*Temp*Cc)/(3* math.pi * mu * d2);
       beta2 = Cc/(3 *3.14*mu*d2);
       reynolds2 = (2 * densityA * V * Height)/mu;
       mass2 = (3*math.pi * mu * d2)/Cc;

       print("Dissifutivity = %30.3E" % (Diss2));
       print(" = %30.3E" % (beta2));
       print(reynolds2);
       print(mass2);
       for x in range(0,30):
           y = math.sqrt( 2* Diss2 * (x*2));
           x2.append(y);
       print(x2);

       #large size
       Diss3 = (k*Temp*Cc)/(3* math.pi * mu * d3);
       beta3 = Cc/(3 *3.14*mu*d3);
       reynolds3 = (2 * densityA * V * Height)/mu;
       mass3 = (3*math.pi * mu * d3)/Cc;

       print("Dissifutivity = %30.3E" % (Diss3));
       print(" = %30.3E" % (beta3));
       print(reynolds3);
       print(mass3);
       for x in range(0,30):
           y = math.sqrt( 2* Diss3 * (x*2));
           x3.append(y);
       print(x3);
       
       for x in range(0,30):
           y = x;
           xaxis.append(y);

       plt.plot(xaxis,x1)
       plt.legend(['x1']);
       #plt.plot(xaxis,x2);
       #plt.legend(['x2']);
       #plt.plot(xaxis,x3);
       #plt.legend(['x3']);
       plt.autoscale();
       plt.show();
       return;




string = input('Enter True to begin:');
Dissifutivity(string);

