"""
Simple WebService Client, using urllib.request, making 10 requests to the WebService, after a health check.
Author: Wolf Paulus
Contributed: Jordan Wallschlaeger

Added json integration
"""

import urllib.request
import json

server_url = "https://erau07.techcasitaproductions.com/"  # change this to the URL of your WebService
service_url = f"{server_url}/?number="
health_url = f"{server_url}/health"


def get_health() -> bool:
    with urllib.request.urlopen(health_url) as response:
        return response.status == 200


def remote_div7(number: int) -> bool:
    url = f"{service_url}{number}"
    # print(f"Running {number} on the url: {url}")
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0',
        'Accept': 'application/json'})
    with urllib.request.urlopen(req) as response:
        if response.status != 200:
            raise Exception(f"Error {response.status}: {response.error}")
        my_dict = json.loads(response.read().decode('utf-8'))
        if (str(my_dict['result'][3:])) == "is divisible by 7." or (str(my_dict['result'][2:])) == "is divisible by 7.":
            return True
        else:
            return False


if __name__ == "__main__":
    print("Starting")
    if get_health():
        for i in range(0, 50):
            print(f"{i} is divisible by seven: {remote_div7(i)}")
