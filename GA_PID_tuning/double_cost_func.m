function cost = double_cost_func(K)
assignin('base','theta0',0*pi/180);
assignin('base','thetaf',45*pi/180);
assignin('base','K',K);
sim("test_m.slx");

cost1 = sum(([0 ;diff(100 * control_effort.Data)].^2 + 350 * error.Data .^2) * 0.001);

assignin('base','theta0',80*pi/180);
assignin('base','thetaf',45*pi/180);
sim("test_m.slx");

cost2 = sum(([0 ;diff(100 * control_effort.Data)].^2 + 350 * error.Data .^2) * 0.001);

cost = 1 * cost1 + 1.5*cost2;
end
