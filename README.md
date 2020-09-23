# Simple Quantum Mechanical Systems

This generic code solves for, and plots, the eigenfunctions and eigenvalues of a particle in a one-dimensional potential, based on the finite difference method code introduced by @mholtrop. Interesting potentials are:

## 1. the quantum harmonic oscillator
```
V = x**2
```

## 2. the finite square well
```
# well depth
d = 5

# well width (spans one-third of the x axis range)
a = int(n/3)
b = int(2*n/3)

V = np.zeros(n)
V[0:a] = d
V[b:n] = d
```

## 3. the finite barrier
```
# barrier height
h = 5

# barrier width (spans one-third of the x axis range)
a = int(n/3)
b = int(2*n/3)

V = np.zeros(n)
V[a:b] = h
```
The finite barrier potential generates pairs of eigenfunctions, as this method does not specify from which side the particle enters the system.

## 4. the sine-squared function
```
V = np.sin(x)**2
```
This potential generates eigenfunctions similar to those of an electron in the periodic potential of a lattice.
