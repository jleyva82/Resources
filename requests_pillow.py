'''
Author: Jesus Leyva
Date of Last Update: 02/05/2019
Purpose:
    scrape an image of a web address using Pillow library
'''


import requests
from io import BytesIO
from PIL import Image

r1 = requests.get("https://tse1.mm.bing.net/th?id=OIP.E-PlB-NSNtR1MIIZMgzpzwHaEK&pid=Api")   #request info of given html code
r2 = requests.get("https://images6.alphacoders.com/697/thumb-1920-697050.png")

image1 = Image.open(BytesIO(r1.content))                                                     #uses image function from Pillow library to save image as python variable
image2 = Image.open(BytesIO(r2.content))

print("IMAGE ONE DETAILS")                                                                   #details for first image
print("URL:", r1.url)
print("Status Code:", r1.status_code)
print(image1.size, image1.format, image1.mode)                                                #outputs, size, format and file type

path = "./image1." + image1.format                                                           #name of new file

try:
    image1.save(path, image1.format)
except IOError:
    print("Cannot save image.")

print("\nIMAGE TWO DETAILS")
print("URL:", r2.url)
print("Status Code:", r2.status_code)
print(image2.size, image2.format, image2.mode)

path = "./image2." + image2.format
try:
    image2.save(path, image2.format)
except IOError:
    print("Cannot save image.")