from bs4 import BeautifulSoup
import requests

try:
    # get the source url
    source = requests.get('https://www.ebay.com/urw/Apple-iPhone-XS-64GB-Space-Gray-Unlocked-A1920-CDMA-GSM-/product-reviews/25023700375?_itm=274615310667')
    # validation about the url
    source.raise_for_status()
    # website url format using parser
    soup = BeautifulSoup(source.text,'html.parser')
    # print(soup)
    title = soup.find('div', class_="reviews").find_all('div',class_='ebay-review-section')
    # print(len(title))

    for t in title:
        review_section_left =t.find('div', class_='ebay-review-section-l')
        review_section_right = t.find('div', class_='ebay-review-section-r')
        review_title = review_section_right.find('h3',class_='review-item-title').text
        review_comment = review_section_right.find('p',class_='review-item-content').text
        # need to Update helpful correctly
        helpful = review_section_right.find('div', class_='review-btns')

        print(review_section_left)
        break

except Exception as e:
    print(e)
