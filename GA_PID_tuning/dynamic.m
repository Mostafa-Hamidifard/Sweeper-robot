function [t,f] = dynamic(x,v,a,q,w,b)

global link_mass counter_weight_mass movable_part_mass 
global g link_length counter_weight_length link_dim joint_damper

h = counter_weight_length;
L = link_length;
d = link_dim;

M = link_mass;
mb = counter_weight_mass;
m = movable_part_mass;

IL = M*(d*(L-h)^3/3+d*h^3/3+L*d^3/12)/(d*L);
Ix = mb*h^2 + m*x^2 + IL;
Mx = -mb*h + m*x + M*(L/2-h);

t = Ix*b + 2*m*x*v*w + Mx*cos(q)*g + joint_damper*w;
f = m*a-m*x*w^2 + m*g*sin(q);