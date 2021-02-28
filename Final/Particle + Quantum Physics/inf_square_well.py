import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

L = 10

xvals = np.linspace(0,L,1000)

A = (2/L)**(0.5)


def psi(n,x):
    wf = A*np.sin(n*pi*x/L)
    return wf

yvals1 = psi(1,xvals)
yvals2 = psi(2,xvals)
yvals3 = psi(3,xvals)

plt.plot(xvals,yvals1, label = "n = 1")
plt.plot(xvals,yvals2, label = "n = 2")
plt.plot(xvals,yvals3, label = "n = 3")
plt.title("Wavefunction for Infinite Square Well / Particle in a Box")
plt.xlabel("x")
plt.ylabel("$\psi$(x)")
plt.xticks([0,10],["0","L"])
plt.grid()
plt.legend()


plt.show()