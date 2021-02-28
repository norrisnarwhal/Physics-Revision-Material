# Concepts in Classical Mechanics

There are some important rules in classical mechanics that will (basically) always hold when looking at situations like throwing a ball in the air or tossing failed homework assignments in the rubbish bin. I'm not talking about Newton's Laws (yet); these rules are more fundamental, more of a set of guidelines that any formulation of classical mechanics should follow.

1. The rules of classical mechanics should make sense when time runs backwards.

This feels kind of strange; we live life with time running forwards, so why should the laws of physics be the same when time runs backwards? The truth is that this rule isn't always true: the thermodynamics tells us that entropy tends to increase, so clearly time symmetry can't always hold. But think about smaller scale situations like a pendulum: its motion is described by a wave:

<img src="/Users/norrislam/Documents/GitHub/Physics-Revision-Material/Classical Mechanics/desmos-graph.png" style="zoom:35%;" />

But if you recorded a video of the pendulum and played it backwards, there would be essentially no difference in its motion since taking $t\to -t$ in this graph would still result in a wave:

<img src="/Users/norrislam/Documents/GitHub/Physics-Revision-Material/Classical Mechanics/desmos-graph (1).png" style="zoom:35%;" />

So this "experiment" is time-reversal invariant.



2. The laws of physics are deterministic.

We know this doesn't hold in quantum mechanics, but we're dealing with classical mechanics so it's fine. What this means is that if you describe to me the physical state of the system, then given enough information I can tell you what the state will look like some time in the future (equivalently, since classical systems are time-reversal invariant, I can tell you what it looked like in the past). Given a ball with position $x$ and momentum $p$, I can quite confidently tell you how it will move given that I also know the forces acting on the ball, how the forces change in time etc.

### Newton's equations

One of the most important equations in classical mechanics is Newton's $F=ma$. However, we could then ask, why not $F=mv$? why acceleration? Turning our attention back to a pendulum or a spring, we know (or perhaps will soon find out) that the force acting on the mass is negatively proportional to its displacement, given by $F=-kx$. Now imagine a world where force dictated the velocity of the mass instead of the acceleration. We would get:
$$
\begin{aligned}
mv&=-kx\\
v&=-\frac{k}{m}x
\end{aligned}
$$
Now imagine holding the mass on a pendulum at some initial displacement, then letting go. This equation would tell you that as it reaches the central point it slows down, until eventually it reaches $0$ at the central "equilibrium point". This violates some of the rules above: it's not deterministic, since given the mass at any point its velocity is always the same at that point, so you can't reach into the past and deduce its state in the time leading up to that point. It's also not time-reversal invariant; if it were, we'd have pendula that would spontaneously move from its central position with no external force. This is one reason why we know that Newton's equations are right. The other reason, of course, is that we've thrown balls in the air and Newton's equations work.