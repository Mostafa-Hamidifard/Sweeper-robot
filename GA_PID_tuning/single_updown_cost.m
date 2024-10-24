function cost = single_updown_cost(K)
assignin('base','theta0',80*pi/180);
assignin('base','thetaf',45*pi/180);
assignin('base','K',K);

sim("test_m.slx");

cost = sum(([0 ;diff(100 * control_effort.Data)].^2 + 350 * error.Data .^2) * 0.001);
end
