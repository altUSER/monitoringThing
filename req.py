import requests as r
import time

host = "http://localhost/log"

while True:
    print(r.get(host).text)
    time.sleep(1)
