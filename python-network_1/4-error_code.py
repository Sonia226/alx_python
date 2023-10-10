"""
This module  takes in a URL, 
sends a request to the URL and displays the body of the response.
"""
import requests
import sys


def send_request_and_display_response(url):
    try:
        response = requests.get(url)
        print(f'{response.text}')

        if response.status_code >= 400:
            print(f'Error code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
    else:
        url = sys.argv[1]
        send_request_and_display_response(url)