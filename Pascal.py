#Author: Jesus Leyva
#This code will print out a copy of Pascal's Triangle

user_input = input("Enter the number of rows in the triangle:")		#User input
N = int(user_input)		#convert data into intigers
N = N * 2		#double the user input as columns are twice as many as rows
data = [0]* (N)

data[N//2] = 1		#set middle indice to 1
print(data) #starting position must include initial zeros, they can be removed later

while data[0] == 0:		#loop will run as long as first element in row_n is equal to 0
	for i in range(N//2):		#iteration on loop to genetate row_n as indicated by user
		data[i] += data[i+1]		#new data[i] is equal to previous + next
	print(str(			#iteration of print of data strings that have proper value per indeci
		list(
			filter(
				lambda x: x!=0, data		#filter leading and trailing zeros
				)
			)
		).center(N*3))		#center string of length N*3


