function [r_t] = compute_poly_trajectory(t0,tf,r0,rf,t)
%COMPUTE_POLY_TRAJECTORY computing task space trajectory
r_t = r0 - (t - t0)^2 .* ( (3 * r0) ./ tf^2 - (3*rf) ./ tf^2 ) + (t - t0)^3 *( (2*r0)/tf^3 - (2*rf)/tf^3);

