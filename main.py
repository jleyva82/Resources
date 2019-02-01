'''
Author = Jesus Leyva
Last Update: 01/28/2019
Purpose: uses json (JavaScript Object Notation)
library of tools to in real time change the contents of the file
'''
import json                                                                  #imports simplejson as json
import os                                                                    #imports os tools needed to look up file


#Suppose file exists
if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:   #if "ages.json" file exist and it is not empty
    old_file = open("./ages.json", "r+")                                    #open the file in "r+" (read) mode
    data = json.loads(old_file.read())                                      #assing data as a python object off the old file
    print("Current age is", data["age"], "--adding a year.")                #print current data
    data["age"] = data["age"] + 1                                           #increase age by 1
    print("New age is", data["age"])                                        #UI, let user know of age increase

#File does not exists
else:
    old_file = open("./ages.json", "w+")                                    #create file "ages.json in "w+" (write) mode
    data = {"name": "Nick",                                                 #create data object "name" and "age"
            "age": 27}
    print("No file found, setting default age to", data["age"])

old_file.seek(0)
old_file.write(json.dumps(data))   #writes data unto the empty file
