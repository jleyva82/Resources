'''
Author: Jesus Leyva
Date of Last Update: 01/31/2018
Purpose:
    Introduction to request library
    Exposure to HTML codes
    creation of HTML text file off an existing web address
'''
import requests                                  #import requests library


params = {"q": "pizza"}
r = requests.get("http://www.bing.com/search", params=params)            #scrapes the information of google.com as a python value
print("Web Address:", r.url)
print("Status:", r.status_code)                  #print the sites status code
                                                 #should be code: 200, meaning all is well
#print(r.text)

f = open("./page.html", "w+")                    #creates page.html file in writable mode as python varianble
f.write(r.text)                                  #in new file write the text data collected of google.com

