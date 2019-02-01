'''
Author: Jesus Leyva
Date of Last Update: 01/31/2018
Purpose:
    Introduction to request library
    Exposure to HTML codes
    creation of HTML text file off an existing web address
'''
import requests                                                         #import requests library


params = {"q": "pizza"}                                                 #our example quiery will be for pizza
r = requests.get("http://www.bing.com/search", params=params)           #scrapes the information of bing.com, search pizza, as a python value
print("Web Address:", r.url)                                            #show the webaddress that was scrapped
print("Status:", r.status_code)                                         #print the sites status code
                                                                        #should be code: 200, meaning all is well

f = open("./page.html", "w+")                                           #creates page.html file in writable mode as python varianble
f.write(r.text)                                                         #in new file write the text data collected of google.com

