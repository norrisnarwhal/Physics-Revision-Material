# WHICH HAND DO I USE?

In this document I will attempt to remove any doubts you may have about when to use the left hand rule and when to use the right hand rule.

### The Left Hand

First, we have to understand why the left hand rule works. We know the equation for the force on a charge in a magnetic field as:
$$
F=qvB\sin(\theta)
$$
where $q$ is the charge on the particle, $v$ is the velocity of the particle, $B$ is the **B**agnetic field strength and $\theta$ is the angle the particle's path makes with the magnetic field. However, it's more instructive to look at this as a vector equation:
$$
\vec{F}=q(\vec{v}\times\vec{B})
$$
where the quantities are still the same except endowed with a sense of direction. The $\times$ represents a cross product: essentially, it takes the two vectors and spits out a vector perpendicular to both of them with a length $|v||B|\sin(\theta)$. However, one quickly realises that there are two directions that this perpendicular vector can point in; either

<img src="/Users/norrislam/Documents/CAS/E&M/LH1.png" style="zoom:25%;" />

or

<img src="/Users/norrislam/Documents/CAS/E&M/LH2.png" style="zoom:25%;" />

both of which are valid candidates for being the perpendicular vector. Note that the first and second are simply flipped, showing that the difference between the two is a factor of $-1$. We define $\vec{v}\times\vec{B}$ to be the vector in the first image, such that a vector along the positive $x-$axis crossed with a vector along the positive $y-$axis forms a vector that lies on the positive $z-$axis. At this point, we can see why the left hand rule may be useful:

![](/Users/norrislam/Documents/CAS/E&M/FBI.png)

Since the "current" is given by moving charge, we have the perfect way to remember which way the force vector goes using the left hand rule (the reason I choose to remember it as FBI is because it's a preexisting set of three letters). When questions ask a question involving a wire in a current, they will often use conventional current — the idea of current as the flow of positive charge. Then the force is 
$$
\vec{F}=+q(\vec{v}\times\vec{B})
$$
so this works. However, when the charge is negative, like an electron moving in an electric field, this becomes
$$
\vec{F}=-q(\vec{v}\times\vec{B})
$$
which is nearly identical to the previous vector, except with an extra factor of $-1$. Then, the force vector must point in the opposite direction. One solution would be to use the right hand instead of left hand, still with the thumb pointing in the direction of $\vec{F}$, the index finger in the direction of $\vec{B}$, and the middle finger in the direction of the motion of the charge. However, to avoid confusion, one could easily just continue to use the left hand but point the current in the opposite direction. Since negative charge moving one way ("real current") is computationally the same as positive charge flowing the other way ("conventional current"), it suffices to simply always point the middle finger in the direction of conventional current.

### The Right Hand

The left hand rule will always be used in that awkward tripod pose, corresponding coincidentally to the question that comes up more often than the ones that require the right hand rule. One can only assume this is a gift from the exam board so that we can continue to grip our pens and write with our right hand.

However, the situation still arises when the right hand must be used. This will only be in questions with a current generating a magnetic field, or when a current must be induced to generate a magnetic field. The right hand is used as such:

<img src="/Users/norrislam/Documents/CAS/E&M/RH rule.png" style="zoom:150%;" />

Given a wire with a current flowing through it, grip the wire (not actually, just imagine it) with your right hand with your thumb pointing in the direction of *conventional* current. The direction your fingers wrap around the wire will be the direction the generated magnetic field moves in. Other questions where the right hand may be used is in questions involving Lenz's law with a current being generated in a loop of wire:

![](/Users/norrislam/Documents/CAS/E&M/lenz.png)

In this case, the simplest method would be to first consider the change in magnetic flux. Since the magnetic is moving through the ring, the magnetic flux in the area enclosed by the ring is increasing (imagine the magnetic field being pushed through the ring). According to Lenz's law, the current induced in the ring must be generating a magnetic field opposing this motion — the magnetic field needs to be pointing upwards. At this point, you can either use the right hand as before and point your curled fingers up through the ring and find which way your thumb points. Alternatively, point your thumb in the direction of the induced magnetic field (upwards) and see which way your fingers curl. Either way, we get the same answer.