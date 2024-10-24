function cost = cost_func(K1)
assignin('base','theta0',0*pi/180);
assignin('base','thetaf',45*pi/180);

assignin('base','K',K);
sim("test_m.slx");

cost1 = sum(([0 ;diff(900 * control_effort.Data)].^2 + 350 * error.Data .^2) * 0.001);

K = K1(4:9);
assignin('base','theta0',80*pi/180);
assignin('base','thetaf',45*pi/180);
assignin('base','K',K);
sim("test_m.slx");

cost2 = sum(([0 ;diff(900 * control_effort.Data)].^2 + 350 * error.Data .^2) * 0.001);

cost = 0 * cost1 + 5*cost2;
% cost = integral(error^2 + control_effort^2)

% 
% % Extract numerical values from the timeseries object
% ITAE_data = evalin('base', 'ITAE.Data');
% 
% % Calculate ITAE
% ITAE_value = ITAE_data(end);  % Assuming ITAE_data is a vector and you want the last element
% 
% % Calculate cost using ITAE
% cost = ITAE_value;
end