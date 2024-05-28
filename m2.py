from itertools import permutations
from pprint import pprint
import requests

list_characters = 'abcdefghijklmnopqrstuvwxyz'
number_of_characters = 1

switch = [''.join(p) for p in permutations(list_characters, number_of_characters)]
pprint(switch)  # ['ab', 'ac', 'ba', 'bc', 'ca', 'cb']

p = switch

proxies = {
    "http": f"http://150.61.8.70:10080",
    "https": f"http://150.61.8.70:10080",
}

for name in p:
    response = requests.get(f'https://pypi.org/project/{name}/', proxies=proxies)
    if response.status_code != 200:
        print(f"{name} - {response.status_code}")
