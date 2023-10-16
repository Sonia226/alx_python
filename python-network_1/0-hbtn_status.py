"""This a Module that fetches the URL using requests package"""
import requests
"""
This imports the requests method
"""
if __name__ == "__main__":
    response = requests.get("https://alu-intranet.hbtn.io/status")
    """
    saves the requests in a variable
    """
    print("Body response:")
    """
    prints body response
    """
    print("\t- type:", type(response.text))
    """
    prints type of response text
    """
    print("\t- content:", response.text)
    """
    prints content of response text
    """