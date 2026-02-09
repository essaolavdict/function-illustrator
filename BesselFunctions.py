# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: function-illustrator
#     language: python
#     name: function-illustrator
# ---

# %% [markdown]
# # Jupyter notebook for function illustration

# %% [markdown]
# #### Import modules

# %%
# %matplotlib ipympl
import numpy as np
from scipy.special import jv
import matplotlib.pyplot as plt

from matplotlib.lines import Line2D

# %% [markdown]
# #### Generate some data

# %%
x = np.linspace(0, 10, 100)

# %% [markdown]
# #### Plot:

# %%
fig, ax = plt.subplots()
ax.axhline(0, color='xkcd:gray', lw=2, linestyle='-')
ax.plot(x, jv(0, x), dashes=(6, 2), lw = 2, color = 'xkcd:azure', label = "$J_{0}(x)$")
ax.plot(x, jv(1, x), dashes=(2, 2), lw = 2, color = 'xkcd:melon', label = "$J_{1}(x)$")
ax.plot(x, jv(2, x), dashes=(3, 1, 1, 1), lw = 2, color = 'xkcd:jade', label = "$J_{2}(x)$")

legend_data = [Line2D([], [], dashes=(6, 2), lw = 2, color = 'xkcd:black', label = r'$\alpha=0$'),
               Line2D([], [], dashes=(2, 2), lw = 2, color = 'xkcd:black', label = r'$\alpha=1$'),
               Line2D([], [], dashes=(3, 1, 1, 1), lw = 2, color = 'xkcd:black', label = r'$\alpha=2$')
              ]
ax.legend()
leg = fig.legend(handles=legend_data, title="Integer orders:", loc="upper left", bbox_to_anchor=(0.4, 0.88))
leg.get_title().set_ha("left")
for text in leg.get_texts():
    text.set_ha("left")
leg._legend_box.align = "left"

ax.set_xlabel('$x$')
ax.set_ylabel('$J_{n}$')
ax.set_xlim([0, 10])
ax.set_title('Bessel functions of the first kind')
plt.show()

# %%
