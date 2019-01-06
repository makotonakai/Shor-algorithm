# Shor-algorithm

## The problem this algorithm aims to solve  
This problem is the algorithm which can solve the factoring problem , which is one of the NP problems, in polynomial time.   For instance, this can find b and c, if a = b*c.

## The mathematical explanation  
This problem can be solved by the following order.

1.Pick two numbers N and a.  N is the number you are trying to factor, and a is something between 1 to N and does not have any common divisor with N.  
  
2. Suppose <img src="https://latex.codecogs.com/gif.latex?f(x)&space;=&space;a^x mod N" title="f(x) = a^x mod N" /> and find the number r,which satisfies <img src="https://latex.codecogs.com/gif.latex?f(x)&space;=&space;f(x&plus;r)" title="f(x) = f(x+r)" />.  

3. 
