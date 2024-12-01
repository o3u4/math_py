% 使用 PageRank 算法对网站进行排名
% 在 PageRank 算法的每一步中，每个网页的得分都会根据以下公式更新：
% r = (1-P)/n + P*(A'*(r./d) + s/n);
% r 是 PageRank 得分的向量。
% P 是标量阻尼因子（通常为 0.85），这是随机浏览者点击当前网页上的链接而不是在另一随机网页上继续点击的概率。
% A' 是图形的邻接矩阵的转置。
% d 是包含图形中每个节点的出度的向量。对于没有外向边的节点，d 设置为 1。
% n 是图形中节点的标量数量。
% s 是无链接的网页的 PageRank 得分的标量总和。

s = {'a' 'a' 'a' 'b' 'b' 'c' 'd' 'd' 'd'};
t = {'b' 'c' 'd' 'd' 'a' 'b' 'c' 'a' 'b'};
G = digraph(s,t);
labels = {'a/3' 'a/3' 'a/3' 'b/2' 'b/2' 'c' 'd/3' 'd/3' 'd/3'};
p = plot(G,'Layout','layered','EdgeLabel',labels);
highlight(p,[1 1 1],[2 3 4],'EdgeColor','g')
highlight(p,[2 2],[1 4],'EdgeColor','r')
highlight(p,3,2,'EdgeColor','m')
title('PageRank Score Transfer Between Nodes')

pr = centrality(G,'pagerank','FollowProbability',0.85)
G.Nodes.PageRank = pr;
G.Nodes.InDegree = indegree(G);
G.Nodes.OutDegree = outdegree(G);
G.Nodes