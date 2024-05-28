import itertools
from itertools import permutations
from pprint import pprint
import requests

list_characters = 'abcdefghijklmnopqrstuvwxyz'
number_of_characters = 3

# switch = [''.join(p) for p in permutations(list_characters, number_of_characters)]
switch = [''.join(combo) for combo in itertools.product(list_characters, repeat=number_of_characters)]

proxies = {
    "http": f"http://150.61.8.70:10080",
    "https": f"http://150.61.8.70:10080",
}

for name in switch:
    response = requests.get(f'https://pypi.org/project/{name}/', proxies=proxies)
    if response.status_code != 200:
        print(f"{name} - {response.status_code}")
        with open('name.txt', 'a') as f:
            f.write(f'{name} - {response.status_code}\n')
    else:
        print(f"{name}")
