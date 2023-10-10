"""
This a module that fetches the URL using request package
"""
import request
"""
This is importing the request method
"""
if __name__ == "__main__":
    response = request.get("https://alu-intranet.hbtn.io/status")
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