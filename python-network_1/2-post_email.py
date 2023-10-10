"""
This module sends a request to the URL 
and displays the value of the variable X-Request-Id
"""
import requests
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    r = requests.get(url)
    r1 = r.headers.get("X-Request-Id", None)
    print(r1)