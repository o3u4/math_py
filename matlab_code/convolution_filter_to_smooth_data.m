% 使用 peaks 函数创建二维数据，并在各个等高线层级对数据绘图
Z = peaks(100);
levels = -7:1:10;

% 向数据中插入随机噪声并绘制含噪等高线
Znoise = Z + rand(100) - 0.5;
contour(Znoise,levels)

% 定义一个 3×3 核 K 并使用 conv2 对 Znoise 中的含噪数据进行平滑处理。
% 绘制经过平滑处理的等高线。conv2 中的 'same' 选项使输出的大小与输入相同。
K = (1/9)*ones(3);
Zsmooth1 = conv2(Znoise,K,'same');
contour(Zsmooth1, levels)

% 用 5×5 核对含噪数据进行平滑处理，并绘制新等高线
K = (1/25)*ones(5);
Zsmooth2 = conv2(Znoise,K,'same');
contour(Zsmooth2,levels)