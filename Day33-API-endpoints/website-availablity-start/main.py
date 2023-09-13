import time
import urllib3

def uptime_bot(url):
    while True:
        try: 
            conn = urllib3.request("GET",url)
        except urllib3.exceptions.HTTPError as e:
            print(f"HTTPError: {e.code} for {url}")
        except urllib3.exceptions.InsecureRequestWarning as e:
            print(f"Unverified HTTPS Request: {e.code} for {url}")
        else:
            print(f"{url} is up")
        time.sleep(60)

if __name__=="__main__":
    url = "http://www.google.com"
    uptime_bot(url)