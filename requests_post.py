'''
Author = Jesus Leyva
Last Update: 02/05/2019
Purpose:
    Uses request to post information 
'''
import requests

my_data = {"Name": "Jesus", "Email": "jesus@example.co"}                                #data to be posted
            #for Name category post 'Jesus'
            #for Email category post 'jesus@example.com'
r = requests.post("http://www.w3schools.com/php/welcome.php", data=my_data)            #post to given adress

f = open("myfile.html", "w+")
f.write(r.text)
