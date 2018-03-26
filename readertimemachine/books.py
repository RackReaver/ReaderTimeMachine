import requests

search = 'how to calculate'

r = requests.get('https://www.googleapis.com/books/v1/volumes?q="' + search + '"')
data = r.json()

for book in data['items']:
    print(str(book['volumeInfo']['title']) + '\n')
