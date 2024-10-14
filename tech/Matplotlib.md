# Matplotlib

### 1. 生成图和子图

- **创建一个简单的图：**
  
  ```python
  import matplotlib.pyplot as plt
  fig, ax = plt.subplots()  # 创建一个包含单个轴的图
  plt.show()
  ```
  
- **创建多个子图：**
  ```python
  fig, axs = plt.subplots(nrows=2, ncols=2)  # 创建一个 2x2 的子图网格
  plt.show()
  ```

### 2. 设置图和子图的标题

- **设置主标题和子图标题：**
  ```python
  fig.suptitle('Main Title')  # 设置整个图的主标题
  axs[0, 0].set_title('Subplot Title')  # 设置特定子图的标题
  ```
  
- **获取句柄和标签：**

  ```python
  ax.get_legend_handles_labels()
  ```

- **更改句柄和标签：**

  ```python
  ax.legend(handles, new_labels)
  ```

### 3. 设置坐标轴标题和标签

- **设置 X 轴和 Y 轴标题：**
  ```python
  ax.set_xlabel('X Axis Label')
  ax.set_ylabel('Y Axis Label')
  ```

- **设置标签字体大小：**
  ```python
  ax.set_xlabel('X Axis Label', fontsize=12)
  ax.set_ylabel('Y Axis Label', fontsize=12)
  ```
  
- **设置坐标刻度颜色：**

  ```python
  ax.tick_params(axis='x', labelcolor='b')	# ax子图里面的x轴为蓝色
  ```

### 4. 设置坐标轴刻度

- **设置坐标轴的小突起（minor ticks）和大突起（major ticks）间隔：**
  
  ```python
  from matplotlib.ticker import AutoMinorLocator, MultipleLocator
  ax.xaxis.set_major_locator(MultipleLocator(10))  # X 轴主刻度间隔
  ax.xaxis.set_minor_locator(AutoMinorLocator(4))  # X 轴每个主刻度中的小刻度数量
  ax.yaxis.set_major_locator(MultipleLocator(10))
  ax.yaxis.set_minor_locator(AutoMinorLocator(4))
  ```

### 5. 设置双面坐标轴

- **在右侧添加一个 Y 轴：**
  
  ```python
  ax2 = ax.twinx()
  ax2.set_ylabel('Secondary Y Axis', fontsize=12)
  ```
  
- **设置双坐标轴的标签**

  ```python
  import matplotlib.pyplot as plt
  import numpy as np
  
  # 创建一些数据
  x = np.linspace(0, 10, 100)
  y1 = np.exp(x)  # 指数增长
  y2 = np.log(x + 1)  # 对数增长
  
  # 创建图和左侧轴
  fig, ax1 = plt.subplots()
  
  # 绘制第一组数据，使用左侧Y轴
  ax1.plot(x, y1, 'b-', label='Exp Growth')  # 'b-' 表示蓝色实线
  ax1.set_xlabel('X data')
  ax1.set_ylabel('Exponential Scale', color='b')
  ax1.tick_params(axis='y', labelcolor='b')  # 设置刻度颜色和标签颜色
  
  # 创建右侧轴
  ax2 = ax1.twinx()
  
  # 绘制第二组数据，使用右侧Y轴
  ax2.plot(x, y2, 'r--', label='Log Growth')  # 'r--' 表示红色虚线
  ax2.set_ylabel('Logarithmic Scale', color='r')
  ax2.tick_params(axis='y', labelcolor='r')  # 设置刻度颜色和标签颜色
  
  # 添加图例
  lines, labels = ax1.get_legend_handles_labels()		# 获取图形对象句柄和它们的标签
  lines2, labels2 = ax2.get_legend_handles_labels()
  ax1.legend(lines + lines2, labels + labels2, loc='upper left')		# 合并图形和标签
  
  # 显示图表
  plt.show()
  
  ```

### 6. 设置图例和标签位置

- **添加图例：**
  ```python
  ax.plot(range(10), label='Line 1')
  ax.legend(loc='upper left')
  ```

- **设置图例的位置和字体大小：**
  ```python
  ax.legend(loc='upper left', fontsize=10)	# 可填"upper right", "lower left"等
  ```
  
  ```python
  ax.legend(loc=(0.7, 0.5), fontsize=15)		# (0.7, 0.5)表示坐落在x轴占比0.7，y占比0.5处
  ```

### 7. 设置坐标轴的显示范围

- **设置 X 轴和 Y 轴的显示范围：**
  ```python
  ax.set_xlim(0, 100)
  ax.set_ylim(0, 1000)
  ```

### 8. 设置图的背景色和网格线

- **设置背景色：**
  ```python
  ax.set_facecolor('#D3D3D3')  # 浅灰色背景
  ```

- **添加网格线：**
  ```python
  ax.grid(True)
  ```

### 9. 保存图表

- **保存图像到文件：**
  ```python
  plt.savefig('filename.png', dpi=300)  # 保存图像，指定分辨率为 300 DPI
  ```

### 10. Jupyter notebook

- **直接在notebook中显示图形：**

  ```python
  %matplotlib inline
  ```

  
