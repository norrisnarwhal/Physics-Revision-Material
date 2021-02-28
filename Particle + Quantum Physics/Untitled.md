# Wave Functions

How do we know what wave functions look like?

We know what they mean: when we square them, they become a probability density function for the position of the particle — this is the Born rule. But how do we know what they're going to look like in a given potential? How do we know how it will look later given that we know how it looks now?

While this is kind of outside the IB syllabus, I personally find it very interesting (and quite helpful) to look at wave functions in different potentials.

The first term to look at is an _energy eigenfunction_. This is basically a fancy term for a wave function that describes a particle with some definite energy. These particle states, whose wave functions we will label with $\phi_E$ (for energy E), satisfy the Schrodinger equation:
$$
i\hbar\frac{\partial\phi_E}{\partial t}=-\frac{\hbar}{2m}\frac{\partial^2\phi_E}{\partial x^2}+V(x)\phi_E
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