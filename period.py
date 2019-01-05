# N is the number you want to factor
N = 14
# a is the number which has no common divisor with N, and you want to power
a = 5

# I just put 21 because I thought I could get the answer from somewhere between 1 and 20
for i in range(1,21):
	if((a ** i)%N == 1):
		print(i)
		break
		
	else:
		continue
	
