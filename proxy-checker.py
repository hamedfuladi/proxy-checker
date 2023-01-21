import requests
from bs4 import BeautifulSoup
import pandas as pd

# Get the base URL
base_url = input("Enter the base URL: ")

def test_url_with_proxy(url, proxy):
    """
    Function to test the given url with a proxy
    :param url: The URL to test
    :param proxy: The proxy to use for the connection
    :return: True if the connection is successful, False otherwise
    """
    proxies = {"http": proxy, "https": proxy}
    try:
        response = requests.get(url, proxies=proxies, timeout=5)
        if response.status_code == 200:
            return True
    except:
        pass
    return False

with open("proxies.txt", "r") as f:
    proxies_string = f.read()

proxies_list = proxies_string.splitlines()
url = base_url
for proxy in proxies_list:
    if test_url_with_proxy(url, proxy):
        print(f"Successful connection using proxy: {proxy}")
        proxy_url=proxy
        break
else:
    print("Failed to connect using any of the proxies.")
