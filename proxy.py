import requests
from bs4 import BeautifulSoup
from random import choice

def get_proxies():
    url = "https://free-proxy-list.net/"
    request = requests.get(url)
    soup = BeautifulSoup(request.content, "html.parser")
    proxies = [ i for i in list(map(lambda x: x[0]+':'+x[1] if x[1].isdigit() and len(x[0])>6  else "", list(zip(map(lambda x: x.text, soup.find_all("td")[::8]), map(lambda x: x.text, soup.find_all("td")[1::8]))))) if i and i[4] != '-' ]
    return {"https://":choice(proxies)}

def proxy_finder():
    proxy = get_proxies()
    while True:
        try:
            r = requests.request("get", "https://example.com", timeout=5, proxies=proxy)
            print(proxy)
            break    
        except:
            pass
    return proxy

def main():
    proxy_finder()

if __name__ == "__main__" :
    main()