#Author: Jesus Leyva
#This returns a list of all factors given a number
#to update: 
	#give user option to indicate the order of the list
	#are these two numbers relatively prime?
	#prime factorization

n = input("Give me a whole number:")
n = int(n)

factors = []
factor_count = 1
for x in range(1,n):
 if n % x == 0:
 	factors.append(x)
 	factor_count += 1
 
factors.append(n)
print(factors)
print("The number", n, "has", factor_count, "factors")

if len(factors) == 2:
	print("BINGO! This is a prime number.")