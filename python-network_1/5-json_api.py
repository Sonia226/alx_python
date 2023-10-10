"""
This module takes in a letter and 
sends a POST request to http://0.0.0.0:5000/search_user 
with the letter as a parameter
"""

import requests
import sys


def search_user_by_letter(letter):
    try:
        url = 'http://0.0.0.0:5000/search_user'
        data = {'q': letter}
        response = requests.post(url, data=data)

        if response.status_code == 200:
            try:
                user_data = response.json()
                if user_data:
                    user_id = user_data.get('id')
                    user_name = user_data.get('name')
                    print(f'[{user_id}] {user_name}')
                else:
                    print('No result')
            except ValueError:
                print('Not a valid JSON')
        else:
            print('No result')
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')


if __name__ == "__main__":
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""

    search_user_by_letter(letter)