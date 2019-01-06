# Shor-algorithm

## The problem this algorithm aims to solve  
This problem is the algorithm which can solve the factoring problem , which is one of the NP problems, in polynomial time.   For instance, this can find <img src="https://latex.codecogs.com/gif.latex?b" title="b" /> and <img src="https://latex.codecogs.com/gif.latex?c" title="c" />, if <img src="https://latex.codecogs.com/gif.latex?a" title="a" /> = <img src="https://latex.codecogs.com/gif.latex?b" title="b" /><img src="https://latex.codecogs.com/gif.latex?\quad" title="\quad" /><img src="https://latex.codecogs.com/gif.latex?\bullet" title="\bullet" /><img src="https://latex.codecogs.com/gif.latex?\quad" title="\quad" /><img src="https://latex.codecogs.com/gif.latex?c" title="c" />.

## The mathematical explanation  
This problem can be solved by the following order.

1.Pick two numbers <img src="https://latex.codecogs.com/gif.latex?N" title="N" /> and <img src="https://latex.codecogs.com/gif.latex?a" title="a" />.  <img src="https://latex.codecogs.com/gif.latex?N" title="N" /> is the number you are trying to factor, and <img src="https://latex.codecogs.com/gif.latex?a" title="a" /> is something between 1 to <img src="https://latex.codecogs.com/gif.latex?N" title="N" /> and does not have any common divisor with <img src="https://latex.codecogs.com/gif.latex?N" title="N" />.  
  
2. Suppose <img src="https://latex.codecogs.com/gif.latex?f(x)&space;=&space;a^x&space;mod&space;N" title="f(x) = a^x mod N" /> and find the number r,which satisfies <img src="https://latex.codecogs.com/gif.latex?f(x)&space;=&space;f(x&plus;r)" title="f(x) = f(x+r)" />.
3. Because <img src="https://latex.codecogs.com/gif.latex?a^r&space;=&space;1" title="a^r = 1" />, it can be said that <img src="https://latex.codecogs.com/gif.latex?N&space;=&space;(a^r/2&space;&plus;&space;1)(a^r/2&space;-&space;1)" title="N = (a^r/2 + 1)(a^r/2 - 1)" />
