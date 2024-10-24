no_var = 6;
lb = [-10,-10,-10, 0, 0.5, 0.1];
up = [0, 0, 0, 0.16, 1.5, 0.5];
ga_opt = gaoptimset('Display','off','Generations',15,'PopulationSize',20,'PlotFcns',@gaplotbestf);

obj_fun = @(K) double_cost_func(K);
[K,best] = ga((obj_fun),no_var,[],[],[],[],lb,up,[],ga_opt)