import requests

url = "https://www.github.com"

try:
    response = requests.get(url)
    response.raise_for_status()
    print(f"{url} is up and running!")

except requests.exceptions.HTTPError as errh:
    print(f"{url} returns HTTP Error: {errh}")

except requests.exceptions.ConnectionError as errc:
    print(f"{url} returns Error Connecting: {errc}")

except requests.exceptions.Timeout as errt:
    print(f"{url} returns Timeout Error: {errt}")

except requests.exceptions.RequestException as err:
    print(f"{url} returns Request error: {err}")
