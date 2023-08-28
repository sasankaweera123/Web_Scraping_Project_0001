import mysql.connector as mc

database_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'moody'
}


def create_schema():
    conn = mc.connect(**database_config)

    cursor = conn.cursor()

    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS moody")
        print("Database created successfully")
    except mc.Error as err:
        print("Database not created")

    cursor.execute("USE moody")

    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
        id INT AUTO_INCREMENT PRIMARY KEY,
        product_id VARCHAR(255), 
        review_title VARCHAR(255), 
        review_comment VARCHAR(255),
        rating INT
        )
        """)
        print("Table created successfully")
    except mc.Error as err:
        print("Table not created")

    try:
        drop_query = "DROP TABLE IF EXISTS products"
        cursor.execute(drop_query)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
        id INT AUTO_INCREMENT PRIMARY KEY,
        product_id VARCHAR(255), 
        product_name VARCHAR(255), 
        product_link VARCHAR(255)
        )
        """)
        print("Table created successfully")
    except mc.Error as err:
        print("Table not created")

    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS moodyDB (
        id INT AUTO_INCREMENT PRIMARY KEY,
        product_id VARCHAR(255),
        avg_pt VARCHAR(255),
        sentiment_st VARCHAR(255),
        avg_ct VARCHAR(255),
        sentiment_sc VARCHAR(255)
        )
        """)
        print("Table created successfully")
    except mc.Error as err:
        print("Table not created")

    cursor.close()
    conn.close()


def insert_data_products(data):
    try:
        conn = mc.connect(**database_config)

        cursor = conn.cursor()

        insert_query = "INSERT INTO products (product_id, product_name, product_link) VALUES (%s, %s, %s)"

        for entry in data:
            cursor.execute(insert_query, entry)

        conn.commit()
        print("Data inserted successfully")
    except mc.Error as err:
        print("Data not inserted")
    finally:
        if cursor:
            cursor.close()
        if conn.is_connected():
            conn.close()


def main():
    create_schema()

    # insert_data_products
    product_data = [
        ('P0001', 'Apple iPhone XS',
         'https://www.ebay.com/urw/Apple-iPhone-XS-Max-256GB-Space-Gray-Unlocked-A1921-CDMA-GSM-/product-reviews/24023697465?_itm=284963910251'),
        ('P0002', 'Apple iPhone XS',
         'https://www.ebay.com/urw/Apple-iPhone-XS-64GB-Space-Gray-Unlocked-A1920-CDMA-GSM-/product-reviews/25023700375?_itm=274615310667'),
        ('P0003', 'Apple iPhone X',
         'https://www.ebay.com/urw/Apple-iPhone-X-256GB-Space-Gray-Unlocked-A1901-GSM-/product-reviews/239160993?_itm=155158125118'),
        ('P0004', 'Apple iPhone X',
         'https://www.ebay.com/urw/Apple-iPhone-X-256GB-Space-Gray-Unlocked-A1865-CDMA-GSM-/product-reviews/240420150'),
        ('P0005', 'Apple iPhone 8',
         'https://www.ebay.com/urw/Apple-iPhone-8-64GB-Space-Gray-AT-T-A1905-GSM-/product-reviews/239054120?_itm=292922186222'),
        ('P0006', 'Apple iPhone 12',
         'https://www.ebay.com/urw/Apple-iPhone-12-Pro-Max-128GB-Pacific-Blue-Unlocked-/product-reviews/17041715649?_itm=125527552731'),
        ('P0007', 'Apple iPhone SE',
         'https://www.ebay.com/urw/Apple-iPhone-SE-64GB-Space-Grey-Unlocked-A1723-CDMA-GSM-/product-reviews/220288242?_itm=284977072521'),
        ('P0008', 'Apple iPhone 11',
         'https://www.ebay.com/urw/Apple-iPhone-11-64GB-Black-Unlocked-A2221-CDMA-GSM-/product-reviews/22034217345?_itm=165689939104'),
        ('P0009', 'Apple iPhone 8',
         'https://www.ebay.com/urw/Apple-iPhone-8-64GB-Space-Gray-Unlocked-A1905-GSM-/product-reviews/239093015'),
        ('P0010', 'Apple iPhone 11',
         'https://www.ebay.com/urw/Apple-iPhone-11-64GB-Black-Unlocked-A2221-CDMA-GSM-/product-reviews/22034217345?_itm=165689939104'),
        ('P0011', 'Apple iPhone 13 Pro Max',
         'https://www.ebay.com/urw/Apple-iPhone-13-Pro-Max-128GB-Graphite-Unlocked-A2484-CDMA-GSM-/product-reviews/10049287446'),
        ('P0012', 'Apple iPhone 8',
         'https://www.ebay.com/urw/Apple-iPhone-8-64GB-Space-Gray-Unlocked-/product-reviews/15022478164'),
        ('P0013', 'Apple iPhone XR ',
         'https://www.ebay.com/urw/Apple-iPhone-XR-64GB-White-Unlocked-A1984-CDMA-GSM-/product-reviews/6023707176'),
        ('P0014', 'Apple iPhone 12 mini ',
         'https://www.ebay.com/urw/Apple-iPhone-12-mini-64GB-Black-Unlocked-/product-reviews/13041717342'),
        ('P0015', 'Apple iPhone 11',
         'https://www.ebay.com/urw/Apple-iPhone-11-64GB-Black-Unlocked-A2111-CDMA-GSM-/product-reviews/14034212885'),
        ('P0016', 'Apple iPhone 11 Pro',
         'https://www.ebay.com/urw/Apple-iPhone-11-Pro-64GB-Midnight-Green-Unlocked-A2215-CDMA-GSM-/product-reviews/11034210273'),
        ('P0017', 'Apple iPhone 8 Plus ',
         'https://www.ebay.com/urw/Apple-iPhone-8-Plus-64GB-Space-Gray-Unlocked-/product-reviews/16044554351'),
        ('P0018', 'Apple iPhone 11',
         'https://www.ebay.com/urw/Apple-iPhone-11-PRODUCT-RED-64GB-Unlocked-A2111-CDMA-GSM-/product-reviews/22034217304'),
        ('P0019', 'Apple iPhone 11 ',
         'https://www.ebay.com/urw/Apple-iPhone-11-64GB-Black-Unlocked-/product-reviews/17035818063'),
        ('P0020', 'Apple iPhone 12 ',
         'https://www.ebay.com/urw/Apple-iPhone-12-64GB-Green-Unlocked-/product-reviews/5041723844#'),
        ('P0021', 'Apple iPhone 12 mini ',
         'https://www.ebay.com/urw/Apple-iPhone-12-mini-PRODUCT-RED-64GB-Unlocked-/product-reviews/24041710518'),
        ('P0022', 'Apple iPhone 7 Plus',
         'https://www.ebay.com/urw/Apple-iPhone-7-Plus-128GB-Rose-Gold-Unlocked-A1784-GSM-/product-reviews/240464807'),
        ('P0023', 'Apple iPhone 11',
         'https://www.ebay.com/urw/Apple-iPhone-11-64GB-Black-Unlocked-A2111-CDMA-GSM-/product-reviews/18045314698'),
        ('P0024', 'Apple iPhone 12 mini',
         'https://www.ebay.com/urw/Apple-iPhone-12-mini-128GB-White-Unlocked-/product-reviews/5041723597'),
        ('P0025', 'Apple iPhone XS Max',
         'https://www.ebay.com/urw/Apple-iPhone-XS-Max-64GB-Gold-Unlocked-A2101-GSM-/product-reviews/10023710016'),
        ('P0026', 'Apple iPhone 12 mini ',
         'https://www.ebay.com/urw/Apple-iPhone-12-mini-64GB-White-Unlocked-/product-reviews/3041720684'),
        ('P0027', 'Apple iPhone XR',
         'https://www.ebay.com/urw/Apple-iPhone-XR-64GB-Black-Unlocked-A1984-CDMA-GSM-/product-reviews/13023706562'),
        ('P0028', 'Apple iPhone 8 ',
         'https://www.ebay.com/urw/Apple-iPhone-8-64GB-Space-Grey-Unlocked-A1905-GSM-/product-reviews/15053005038'),
        ('P0029', 'Apple iPhone XR',
         'https://www.ebay.com/urw/Apple-iPhone-XR-64GB-White-Unlocked-A2105-GSM-/product-reviews/9023697812'),
        ('P0030', 'Apple iPhone XS Max',
         'https://www.ebay.com/urw/Apple-iPhone-XS-Max-256GB-Gold-Unlocked-A1921-CDMA-GSM-/product-reviews/18023708683')
    ]

    insert_data_products(product_data)


if __name__ == "__main__":
    main()
