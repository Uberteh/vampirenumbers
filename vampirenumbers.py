import time

def list_factors(num):
	factors = []
	for i in range(1, num + 1):
		if num % i ==-0:
			factors.append(i)
	return factors
def vampireNum (teeth,fangnumber):
	
	teethrange = range(10**(teeth-1), 10**teeth)
	fangsize = teeth // fangnumber
	print (fangsize)
	print (teethrange)

	return main()

def main ():
	t,f = input("Please enter two digits, the number of teeth, and the number of fangs:").split()
	t = int(t)
	f = int(f)
	print ("Teeth number =",t,". Fang size =",f,".")
	vampireNum (t,f)



	return main()



main()

