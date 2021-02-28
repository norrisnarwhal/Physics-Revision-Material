# "Deriving" the Schrodinger Equation

It is important to note that this will not be, in any sense, a rigorous derivation of the Schrodinger Equation (henceforth referred to as the SE) from first principles. This is not me being lazy, but rather due to the fact that _no one can_ derive quantum mechanics from first principles. We can, however, tell a story that will let the SE make more sense.

## The Setup

### De Broglie Relations

We first start with De Broglie's idea of matter waves. This stemmed from observations from experiments such as the double slit experiment where matter appeared to have some inherent "waviness" to their dynamics. This resulted in some quite important equations:
$$
p=\frac{h}{\lambda}
$$
and
$$
E=hf
$$
where $h$ is Planck's constant (just a number). These equations relate quantities associated with a wave (wavelength $\lambda$ and frequency $f$) with the physical quantities momentum $p$ and energy $E$.

### Wave functions?

Since the Schrodinger Equation dictates the evolution of this quantity called the "wave function", it may be instructive to study some functions that describe waves. One such function would be:
$$
\cos(x)
$$
Now, we can add parameters to this function to allow us more control over the details of this wave; for example, we can give it a wavelength $\lambda$:
$$
\cos\Big(\frac{2\pi}{\lambda}x\Big)
$$
Now that looks kind of messy so let's define now the wavenumber $k=\frac{2\pi}{\lambda}$ to clean this expression up:
$$
\cos(kx)
$$
Let's now make this wave move to the right with angular frequency $\omega$ (remember that $\omega=2\pi f$):
$$
\cos(kx-\omega t)
$$
This can be quickly verified by considering function transformations; when $t=0$, we just get the wave $\cos(kx)$. When $t=1$, the wave moves to the right by $\omega$, becoming $\cos(kx-\omega)$. We can hence see that when time increases, the wave shifts to the right with an angular frequency of $\omega$ (if $\omega$ were to be negative, it would be a left-moving wave).

The more mathematically inclined may also know the equation
$$
e^{ix}=\cos(x)+i\sin(x)
$$
giving us a nice way to write a wave as an exponential involving $i$ (for those that aren't familiar with this, just know what this was a magical equation worked out centuries ago that involves a number called "$i$" whose only special quality is that squaring it returns $i^2=-1$).

We can then rewrite the wave we have as:
$$
e^{i(kx-\omega t)}
$$
which we can now play around with as our "wave function".

### Scary symbols

The more mathematically ambitious of you may be inclined to take derivatives of the function
$$
\psi(x,t)=e^{i(kx-\omega t)}
$$
However, there's some ambiguity as to which variable we should take derivatives with respect to; since $\psi$ is a function of both $x$ and $t$, it is equally fair to take derivatives with respect to either of these variables. As such, we will do both.
$$
\begin{aligned}
\frac{\partial\psi}{\partial x}&=ike^{i(kx-\omega t)}\\
\frac{\partial\psi}{\partial t}&=-i\omega e^{i(kx-\omega t)}
\end{aligned}
$$
Notice that the derivatives are written with a curly $\partial$ instead of $d$ to remind us that there is more than one variable we could take the derivative with respect to. To compute the derivatives, we have leveraged the fact (via the chain rule) that taking the derivative of the exponential of something times $x$ simply returns the same exponential with the something in front.

These equations are very similar to the De Broglie relations! This is made more clearer when we substitute the wavefunction $\psi$ back when we see the exponential:
$$
\begin{aligned}
\frac{\partial\psi}{\partial x}&=ik\psi\\
\frac{\partial\psi}{\partial t}&=-i\omega\psi
\end{aligned}
$$
and recalling the De Broglie relations (this time with $k$):
$$
\begin{aligned}
p&=\hbar k\\
E&=\hbar\omega
\end{aligned}
$$
where we have defined $\hbar=\frac{h}{2\pi}$. This has a fancy name: the "reduced Planck's constant" (but no one will tell you if you just call it Planck's constant). By multiplying the derivatives by the suitable factors of $\hbar$ and $i$, we can get:
$$
\begin{aligned}
-i\hbar\frac{\partial\psi}{\partial x}&=\hbar k\psi\\
i\hbar\frac{\partial\psi}{\partial t}&=\hbar\omega\psi
\end{aligned}
$$
Which then gives us:
$$
\begin{aligned}
-i\hbar\frac{\partial\psi}{\partial x}&=p\psi\\
i\hbar\frac{\partial\psi}{\partial t}&=E\psi
\end{aligned}
$$

### Another way of getting the energy

We know that the total energy of a particle is just the sum of its kinetic and potential energy:
$$
E=E_K+E_P
$$
Since the potential energy is simply an energy that depends on where you are, we can write it as
$$
E_P=V(x)
$$
The kinetic energy can be written as
$$
E_K=\frac{1}{2}mv^2
$$
or alternatively, with $p=mv$,
$$
E_K=\frac{p^2}{2m}
$$
You can quickly verify this is true by making the substitution $p=mv$.

Looking back at the previous section, we had
$$
-i\hbar\frac{\partial}{\partial x}\psi=p\psi\\
$$
Where we got a factor of $p$ in front of our wavefunction by differentiating with respect to $x$ and then multiplying by $-i\hbar$. It wouldn't be too hard to imagine then that to get $p^2$, we simply differentiate and multiply again. Then, we get
$$
p^2\psi=-\hbar\frac{\partial^2\psi}{\partial x^2}
$$
Looking back at the "energy equation" and multiply by $\psi$, we get:
$$
E\psi=\frac{p^2}{2m}\psi+V(x)\psi
$$
and now substituting what we got for $p^2$:
$$
E\psi=-\frac{\hbar}{2m}\frac{\partial^2\psi}{\partial x^2}+V(x)\psi
$$

## Schrodinger's contribution

This is the bit that really made the Schrodinger Equation. We now have two ways of writing the energy $E\psi$:
$$
E\psi=i\hbar\frac{\partial\psi}{\partial t}
$$
and
$$
E\psi=-\frac{\hbar}{2m}\frac{\partial^2\psi}{\partial x^2}+V(x)\psi
$$
Putting these two together, we get:
$$
i\hbar\frac{\partial\psi}{\partial t}=-\frac{\hbar}{2m}\frac{\partial^2\psi}{\partial x^2}+V(x)\psi
$$
which is commonly referred to as "the Schrodinger equation".