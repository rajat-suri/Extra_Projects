#.....Automated tool who's Go on to location & Automatic Download Images and Store it in the directory of linux system......#

import requests,random

url = "https://pastebin.com/raw/01yJu4gY"

#h={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'}

data=requests.get(url, timeout=10)
d = data.text.split("\r\n")
for i in d :
    #image=d.readlines()
    image=requests.get(i)
    num = str(random.randint(1,100))
    #print(image.content)
    f=open("image"+num+".png","wb")
    f.write(image.content)
    f.close()
