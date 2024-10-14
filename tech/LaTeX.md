# $\LaTeX$

## 字体

```latex
% 设置中文和英文字体为 Fandol
\setCJKmainfont{FandolSong} % Fandol 宋体
```

## 公式

```latex
\displaystyle \sum  % 展示模式，可以让求和号变成正常大小

\left\{ 
		\begin{matrix}
		\frac{1}{n}\displaystyle\sum_{i=1}^{n}\xi_i = \hat{\nu_1}\\
		\frac{1}{n}\displaystyle\sum_{i=1}^{n}\xi_i^2 = \hat{\nu_2}
		\end{matrix}	\right.
```

## 表格

### table 环境下的表格

- **常用**

```latex
\begin{table}[htbp!]
	\caption{标题}
	\label{标签}
	\centering
	\begin{tabular}{cc}
		\toprule
		\makebox[0.45\textwidth][c]{符号} & \makebox[0.45\textwidth][c]{意义}	\\ \midrule
		Symbol  & Meanings \\
		Symbol  & Meanings \\
		Symbol  & Meanings \\
		Symbol  & Meanings \\ \bottomrule
	\end{tabular}
\end{table}
```

### 多表格并排

- 两表格并排，且共用标题

  - `\caption{标题}` ` \label{标签}` 写在`\begin{minipage}`前面即可

  ```latex
  \begin{table}[htbp!]
  	\caption{标题}
  	\label{标签}
  	\centering
  	\begin{minipage}{0.48\textwidth}
  		\centering
  		\begin{tabular}{cc}
  			\toprule
  			\makebox[0.5\textwidth][c]{符号} & \makebox[0.5\textwidth][c]{意义} \\
  			\midrule
  			Symbol  & Meanings \\
  			Symbol  & Meanings \\
  			Symbol  & Meanings \\
  			Symbol  & Meanings \\
  			\bottomrule
  		\end{tabular}
  	\end{minipage}
  	\hfill
  	\begin{minipage}{0.48\textwidth}
  		\centering
  		\begin{tabular}{cc}
  			\toprule
  			\makebox[0.5\textwidth][c]{符号} & \makebox[0.5\textwidth][c]{意义} \\
  			\midrule
  			Symbol  & Meanings \\
  			Symbol  & Meanings \\
  			Symbol  & Meanings \\
  			Symbol  & Meanings \\
  			\bottomrule
  		\end{tabular}
  	\end{minipage}
  \end{table}
  ```

### center 环境下的表格

- `\makebox[0.45\textwidth][c]{符号}`：控制单元格长度

```latex
\begin{center}
	\begin{tabular}{cc}
		\hline
		\makebox[0.45\textwidth][c]{符号} & \makebox[0.45\textwidth][c]{意义}	\\ \hline
		Symbol  & Meanings \\
		Symbol  & Meanings \\
		Symbol  & Meanings \\
		Symbol  & Meanings \\ \hline
	\end{tabular}
\end{center}
```

**`@{}`**：这个命令用于移除或者添加特定的格式或空间。在这个上下文中，`@{}` 用于移除列间隙的默认空格，这通常用于改变表格的默认边距设置。放在开始和结束处，表示表格的最左侧和最右侧不会有额外的空白。

**`c`**：表示列的对齐方式，`c` 代表居中对齐。

**`|`**：用于在列之间添加垂直分隔线。

例如：`@{}ccc|ccc|ccc@{}`

- 合并单元格：
  - 合并列：`\multicolumn{3}{c|}{第一组}`
    - 设置合并后的列的对齐方式为居中（`c`），并在合并的列的右侧添加一个垂直分隔线（`|`）
  - 合并行：`\multirow{合并行数}{对齐方式}{内容}`

---

## 图片

### 单张图片

- 调整大小
  - `width=10cm`
  - `height=50mm`
  - `scale=0.5`，缩小到原始大小的一半
  - `width=0.75\textwidth`，文本宽度的75%
- 调整位置
  - `\hspace*{-0.5cm}`，左移0.5cm
  - `\vspace*{-0.5cm}`，上移0.5cm

```latex
\begin{figure}[htbp!]
	\centering
	\includegraphics[width=15cm]{路径}
	\caption{标题}
  	\label{标签}
\end{figure}
```

### 多张图片

- 对齐
  - `b` 表示基线对齐，底部将对齐
  - **`[t]`** - 顶部对齐
  - **`[c]`** - 中心对齐

```latex
\begin{figure}[htbp!]  
    \centering  
    \begin{minipage}[b]{0.45\linewidth}  
        \centering  
        \includegraphics[height=5.5cm]{图片1}
        \caption{标题1}  
        \label{标签1}  
    \end{minipage}  
    \hfill % 在两张图片之间添加水平间距  
    \begin{minipage}[b]{0.45\linewidth}  
        \centering  
        \includegraphics[height=5.5cm]{图片2}
        \caption{标题2}  
        \label{标签2}  
    \end{minipage}  
\end{figure} 
```
