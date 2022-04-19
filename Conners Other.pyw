# Othercode to test out different things
# laminar flow of Air
#Particle Size Range 0.01 to 100 micron (Must pick 3)
#Velocity
import math;
import pickle;
from matplotlib import pyplot as plt;
from matplotlib import pyplot as plt2;
import random;
import numpy as np;
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
mass1 = (3*math.pi * mu * d1)/Cc;
mass2 = 0.00000000128281700;
mass3 = (2000*1.2)*((4/3)*math.pi*(d3/2)*(d3/2)*(d3/2));
x1 = [];
x2 = [];
x3 = [];
xaxis = [];
brown = np.empty(200);
drag = np.empty(200);
velocity = np.empty(200);
vp = np.empty(200);
slip = np.empty(200);
def BrownianForce(String):
    if String == 'True':
            for x2 in range(1,200):
                top = 12 * math.pi *(d3/2) * mu *k * Temp;
                dt = x2 *0.0001;
                randomint = random.uniform(0,1)
                ##randominteger = random.ran
                brown[x2] = randomint*(math.sqrt(top/dt));
            for x3 in range(0,200):
                Tow = (mass3* Cc)/(3 * math.pi * mu * d3);
                ##Tow = 10;
                step = x3 *(Height/200);
                Vm = (.1*.02)/.2;
                velocity[x3] = Vm*(1-(((step)*(step))/((Height/2)*(Height/2))));
                top = 3*math.pi *mu*d3;
                exponent = math.exp(-step/Tow);
                vo = 0;
                #C = (-velocity[x3])*exponent;

                vp[x3] = velocity[x3-1]*(1-exponent);
                slip[x3] = (velocity[x3]-vp[x3]);
                reynolds = (densityA * np.absolute(slip[x3]) * d3)/mu;
                Cd = 24/reynolds;
                Area = 4 * math.pi * ((d3/2)*(d3/2));
                multi = (0.5 * densityA * (slip[x3]* slip[x3])*Area);
                drag[x3] = multi * Cd;

    print(brown);
    print(reynolds);
    print(Cd);
    print();
    print(drag);
    print(velocity);
    print(vp);
    print()
    print(slip);
    return;
string = input('Enter True to begin:');
BrownianForce(string);
plt.figure(1);
plt.subplot(221);
plt.plot(brown);
plt.xlabel('Brownian Force')
plt.subplot(222);
plt.plot(drag);
plt.xlabel('Drag Force')
plt.subplot(223);
plt.plot(velocity);
plt.xlabel('Fluid Velocity')
plt.subplot(224);
plt.plot(vp);
plt.xlabel('Particle Velocity')
plt.show();