# Shor-algorithm

## The problem this algorithm aims to solve  
This problem is the algorithm which can solve the factoring problem , which is one of the NP problems, in polynomial time.   For instance, this can find b and c, if a = b*c.

## The mathematical explanation  
This problem can be solved by the following order.

1.Pick two numbers N and a.  N is the number you are trying to factor, and a is something between 1 to N and does not have any common divisor with N.  
  
2. Suppose  and find the number r,which satisfies <img src="https://latex.codecogs.com/gif.latex?f(x)&space;=&space;f(x&plus;r)" title="f(x) = f(x+r)" />.
3. Because <img src="https://latex.codecogs.com/gif.latex?a^r&space;=&space;1" title="a^r = 1" />, it can be said that <img src="https://latex.codecogs.com/gif.latex?N&space;=&space;(a^r/2&space;&plus;&space;1)(a^r/2&space;-&space;1)" title="N = (a^r/2 + 1)(a^r/2 - 1)" />
