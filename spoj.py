import math

t = int(raw_input())
start = []
end = []

def check_prime(x):
	flag = True
	if x%2 == 0:
		return False
	for i in range(3,math.sqrt(x),2):
		if x%i==0:
			return False
		
	return True
		
for i in range(t):
	temp = raw_input().split(' ')
	start.append(int(temp[0]))
	end.append(int(temp[1]))
	
for z in range(t):
	for y in xrange(start[z],end[z]+1):
		if check_prime(y):
			print y
			
	print ''