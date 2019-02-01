'''
Author = Jesus Leyva
Last Update: 01/28/2019
Purpose: Sample of how to use python to create a new file
sample resources as described via stack skills python lessons

'''
newfile = open("newfile.txt", "w+")                 #newfile variable is like a class.
                                                    # "open()" function.
                                                    #"newfile.txt" is the name of the file
                                                    #"w+" is the note, that we will write on this file

string = "This is the content that will be written to the text file."   #create a variable and pass it to the file

newfile.write(string)                               #use ".write()" function to pass on text into the file
