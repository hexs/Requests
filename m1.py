from pprint import pprint
import requests
from bs4 import BeautifulSoup


proxy_host = "150.61.8.70"
proxy_port = 10080

proxy_user = "agyc026730"
proxy_pass = "op90-==="

proxy_url = f"http://{proxy_host}:{proxy_port}"

proxies = {
    "http": proxy_url,
    "https": proxy_url
}
proxy_auth = requests.auth.HTTPProxyAuth(proxy_user, proxy_pass)

response = requests.get('https://www.example.com', proxies=proxies, auth=proxy_auth)

print(response)

response = requests.get('https://deadbydaylight.fandom.com/wiki/Perks', proxies=proxies)
print(response.status_code)

soup = BeautifulSoup(response.content, "html.parser")

survivor_perks = soup.select("table:nth-of-type(1) tr th:nth-of-type(2) a")
survivor_perk_names = [perk.text for perk in survivor_perks]

killer_perks = soup.select("table:nth-of-type(2) tr th:nth-of-type(2) a")
killer_perk_names = [perk.text for perk in killer_perks]

print("Survivor Perk Names:")
for name in survivor_perk_names:
    response = requests.get(f'https://pypi.org/project/{name}/', proxies=proxies)
    if response.status_code != 200:
        print(f"{name} - {response.status_code}")

print("Killer Perk Names:")
for name in killer_perk_names:
    response = requests.get(f'https://pypi.org/project/{name}/', proxies=proxies)
    if response.status_code != 200:
        print(f"{name} - {response.status_code}")

# with open('index.html', 'w', encoding='utf8') as f:
#     f.write(response.text)



