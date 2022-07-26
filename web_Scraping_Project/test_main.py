import unittest
import main


class TestMain(unittest.TestCase):

    def test_get_number_of_pages(self):
        result = main.get_number_of_pages(main.url_format('https://www.ebay.com/urw/Apple-iPhone-SE-64GB-Space-Grey-Unlocked-A1723-CDMA-GSM-/product-reviews/220288242?_itm=284977072521'))
        self.assertEqual(result, 16)

    def test_get_all_links(self):
        result = main.get_all_links('https://www.ebay.com/urw/Apple-iPhone-SE-64GB-Space-Grey-Unlocked-A1723-CDMA-GSM-/product-reviews/220288242?_itm=284977072521', 16)
        self.assertEqual(len(result), 16)

    def test_create_excel_file(self):
        result = main.create_excel_file()
        self.assertEqual(result[1].title, 'Apple iPhone X')


if __name__ == '__main__':
    unittest.main()
