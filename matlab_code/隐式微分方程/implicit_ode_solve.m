function [T,Y] = implicit_ode_solve()
    % 初始条件与常数
    R1 = 1.0;        % 根据需要设置 R1
    GAMA = 0.5;      % 根据需要设置 GAMA
    L = 10;          % 设置 L
    y01 = [R1, 0, pi/2 - GAMA, 2];  % 初始条件
    tspan = [0 L];   % 求解的时间区间
    
    % 使用 ode45 求解
    [T, Y] = ode45(@Fun, tspan, y01);
    
    % 隐式方程的右边函数定义
    function Dy = Fun(t, y)
        % 定义方程组
        Fun = @(dy)[
            dy(1) - y(2);  % dy1/dt = y2
            y(1)*(dy(2))^2 + (2*(1 + (dy(1))^2)^(3/2)) * tan(y(3)) - dy(2);  % dy2/dt 方程
            (dy(4))/y(4) + (dy(1))/y(1) - dy(3) * tan(y(3)) - dy(3);  % dy3/dt 方程
            (dy(1))^4 - ((5 * y(4) * sin(y(3))) / 8) * (1 + (dy(1))^2)^(5/2) - dy(4);  % dy4/dt 方程
        ];
        
        % 使用 fsolve 解隐式方程
        Dy = fsolve(Fun, zeros(size(y)));  % fsolve 会尝试求解方程组
    end
end
