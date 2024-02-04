import matplotlib.pyplot as plt
import numpy as np

import os
def absRef(relRef): # funksjon for å finne absolutt referanse til en fil fra relativ referanse
    return os.path.join(os.path.dirname(__file__), relRef)


funksjon = 'x**2-4*x+12'

def f(x):
  return eval(funksjon)

xverdier = np.linspace(0, 10, 21)
yverdier = f(xverdier)


plt.style.use('bmh')

plt.subplot(1, 2, 1)
plt.scatter(xverdier, yverdier, color='red', zorder=2)
plt.plot(xverdier, yverdier, zorder=1)

plt.title(f'Funksjonen ${funksjon}$')
plt.xlabel('$x$')
plt.ylabel('$y$')


funksjon = '-0.3*x**3'

plt.subplot(1, 2, 2)
plt.plot(xverdier, f(xverdier))
plt.plot(xverdier, f(xverdier)*2)

plt.title(f'Funksjonen ${funksjon}$')
plt.xlabel('$x$')
plt.ylabel('$y$')


plt.savefig(absRef('plot/testPlot.png'))
plt.show()