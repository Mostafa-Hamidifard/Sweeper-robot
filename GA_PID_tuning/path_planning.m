clc;

theta0 = 80*pi/180;
thetaf = 40*pi/180;

tf = 0.1;

a0 = theta0;
a1 = 0;
A = [tf^2 tf^3;
    2*tf 3*tf^2];
x = A\[thetaf-theta0;0];
a2 = x(1);
a3 = x(2);


t = 0:0.01:2;
y = a0+a1.*t + a2.*t.^2 + a3.*t.^3;