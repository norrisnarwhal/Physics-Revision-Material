# How should we solve problems in classical mechanics?

After the first few months of doing physics, you quickly realise that there seem to be two main ways of doing classical mechanics problems: SUVAT equations and $F=ma$, and using the idea of energy. In fact, these two methods are equivalent, but showing the link between the two requires mathematical technicalities and Lagrangians and Hamiltonians and differential equations so it is often better to just deal with them separately (as I am about to do here).

### The SUVAT equations

These equations deal with motion with a constant acceleration $a$. The following will be a derivation of the SUVAT equations without calculus (a derivation using calculus will be in a separate file). First, we look at $a$. The acceleration is just a change in velocity over time:
$$
a=\frac{\Delta v}{\Delta t}
$$
But the change in velocity is just the difference between the final and initial velocities, so we can write this as
$$
a=\frac{v_f-v_i}{\Delta t}
$$
If we just write $\Delta t$ as $t$ (by just defining our initial time to be $t=0$), we can rearrange to get
$$
\begin{aligned}
a&=\frac{v_f-v_i}{t}\\
v_f&=v_i+at
\end{aligned}
$$
which is the first of the SUVAT equations.

The average velocity over some time can be thought of as:
$$
v=\frac{v_i+v_f}{2}
$$
which is an approximation that can be made better and better by looking at $v_i$ and $v_f$ over shorter time intervals. Velocity is also the change in position over time, so we have:
$$
\frac{v_i+v_f}{2}=\frac{\Delta x}{t}
$$
Substituting the previous equation $v_f=v_i+at$ into this equation, we have
$$
\begin{aligned}
\frac{v_i+(v_i+at)}{2}&=\frac{\Delta x}{t}\\
\frac{(2v_i+at)}{2}&=\frac{\Delta x}{t}\\
t(2v_i+at)&=2\Delta x\\
v_it+\frac{1}{2}at^2&=\Delta x
\end{aligned}
$$
Recognising that $\Delta x$ is the displacement (commonly written as $s$ in IB textbooks), we now arrive at the second SUVAT equation
$$
s=v_it+\frac{1}{2}at^2
$$
For the final equation, we look back at the definitions of $a$ and $v$:
$$
\begin{aligned}
a&=\frac{\Delta v}{t}\\
v&=\frac{\Delta x}{t}
\end{aligned}
$$
We can rearrange for $t$ in both equations and set them equal to each other:
$$
t=\frac{\Delta v}{a}=\frac{\Delta x}{v}
$$
using once again that $v=\frac{v_i+v_f}{2}$ and $\Delta v=v_f-v_i$, we get:
$$
\begin{aligned}
\frac{\Delta v}{a}&=\frac{\Delta x}{v}\\[1 em]
v\Delta v&=a\Delta x\\[1 em]
\Big(\frac{v_i+v_f}{2}\Big)(v_f-v_i)&=a\Delta x\\[1 em]
(v_f+v_i)(v_f-v_i)&=2a\Delta x\\[1 em]
v_f^2-v_i^2=2a\Delta x\\[2 em]
v_f^2=v_i^2+2as
\end{aligned}
$$
where in the final line we have used once again $s=\Delta x$. This is the third SUVAT equation. For many problems, it will be necessary to choose the correct equation to use given the quantities that are provided in the question, and then to rearrange it for the variable that needs to be solved for.

### F=ma

Quite often, the acceleration will be unknown. In this case, you will need to find resultant force acting on the body — the best way to do this is by considering all of the forces acting on the body through a free body diagram. Unfortunately, the skill of drawing these appears to be commonly lost after a year of not doing any problems. Here, I present to you a quick way of remembering how to draw free body diagrams:

1. Draw all the forces you know are acting on it. This usually includes weight, tension, friction, and the finger pushing the block up the slope.
2. Draw the _reaction forces_. These are the contact forces between objects like a mass and the "smooth, frictionless table" that seems to always show up in questions.
3. Draw the angles on and remember how to decompose forces into components by using the right trig functions.
4. The **sum** of these forces will give you $ma$.

### "The energy method"

Another common way of approaching mechanics problems is by considering the conservation of energy. This will usually be for questions that have a mass falling with a spring involved. This requires thinking about where energy gets transferred to and from. When something is falling, it's losing gravitational potential energy; when it is speeding up, it gains kinetic energy; when an object compresses or stretches a spring, it loses energy **to the spring**.

An important result that comes up extremely often is the velocity of an object after falling through a height $h$
$$
\begin{aligned}
\frac{1}{2}mv^2&=mgh\\
v^2&=2gh\\
v&=\sqrt{2gh}
\end{aligned}
$$
which is an equation that comes up so often that it entirely surpasses the category of equations dubbed "important to memorise since it isn't in the data booklet" and moves into the category "I've calculated this so many times I know it by heart". As such, any time spent memorising this equation will be wasted as doing a sufficient number of problems should do the trick.