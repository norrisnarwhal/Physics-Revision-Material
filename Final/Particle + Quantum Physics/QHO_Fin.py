import matplotlib.pyplot as plt
import numpy as np
import math

for l in range (0,4,1):
  epsilon = l+0.5
  N = 60000 # iterations

  n=-1*N+2
  h = 0.0001
  h2 = pow(h,2)

  y = 0.0
  k = 0.0
  x = -1*(N-2)*h

  X = []
  Y = []

  k_minus_2 = epsilon + x-2*h # k_0
  k_minus_1 = epsilon + x-h # k_1
  a = 0.1
  y_minus_2 = 0 # y_0
  y_minus_1 = (epsilon+1)**5*a # y_1

  while n<N-2:
    n+=1
    x += h;
    k = 2*epsilon - pow(x, 2)
    b = h2/12
    y = ( 2*(1-5*b*k_minus_1) * y_minus_1 - (1+b*k_minus_2) * y_minus_2 ) / (1 + b * k)

    # x and y values for plotting
    X.append(x)
    Y.append(y)

    # Shift for next iteration
    y_minus_2 = y_minus_1
    y_minus_1 = y
    k_minus_2 = k_minus_1
    k_minus_1 = k
  Y_s = [(pow(10,-2)*y + epsilon*pow(10,9))*pow(10,-9) for y in Y]
  plt.plot(X, Y_s, label="$\epsilon = "+repr(epsilon)+"$")


x=np.linspace(-2,2,1000)
y=pow(x,2)
plt.plot(x,y)

# Plot
plt.figure(1)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Energy Eigenstate in QHO")
plt.legend(loc=1)
plt.show()