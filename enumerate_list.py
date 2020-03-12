#Author: Jesus Leyva
#this is a sample of you would add indices to a list


data = ['alpha', 'beta', 'gamma']

#simple data print
print(data, 'is type', type(data))



#create new varible with indices
data_with_indices = list(
    enumerate(data)
)

#print data with indices
print(data_with_indices, 'is type', type(data_with_indices))


