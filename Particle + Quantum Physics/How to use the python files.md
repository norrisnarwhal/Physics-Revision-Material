# How to use the python files in this folder

Included in this folder are python files. They can be opened with any program that can run python, but I would recommend using PyCharm.

### QHO_Fin.py

This file displays the energy eigenstates of the quantum harmonic oscillator, given by the potential $V(x)=\frac{1}{2}{m}{\omega}^2 x^2$. The eigenfunctions are not properly normalised, but rather scaled so they are displayed nicely.

This is a good visual to look at (qualitatively) what energy eigenstates of a potential look like, as well as to see how the allowable energies in one dimensional bound states are discrete.

You can edit the python file to show as many energy eigenstates you want by editing the range of $l$.

### inf_square_well.py

This file displays the energy eigenstates of the infinite square well potential, or the "particle in a box". Same as the QHO file, this is good for looking at the eigenstates of a given potential, but this time with boundary conditions $V\to\infty$ on the sides of the well.

Unfortunately, this time the energy eigenstates are hard-coded so you can't show as many eigenstates as you want.



For both files, notice that as $E$ increases, the wavelength of the eigenstate in the classically allowed region decreases — this fits the equations
$$
E=\frac{hc}{\lambda},\,p=\frac{h}{\lambda}
$$
