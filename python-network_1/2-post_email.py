"""
This module takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter
"""
import requests
import sys


def send_post_request(url, email):
    try:
        data = {'email': email}
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print(response.text)
        else:
            print(f'Request failed with status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
    else:
        url = sys.argv[1]
        email = sys.argv[2]
        send_post_request(url, email)