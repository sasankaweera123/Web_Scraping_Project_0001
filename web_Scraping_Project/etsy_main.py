from bs4 import BeautifulSoup
import requests
import openpyxl


def URL_format(url):
    # get the source url
    source = requests.get(url)
    # validation about the url
    source.raise_for_status()
    # website url format using parser
    soup = BeautifulSoup(source.text, 'html.parser')

    return soup


def get_the_number_of_reviews(reviews):

    #wt-display-flex-xs
    count = reviews.find('div', {'class': 'wt-display-flex-xs'}).find('h2').text
    listOfChars = list()

    for char in count:
        if char.isdigit():
            listOfChars.append(char)

    number_reviews=""
    for i in range(len(listOfChars)):
        number_reviews += listOfChars[i]

    print(int(number_reviews))

    return int(number_reviews)

def get_reviews(reviews):
    items = reviews.find_all('div',class_="wt-text-body-01")
    reviews_list = list()
    for item in items:
        review = item.find('p').text
        review = review.replace('\n', '')
        review=review.lstrip()
        review = review.rstrip()
        reviews_list.append(review)

    print(reviews_list)
    return reviews_list


if __name__ == "__main__":
    url = "https://www.etsy.com/listing/1328133422/custom-name-mirror-phone-case?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=iphone&ref=sc_gallery-1-1&pro=1&plkey=b0d11581c0f8bd5f1c53904a8c5a6bf151e8b971%3A1328133422"
    reviews = URL_format(url).find('div', {'id': 'reviews'})
    get_the_number_of_reviews(reviews)
    get_reviews(reviews)