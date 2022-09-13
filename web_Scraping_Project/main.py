from bs4 import BeautifulSoup
import requests, openpyxl

excel = openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel.active
sheet.title = 'Apple iPhone X'
print(excel.sheetnames)
sheet.append(['Id', 'Review_Title', 'Review_Comment', 'Rating'])

urlLink = 'https://www.ebay.com/urw/Apple-iPhone-8-64GB-Space-Gray-AT-T-A1905-GSM-/product-reviews/239054120?_itm=292922186222'

try:
    # get the source url
    source = requests.get(urlLink)
    # validation about the url
    source.raise_for_status()
    # website url format using parser
    soup = BeautifulSoup(source.text, 'html.parser')
    # print(soup)
    # Review count
    findCount = soup.find('div', id='reviewContentSection').find('div', id='reviewsSection')
    count = findCount.find('div', class_='review-section-header').h2.text
    count = [int(s) for s in count.split() if s.isdigit()]

    print(int(count[0]))

    pages = int(int(count[0]) / 10) + 1 if int(count[0]) % 10 != 0 else int(int(count[0]) / 10)
    print(pages)

    sourceLink = [urlLink]
    for i in range(pages - 1):
        link = urlLink+'&pgn=' + str(
            i + 2)
        sourceLink.append(link)

    print(sourceLink)
    idNum = 0
    for s in sourceLink:
        source = requests.get(s)
        source.raise_for_status()
        soup = BeautifulSoup(source.text, 'html.parser')
        title = soup.find('div', class_="reviews").find_all('div', class_='ebay-review-section')

        for t in title:
            review_section_left = t.find('div', class_='ebay-review-section-l')
            review_section_right = t.find('div', class_='ebay-review-section-r')
            try:
                review_title = review_section_right.find('h3', class_='review-item-title').text
                review_comment = review_section_right.find('p', class_='review-item-content').text
            except:
                review_title = ''
                review_comment = ''

            rating = int(review_section_left.find('div', class_='ebay-star-rating').meta['content'])

            # print(review_title,review_comment,rating)
            idNum = idNum + 1
            sheet.append([idNum, review_title, review_comment, rating])


except Exception as e:
    print(e)

excel.save('ebayReviewiphonex.xlsx')
