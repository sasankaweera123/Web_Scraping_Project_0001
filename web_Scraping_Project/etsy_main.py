from bs4 import BeautifulSoup
import requests
import openpyxl

url = "https://www.etsy.com/listing/1328133422/custom-name-mirror-phone-case?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=iphone&ref=sc_gallery-1-1&pro=1&plkey=b0d11581c0f8bd5f1c53904a8c5a6bf151e8b971%3A1328133422"

source = requests.get(url)
source.raise_for_status()
soup = BeautifulSoup(source.text, 'html.parser')

reviews = soup.find('div', {'id': 'reviews'})

#wt-display-flex-xs
count = reviews.find('div', {'class': 'wt-display-flex-xs'}).find('h2').text
listOfChars = list()

for char in count:
    if char.isdigit():
        listOfChars.append(char)

print(listOfChars)

print(count)

items = reviews.find_all('div',class_="wt-text-body-01")

# for item in items:
#     print(item.find('p').text)

# print(items)