import requests as r
import time

host = "http://localhost/log"

while True:
    try:
        print(r.get(host).text, t=1)
    except:
        print("Error")
    time.sleep(1)
