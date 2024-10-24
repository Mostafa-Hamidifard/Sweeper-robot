%% down to up
K = [K1(1:3) , K1(7:9)];
assignin('base','theta0',0*pi/180);
assignin('base','thetaf',45*pi/180);
assignin('base','K',K);
sim("test_m.slx");

%% up to down
K = K1(4:9);
assignin('base','theta0',45*pi/180);
assignin('base','thetaf',80*pi/180);
assignin('base','K',K);
sim("test_m.slx")