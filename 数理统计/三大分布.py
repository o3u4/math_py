from scipy.stats import norm, chi2, t, f
from draw.draw import plot_line, fill_area, plot_vertical_line, add_text
from draw import color
import numpy as np
import matplotlib.pyplot as plt

normal_x = np.linspace(-3, 3, 100)
fig, axs = plt.subplots(2, 2, figsize=(10, 6))
plot_line(normal_x, norm.pdf(normal_x, 0, 1), line_label="$\\mathcal{N}(0, 1)$", ax=axs[0, 0])
axs[0, 0].set_title('标准正态分布')
plot_vertical_line(-1, ax=axs[0, 0], label="$z_p$", color=color.pink[1])
fill_area(normal_x, norm.pdf(normal_x, 0, 1), (normal_x <= -1), ax=axs[0, 0], label="$P(x\leq z_p)$")
"<=-1"
axs[0, 0].legend()

chi2_x = np.linspace(0, 20, 100)
chi2_df = 5
plot_line(chi2_x, chi2.pdf(chi2_x, chi2_df), line_label=f"$\\chi^2({chi2_df})$", ax=axs[0, 1])
axs[0, 1].set_title('$\\chi^2$分布')
">=10"
plot_vertical_line(10, ax=axs[0, 1], label="$\\chi^2_\\alpha$", color=color.pink[1])
fill_area(chi2_x, chi2.pdf(chi2_x, chi2_df), (chi2_x >= 10), ax=axs[0, 1],
          label="$P(\\chi^2\geq \\chi^2_\\alpha)$")
axs[0, 1].legend()

t_x = np.linspace(-5, 5, 100)
t_df = 5
plot_line(t_x, t.pdf(t_x, t_df), line_label=f"$t({t_df})$", ax=axs[1, 0])
axs[1, 0].set_title('$t$分布')
"||>=2"
plot_vertical_line(2, ax=axs[1, 0], label="$\pm t_\\alpha$", color=color.pink[1])
plot_vertical_line(-2, ax=axs[1, 0], color=color.pink[1])
fill_area(t_x, t.pdf(t_x, t_df), (abs(t_x) >= 2), ax=axs[1, 0],
          label="$P(|t|\geq t_\\alpha)$")
axs[1, 0].legend()

f_x = np.linspace(0, 6, 100)
f_df1 = 5
f_df2 = 5
plot_line(f_x, f.pdf(f_x, f_df1, f_df2), line_label=f"$f({f_df1}, {f_df2})$", ax=axs[1, 1])
axs[1, 1].set_title('$f$分布')
">=3"
plot_vertical_line(3, ax=axs[1, 1], label="$F_\\alpha$", color=color.pink[1])
fill_area(f_x, f.pdf(f_x, f_df1, f_df2), (f_x >= 3), ax=axs[1, 1],
          label="$P(F\geq F_\\alpha)$")
axs[1, 1].legend()

plt.show()
