# Wave Functions

How do we know what wave functions look like?

We know what they mean: when we square them, they become a probability density function for the position of the particle — this is the Born rule. But how do we know what they're going to look like in a given potential? How do we know how it will look later given that we know how it looks now?

While this is kind of outside the IB syllabus, I personally find it very interesting (and quite helpful) to look at wave functions in different potentials.

### Energy Eigenfunctions

The first term to look at is an _energy eigenfunction_. This is basically a fancy term for a wave function that describes a particle with some definite energy. These particle states, whose wave functions we will label with $\phi_E$ (for energy E), satisfy the Schrodinger equation:
$$
i\hbar\frac{\partial\phi_E}{\partial t}=-\frac{\hbar^2}{2m}\frac{\partial^2\phi_E}{\partial x^2}+V(x)\phi_E
$$
Equally importantly, it satisfies the equation
$$
i\hbar\frac{\partial}{\partial t}\phi_E=E\phi_E
$$
which we already saw for a plane wave with angular frequency $\omega=\frac{E}{\hbar}$. 

For those of you familiar with differential equations, this is a separable equation with solution
$$
\phi_E(x,t)=\phi_E(x,0)e^{-i\omega t}
$$
with $\omega = \frac{E}{\hbar}$ and initial wave function $\phi_E(x,0)$. Note that if we had a plane wave $\phi_E(x,0)=e^{ikx}$, this would just be the wave we studied in the "derivation" of the Schrodinger equation.

Note that this differential equation only held because $\phi_E$ was a state with definite energy — in general, applying $i\hbar\frac{\partial}{\partial t}$ to a wave function just spits out another function, completely unrelated to the original wave function. This is why it's particularly useful to study energy eigenfunctions — they evolve in time in a very simple fashion.

### The Free Particle

The free particle is the situation that corresponds to $V(x)$ being constant. Equivalently, we can think of this as $V(x)=0$ (think about why this is). Once again, for those familiar with differential equations, one can attempt to solve the differental equation
$$
E\phi_E=-\frac{\hbar^2}{2m}\frac{\partial^2\phi_E}{\partial x^2}
$$
by rearranging to get
$$
\frac{\partial^2\phi_E}{\partial x^2}=-\frac{2mE}{\hbar^2}\phi_E
$$
and trying an ansatz $\phi_E=e^{px}$. We arrive at the general solution
$$
\phi_E=Ae^{ikx}+Be^{-ikx}
$$
for complex constants $A$ and $B$ and 
$$
k=\frac{\sqrt{2mE}}{\hbar}
$$
where $E>0$. We can recognise this as a superposition of two waves (one left-moving and one right-moving) with wavenumber $k$. Then the wavefunction is
$$
\phi_E(x,t)=Ae^{i(kx-\omega t)}+Be^{-i(kx+\omega t)}
$$
from the result above.

### Qualitative sketches of the wave function

Looking at the Schrodinger equation, we have
$$
E\phi_E=-\frac{\hbar^2}{2m}\frac{\partial^2\phi_E}{\partial x^2}+V(x)\phi_E
$$
which we can rearrange to get
$$
\frac{\partial^2\phi_E}{\partial x^2}=\frac{2m}{\hbar^2}(V(x)-E)\phi_E
$$
If you try to go through solving this differential equation, you come to two cases: either $V(x)>E$ or $E>V(x)$. These correspond to classically allowed and disallowed regions.

<img src="/Users/norrislam/Documents/GitHub/Physics-Revision-Material/Particle + Quantum Physics/regions.png" style="zoom:30%;" />

Suppose you placed a ball in the middle region with total energy $E$. The potential $V(x)$ shows you the potential energy of the ball, and the rest is kinetic energy. As it rolls up the hill to the right, it reaches the point where all of its energy is potential energy. At this point the ball has no kinetic energy and is not moving. It then rolls back down the hill, to the left, where the same thing will occur. The ball will never have enough energy to roll up and over the hill. This allows us to split the area into three regions: the region in the middle, where the ball can be found classically, and the left and right regions, where the ball will never be found classically.

Upon solving for the general solution of the Schrodinger equation, we get
$$
\phi_E=Ae^{\alpha x}+Be^{-\alpha x}
$$
for
$$
\alpha^2=\frac{2m(V(x)-E)}{\hbar^2}
$$
Notice that when $V(x)>E$, $\alpha^2$ is positive so $\alpha$ is a real number. This corresponds to the wave function taking the form of growing and decaying exponentials. Since we know the area under the wave function squared must be a probability, the wave functoin itself must be bounded — it cannot go to infinity. Hence, we know that in region 1, the wave function will be a growing exponential, and in region 3, it will be a decaying exponential. This tells us that in classically disallowed regions, the wave function is a growing or decaying exponential.

However, in classically allowed regions, we have $E>V(x)$ so $\alpha$ is complex — this means that our wave function is oscillatory with wavenumber
$$
k=\frac{\sqrt{2m(V(x)-E)}}{\hbar}
$$
like in the case of the free particle. If we sketch the wave function on the diagram, it might look something like this:

<img src="/Users/norrislam/Documents/GitHub/Physics-Revision-Material/Particle + Quantum Physics/wf.png" style="zoom:30%;" />

modulo my bad art.

Mathematically, we could write it as:
$$
\phi_E(x)=\begin{cases} 
      Ae^{\alpha x} & \text{Region I} \\
      Be^{ikx}+Ce^{-ikx} & \text{Region II} \\
      De^{-\alpha x} & \text{Region III} 
   \end{cases}
$$
Where the constants $A$, $B$, $C$, and $D$ are to be determined by patching together the solution to match up continuously and smoothly at the boundaries of the region.