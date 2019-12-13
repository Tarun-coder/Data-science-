# We can transfer data from one file to other file and execute it by using multi 
# threading

import shutil
import time
import requests
from threading import Thread

def download_file(url,imagename):
    print(imagename +  "Start Downloading"  +  time.ctime(time.time()))

    file = requests.get(url,stream=True)

    with open(imagename,"wb") as new_file:
        shutil.copyfileobj(file.raw,new_file)
    del file


    print(imagename +  "Finished Downloading" +   time.ctime(time.time()))

url1="https://vignette.wikia.nocookie.net/deathbattlefanon/images/b/b7/Epic_Iron_Man.png/revision/latest?cb=20150404070629"
url2="https://vignette.wikia.nocookie.net/marvelcinematicuniverse/images/c/c0/AoU_Iron_Man_01.png/revision/latest?cb=20150309164237"
url3="https://clipart.info/images/ccovers/1516940925ironman-png-33.png"

#t1=Thread(target=download_file,args=(url1,"ironman1.png"))
#t1.start()
#t2=Thread(target=download_file,args=(url2,"ironman2.png"))
#t2.start()
#t3=Thread(target=download_file,args=(url3,"ironman3.png"))
#t3.start()

download_file(url1,"ironman1.png")

download_file(url2,"ironman2.png")

download_file(url3,"ironman3.png")





