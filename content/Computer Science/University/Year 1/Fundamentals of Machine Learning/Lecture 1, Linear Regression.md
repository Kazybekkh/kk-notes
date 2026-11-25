


# Random Sampling
- Use $r^2$ value
# Grid search


- How to go at it?
	- Iteratively
	- or minimising error

**A generic c parameter- fitting method: || The Gradient descent method**
1. Start a random point $p_1$ in parameter space
2. Calculate the error at $p_1$
3. Move to another point $p_2$ nearby
4. Calculate the error at $p_2$
	1. when do we stop? - deterministic, no randomness
	1. Run of data points
	2. Set a limit
	3. Satisfied
	4. Realise you're no longer learning
5. Repeat steps 3-4 until the error is less than a threshold, or N steps have been taken

- Stochastic = with randomness
- Deterministic = no randomness


Most common error norms

- L1 norm: 
	$$\text{error}=\sum^m_{i=1}|y_i^{pred}-y_i^{data}|$$
- L2 norm:
	$$\text{error}=\sqrt{\sum^m_{i=1}(y_i^{pred}-y_i^{data})^2}$$
	- Harsher (default)
	- more conservative, small values

Another name for the error is **cost function** or **loss function**


# A stochastic parameter - fitting method
- This is the core idea behind genetic algorithms
	- Mutation and Selection
	- min(L2_norm)
ln1 dimesion
- Calculus
- $d(loss)/da=0$
2 dimensions
- Going down the gradient













