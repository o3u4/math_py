% 经纬度 30.913756 和 119.118062
rdrlat = 30.913756;
rdrlon = 119.118062;

figure
% 绘制雷达位置
geoplot(rdrlat, rdrlon, ...
    "LineWidth", 6, ...
    "MarkerSize", 3, ...
    "DisplayName", "Radar location")
% 设置地图背景为地形图
geobasemap topographic

% 手动设置地图显示区域，放大到特定范围
latmin = 30.8; % 设置最小纬度
latmax = 31.0; % 设置最大纬度
lonmin = 119.0; % 设置最小经度
lonmax = 119.2; % 设置最大经度
geolimits([latmin, latmax], [lonmin, lonmax]); % 通过 geolimits 放大特定区域

hold on
% 绘制边界框
% geoplot([latmin latmin latmax latmax latmin], [lonmin lonmax lonmax lonmin lonmin], ...
%     "LineWidth", 1, ...
%     "Color", "k", ...
%     "DisplayName", "Terrain limits");
