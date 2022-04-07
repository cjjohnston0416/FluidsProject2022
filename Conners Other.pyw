# Othercode to test out different things
# laminar flow of Air
#Particle Size Range 0.01 to 100 micron (Must pick 3)
#Velocity
import math;
import pickle;
from matplotlib import pyplot as plt;
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
k = 0.000000000000000000000138;
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
brown = np.empty(200);
def BrownianForce(String):
    if String == 'True':
        #for x in range(0,200):
            for x2 in range(0,200):
                top = 12 * math.pi *(d1/2) * mu *k * Temp;
                dt = 0.003;
                randomint = random.uniform(0,1)
                ##randominteger = random.ran
                brown[x2] = randomint*(math.sqrt(top/dt));
                print(brown);

            return;
        #return;
    return;
string = input('Enter True to begin:');
BrownianForce(string);
plt.plot(brown);
plt.show();
