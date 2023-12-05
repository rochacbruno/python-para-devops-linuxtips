import os

def get_api_key():
    api_key = os.getenv("API_KEY")

    if api_key is None:
        raise RuntimeError("Oops! Looks like API_KEY is missing!")
    return api_key


key = get_api_key()

print(key)