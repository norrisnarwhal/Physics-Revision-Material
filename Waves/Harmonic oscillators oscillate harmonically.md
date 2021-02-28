# Harmonic oscillators oscillate harmonically

The most common example of a harmonic oscillator is a mass on a spring. We know that the force on the mass exerted by the spring is given by
$$
F=-kx
$$
where $x$ is the distance of the mass from the equilibrium position. The negative sign is there to remind you that the force is opposite to the direction of the displacement — it pulls the mass back towards the equilibrium position (which is why it's called a restoring force).

Writing $F=ma$, we get:
$$
ma=-kx\implies a=-\frac{k}{m}x
$$
We can fit this with the equation for harmonic motion, $a=-\omega^2 x$, by simply letting $\omega=\sqrt{\frac{k}{m}}$:
$$
a=-\Big(\sqrt{\frac{k}{m}}\Big)^2x
$$
showing that the mass-spring system is indeed a harmonic oscillator.



We can do a similar analysis with a pendulum, which is a fun exercise that I encourage everyone to try out.

- Hints: Let the angle the bob makes with the vertical be $\theta$. Realise that the force acting on the bob will be gravity, with magnitude $mg$. The only component of this force we care about is the component acting along the arc the bob travels on. Try to find an equation of the form $a=-\omega^2 x$ but for an angular acceleration and angular displacement $\theta$ (the approximation $\theta\approx\sin(\theta)$ will be necessary).
- Note: the necessity of the small angle approximation to match the dynamics of a pendulum to the equation describing simple harmonic motion shows that pendula only approximate harmonic oscillators for small angles; they are harmonic approxilators, if you will.



Turning back to the Desmos graph (https://www.desmos.com/calculator/e3zx3twb8e), we can study the point moving up and down as a harmonic oscillator.

Upon varying the amplitude, the velocity of the point as it moves through the center increases. Does this make sense? When it has a larger amplitude, the particle has "more room" to accelerate. Remember; the velocity of the point as it passes through the centre is the sum of all the contributions of the acceleration as it moves from maximum displacement to the centre. When we increase the amplitude, all the previous contributions are still going to be there — the acceleration is dependent only on the point's current position. By increasing the amplitude, we give the point more of a "run up", allowing it to accelerate more before passing through the center. Of course, with an increased velocity through the center, it now takes longer to decelerate to $0$ velocity, which is why it has a larger amplitude.

Now, change what we previously called the "wavelength". This is in reality now the period of the oscillation — we can view the graph as a displacement-time graph.