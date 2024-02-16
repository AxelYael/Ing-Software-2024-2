import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x**2

x = np.linspace(-10, 10, 100)
y = f(x)


plt.plot(x, y)
plt.title('Funcion cuadrática')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
