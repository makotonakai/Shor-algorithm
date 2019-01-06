# Shor-algorithm

## The problem this algorithm aims to solve  
This problem is the algorithm which can solve the factoring problem , which is one of the NP problems, in polynomial time.   For instance, this can find <img src="https://latex.codecogs.com/gif.latex?b" title="b" /> and <img src="https://latex.codecogs.com/gif.latex?c" title="c" />, if <img src="https://latex.codecogs.com/gif.latex?a" title="a" /> = <img src="https://latex.codecogs.com/gif.latex?b" title="b" /><img src="https://latex.codecogs.com/gif.latex?\quad" title="\quad" /><img src="https://latex.codecogs.com/gif.latex?\bullet" title="\bullet" /><img src="https://latex.codecogs.com/gif.latex?\quad" title="\quad" /><img src="https://latex.codecogs.com/gif.latex?c" title="c" />.

## The mathematical explanation  
This problem can be solved by the following order.

1.Pick two numbers <img src="https://latex.codecogs.com/gif.latex?N" title="N" /> and <img src="https://latex.codecogs.com/gif.latex?a" title="a" />.  <img src="https://latex.codecogs.com/gif.latex?N" title="N" /> is the number you are trying to factor, and <img src="https://latex.codecogs.com/gif.latex?a" title="a" /> is something between 1 to <img src="https://latex.codecogs.com/gif.latex?N" title="N" /> and does not have any common divisor with <img src="https://latex.codecogs.com/gif.latex?N" title="N" />.  
  
2. Suppose <img src="https://latex.codecogs.com/gif.latex?f(x)&space;=&space;a^x&space;mod&space;N" title="f(x) = a^x mod N" /> and find the number <img src="https://latex.codecogs.com/gif.latex?r" title="r" />(<img src="https://latex.codecogs.com/gif.latex?r\neq0" title="r\neq0" />),which satisfies <img src="https://latex.codecogs.com/gif.latex?f(x)&space;=&space;f(x&plus;r)" title="f(x) = f(x+r)" />.
3. Because <img src="https://latex.codecogs.com/gif.latex?a^r&space;=&space;1" title="a^r = 1" />, it can be said that <img src="https://latex.codecogs.com/gif.latex?N&space;=&space;(a^r/2&space;&plus;&space;1)(a^r/2&space;-&space;1)" title="N = (a^r/2 + 1)(a^r/2 - 1)" />  

## algorithm  
I'm going to factor 14 here, and <img src="https://latex.codecogs.com/gif.latex?a" title="a" />=5, <img src="https://latex.codecogs.com/gif.latex?N" title="N" /> = 14.  

According to the ```period.py```, <img src="https://latex.codecogs.com/gif.latex?r&space;=&space;6" title="r = 6" />.  

(<img src="https://latex.codecogs.com/gif.latex?a^0&space;mod&space;N&space;=&space;1" title="a^0 mod N = 1" />,
<img src="https://latex.codecogs.com/gif.latex?a^1&space;mod&space;N&space;=&space;5" title="a^1 mod N = 5" />,
<img src="https://latex.codecogs.com/gif.latex?a^2&space;mod&space;N&space;=&space;11" title="a^2 mod N = 11" />,
<img src="https://latex.codecogs.com/gif.latex?a^3&space;mod&space;N&space;=&space;13" title="a^3 mod N = 13" />,
<img src="https://latex.codecogs.com/gif.latex?a^4&space;mod&space;N&space;=&space;9" title="a^4 mod N = 9" />,
<img src="https://latex.codecogs.com/gif.latex?a^5&space;mod&space;N&space;=&space;3" title="a^5 mod N = 3" />)  

 <img src="https://latex.codecogs.com/gif.latex?r" title="r" /> has 6(2^3) gates, and the maximum value of the reminder is 13 , which is less than 16(2^4), so let's make an oracle which shows r(q1) and reminder(q2).  This is the oracle that I created.
 
 In order to get <img src="https://latex.codecogs.com/gif.latex?|0\rangle" title="|0\rangle" /> to <img src="https://latex.codecogs.com/gif.latex?|6\rangle" title="|6\rangle" />, I put hadamard gates on the all the qubits.
 
 Then, put the oracle that I mentioned. You can see the same codes down below in the `Factoring.py`  
 
```   
for i in range(nx):
	qc.h(q1[i])
qc.x(q2[3])
qc.cx(q1[0],q2[0])
qc.cx(q1[1],q2[0])
qc.cx(q1[1],q2[2])
qc.cx(q1[2],q2[1])
qc.ccx(q1[0],q1[2],q2[0])
qc.ccx(q1[0],q1[2],q2[1])
qc.ccx(q1[0],q1[2],q2[2])
qc.ccx(q1[1],q1[2],q2[2])  
```  
Then, if you apply the inverse quantum fourier transform, you would get all the reminders(from the one when <img src="https://latex.codecogs.com/gif.latex?r=0" title="r=0" /> to <img src="https://latex.codecogs.com/gif.latex?r=5" title="r=5" />.  If you don't know about the inverse quantum fourier transform, please refer to my Quantum Fourier Transform repository.

Here is the result on the QASM simulator.  
![shor_oracle_sim](https://user-images.githubusercontent.com/45162150/50736795-118b7780-1205-11e9-8d92-f19d84ee9c3e.png)

And, this is the result on ibmq_20_tokyo.  
![shor_oracle_tokyo](https://user-images.githubusercontent.com/45162150/50736806-397adb00-1205-11e9-9582-9fc0197e901b.png)  

So, we got 1,3,5,7,9,11,13.  In this case, 7 = 1 + 6, 9 = 3 + 6, 11 = 5 + 6, 13 = 1 + 6 * 2. So, the period is 6, which is the same value as what we got from the `period.py`.    
  
 Therefore, <img src="https://latex.codecogs.com/gif.latex?5^{6/2}&space;-&space;1&space;=&space;124" title="5^{6/2} - 1 = 124" /> and <img src="https://latex.codecogs.com/gif.latex?gcd(14,124)&space;=&space;2" title="gcd(14,124) = 2" />, which is a prime number.  Then <img src="https://latex.codecogs.com/gif.latex?14&space;/&space;2&space;=&space;7" title="14 / 2 = 7" />,which is also a prime number.  Therefore, <img src="https://latex.codecogs.com/gif.latex?14&space;=&space;2&space;\bullet&space;7" title="14 = 2 \bullet 7" />

  
