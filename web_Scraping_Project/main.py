from bs4 import BeautifulSoup
import requests
import openpyxl

excel = openpyxl.Workbook()
sheet = excel.active


def create_excel_file():
    print(excel.sheetnames)
    sheet.title = 'Apple iPhone X'
    print(excel.sheetnames)
    sheet.append(['Id', 'Review_Title', 'Review_Comment', 'Rating'])


def add_excel_file_data(data):
    sheet.append(data)


def save_excel_file(name):
    excel.save(name)


def get_number_of_pages(soup):
    # Review count
    find_count = soup.find('div', id='reviewContentSection').find('div', id='reviewsSection')
    count = find_count.find('div', class_='review-section-header').h2.text
    count = [int(s) for s in count.split() if s.isdigit()]

    print(int(count[0]))

    pages = int(int(count[0]) / 10) + 1 if int(count[0]) % 10 != 0 else int(int(count[0]) / 10)
    print(pages)
    return pages


def get_all_links(link, pages):
    source_link = [link]
    for i in range(pages - 1):
        links = link + '?pgn=' + str(
            i + 2)
        source_link.append(links)

    print(source_link)
    return source_link


def url_format(url):
    # get the source url
    source = requests.get(url)
    # validation about the url
    source.raise_for_status()
    # website url format using parser
    soup = BeautifulSoup(source.text, 'html.parser')

    return soup


def get_review_data(section):
    try:
        review_title = section.find('h3', class_='review-item-title').text
        review_comment = section.find('p', class_='review-item-content').text
    # put the value error here if error occur remove value error
    except ValueError:
        review_title = ''
        review_comment = ''

    return review_title, review_comment


def get_data(url):
    # print(soup)
    number_of_pages = get_number_of_pages(url_format(url))
    all_links = get_all_links(url, number_of_pages)
    id_num = 0
    for s in all_links:
        soup = url_format(s)
        title = soup.find('div', class_="reviews").find_all('div', class_='ebay-review-section')

        for t in title:
            review_section_left = t.find('div', class_='ebay-review-section-l')
            review_section_right = t.find('div', class_='ebay-review-section-r')
            review_title, review_comment = get_review_data(review_section_right)

            rating = int(review_section_left.find('div', class_='ebay-star-rating').meta['content'])

            # print(review_title,review_comment,rating)
            id_num = id_num + 1
            add_excel_file_data([id_num, review_title, review_comment, rating])


def main():
    create_excel_file()
    website = 'https://www.ebay.com/'
    item_code = '220288242?_itm=284977072521'
    url = website+'urw/Apple-iPhone-SE-64GB-Space-Grey-Unlocked-A1723-CDMA-GSM-/product-reviews/'+item_code
    try:
        get_data(url)
    except Exception as e:
        print(e)
    save_excel_file('Apple iPhone X.xlsx')


if __name__ == '__main__':
    main()
