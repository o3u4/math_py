% 主程序
% 设置随机种子
rng(101)
rng_state = rng; % 保存随机数生成器状态
disp(['当前随机种子: ', num2str(rng_state.Seed)]);
% 假设我们有一些真实数据 (时间、猎物种群、捕食者种群)
t_data = linspace(0, 10, 100);  % 时间数据
x_true = 40 + 10 * sin(0.6 * t_data);  % 模拟真实数据 (猎物种群)
y_true = 9 + 3 * cos(0.6 * t_data);   % 模拟真实数据 (捕食者种群)

% 添加噪声
x_data = x_true + randn(size(t_data)) * 2;  % 加入噪声
y_data = y_true + randn(size(t_data)) * 1;  % 加入噪声

% 初始条件
initial_conditions = [x_data(1), y_data(1)];

% 设置初始参数猜测
initial_params = [1.0, 0.5, 0.5, 0.1];  % [alpha, beta, gamma, delta]

% 定义目标函数 (最小化误差)
objective_function = @(params) error_function(params, t_data, x_data, y_data, initial_conditions);

% 使用 fminsearch 进行参数拟合
options = optimset('Display', 'iter');  % 显示信息, 'off'：不显示信息, 'final'显示最终结果
fitted_params = fminsearch(objective_function, initial_params, options);

% 打印拟合的参数
disp('拟合的参数：')
disp(['alpha = ', num2str(fitted_params(1))])
disp(['beta = ', num2str(fitted_params(2))])
disp(['gamma = ', num2str(fitted_params(3))])
disp(['delta = ', num2str(fitted_params(4))])

% 使用拟合的参数求解方程
[t, z] = ode45(@(t, z) lotka_volterra(t, z, fitted_params(1), fitted_params(2), fitted_params(3), fitted_params(4)), t_data, initial_conditions);
% 求数值解使用t_data对应真实值, 也可以指定范围[0, 15], 进行预测, 

% 绘制结果
figure;
hold on;
plot(t_data, x_data, 'r.', 'DisplayName', 'Prey (data)');
plot(t_data, y_data, 'b.', 'DisplayName', 'Predator (data)');
plot(t, z(:,1), 'r-', 'DisplayName', 'Prey (fitted)');
plot(t, z(:,2), 'b-', 'DisplayName', 'Predator (fitted)');
xlabel('Time');
ylabel('Population');
legend;
title('Lotka-Volterra Model Fitting');
hold off;

% 误差函数，用于拟合
function error = error_function(params, t_data, x_data, y_data, initial_conditions)
    % 求解模型
    [t, z] = ode45(@(t, z) lotka_volterra(t, z, params(1), params(2), params(3), params(4)), t_data, initial_conditions);
    
    % 插值使模型解与真实数据对齐
    x_model = interp1(t, z(:,1), t_data, 'spline');  % 猎物种群
    y_model = interp1(t, z(:,2), t_data, 'spline');  % 捕食者种群
    
    % 计算误差：真实数据和模型解的平方误差
    error = sum((x_model - x_data).^2 + (y_model - y_data).^2);  % 总平方误差
end

% Lotka-Volterra 方程
function dzdt = lotka_volterra(t, z, alpha, beta, gamma, delta)
    x = z(1);  % Prey population
    y = z(2);  % Predator population
    dxdt = alpha * x - beta * x * y;
    dydt = delta * x * y - gamma * y;
    dzdt = [dxdt; dydt];
end
