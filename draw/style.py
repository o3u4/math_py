import numpy as np
import matplotlib.pyplot as plt

# Define the function y = x^2
x = np.linspace(-10, 10, 400)
y = x**2

# Loop through all available styles and plot y = x^2 for each
for style in plt.style.available:
    plt.style.use(style)
    plt.figure(figsize=(6, 4))
    plt.plot(x, y)
    plt.title(f'Style: {style}')
    plt.xlabel('x')
    plt.ylabel('y = x^2')
    plt.show()
