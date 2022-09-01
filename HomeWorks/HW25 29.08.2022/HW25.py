import requests  # - библиотека для формирования HTTP - запроса

url = 'https://jsonplaceholder.typicode.com/photos'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}
response = requests.get(url=url, headers=headers, timeout=10)
# print(response.json()[0])
# print(type(response.json()[0]))
with open('new.txt', mode='w') as file:
    file.write(response.text)

index = 0
for element in response.json():
    response_pic = requests.get(url=element['url'], headers=headers, timeout=10)
    # print(response_pic.text)
    with open(f'tmp/pic_{index}.jpg', mode='wb') as file:
        file.write(response.content)
    index += 1
