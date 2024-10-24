clear;clc;

global link_mass counter_weight_mass movable_part_mass 
global g link_length counter_weight_length link_dim joint_damper ee_waight
global link_width ee_radi ee_lenght

counter_weight_length = 0.03;

link_length = 0.9;
link_dim = 0.03;
link_width = 0.34;

ee_radi = 0.07;
ee_lenght = 0.3;

ee_waight = 3.3; %kg
counter_mass = 0; %kg
link_mass = 5.31; %kg
movable_part_mass = 7.58; %kg

joint_damper = 0;

g = 9.80665;
%% gains

K = [-6.348 -6.1879 -7.4748 0.0263 1.3776 0.3140]; %% Kp_du , Ki_du, Kd_du, Kp_ud , Ki_ud, Kd_ud, center_offset , slider_mass , damper
K1 = K;
% counter_balance_mass = ((link_length / 2 + K(4)) * ee_waight) / (link_length / 2 - K(4));
% counter_balance_mass = ((link_length / 2 - K(4)) * ee_waight) / (link_length / 2 + K(4));

%%
%%%%%%%%% Shapes Parameters %%%%%%%%%%%%%%%%%%%%%%
r = 0.01;
b1 = 0.03;b2 = 0.34;b3 = 0.09; 
mb1 = 0.21;mb2 = 0.061;mb3 = 0.21;
%%%%%%%%% Brush Parameters %%%%%%%%%%%%%%%%%%%%%%%
brush_mass = 0.2;
brush_radius = 0.2;
brush_dim = 0.1;
brush_frequency = 20;
%%%%%%%%% constrain force parameters %%%%%%%%%%%%%%
impact_Kp = 500;impact_Kd = 50;
%%%%%%%%% simulation %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

sim('test_m.slx',3);

for i = 1:length(time)
    [t(i),f(i)] = dynamic(x(i),v(i),a(i),q(i),w(i),b(i));
end
%%%%%%%%% Dynamical Error %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
figure(1)
plot(time,t);xlabel('Time [s]');ylabel('Dynamic error [Nm]');
title('tau')
figure(2)
plot(time,f);xlabel('Time [s]');ylabel('Dynamic error [Nm]');
title('force')

disp('Brush Mass Ratio')
disp(brush_mass/(counter_weight_mass+link_mass+movable_part_mass+brush_mass)*100)
disp('Joint Damper')
disp(joint_damper)
disp('Brush Frequency')
disp(brush_frequency)