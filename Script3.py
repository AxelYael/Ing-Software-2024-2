import matplotlib
matplotlib.use('TkAgg')  # o el backend que prefieras: Qt5Agg, GTK3Agg, etc.

import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x**2

x = np.linspace(-10, 10, 100)

y = f(x)

plt.plot(x, y)
plt.title('Gráfica de una función cuadrática')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
