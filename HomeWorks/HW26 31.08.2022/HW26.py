import requests
from bs4 import BeautifulSoup

url = 'https://uchet.kz/kursi_valut/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}
response = requests.get(url=url, headers=headers, timeout=10)
print(response.text)
# with open('new.txt', mode='w') as file:
    # file.write(response.text)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('a', href_="/kursi_valut/?filter_currency=RUB")

print(len(quotes))