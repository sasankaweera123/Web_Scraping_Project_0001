from main import *


def test_get_number_of_pages():
    soup = url_format('https://www.ebay.com/urw/Apple-iPhone-XS-Max-256GB-Space-Gray-Unlocked-A1921-CDMA-GSM-/product-reviews/24023697465?_itm=284963910251')
    assert get_number_of_pages(soup) == 12


def test_get_review_data():
    # Create a sample BeautifulSoup section for testing
    section = BeautifulSoup(
        "<div class='review-item-title'>Title</div><p class='review-item-content'>Comment</p>", 'html.parser')
    review_title, review_comment = get_review_data(section)
    assert review_title == ""
    assert review_comment == ""

