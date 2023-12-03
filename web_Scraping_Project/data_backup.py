import mysql.connector as mc
import pymongo
import os
from tqdm import tqdm

sql_database_config = {
    'host': 'localhost',
    'user': os.environ.get('SQL_USERNAME'),
    'password': os.environ.get('SQL_PASSWORD'),
    'database': 'moody'
}

mongo_database_config = {
    'host': 'localhost',
    'port': 27017,
    'username': os.environ.get('MONGO__USERNAME'),
    'password': os.environ.get('MONGO__PASSWORD'),
}

def get_review_data_from_sql():
    conn = mc.connect(**sql_database_config)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM reviews")

    data = cursor.fetchall()

    return data

def get_product_data_from_sql():
    conn = mc.connect(**sql_database_config)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")

    data = cursor.fetchall()

    return data

def get_product_polarity_from_sql():
    conn = mc.connect(**sql_database_config)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM moodydb")

    data = cursor.fetchall()

    return data

def delete_collection():
    client = pymongo.MongoClient(**mongo_database_config)
    db = client.moody

    review_collections = db.reviews
    product_collections = db.products
    polarity_collections = db.productsPolarity
    review_collections.delete_many({})
    product_collections.delete_many({})
    polarity_collections.delete_many({})


def insert_review_data_mongodb(data):
    client = pymongo.MongoClient(**mongo_database_config)
    db = client.moody

    collections = db.reviews
    for i in tqdm(data):
        collections.insert_one({
            'id': i[0],
            'product_id': i[1],
            'review_title': i[2],
            'review_comment': i[3],
            'rating': i[4]
        })

def insert_products_data_mongodb(data):
    client = pymongo.MongoClient(**mongo_database_config)
    db = client.moody

    collections = db.products
    for i in tqdm(data):
        collections.insert_one({
            'id': i[0],
            'product_id': i[1],
            'product_name': i[2],
            'product_image': i[3]
        })

def insert_product_polarity_mongodb(data):
    client = pymongo.MongoClient(**mongo_database_config)
    db = client.moody

    collections = db.productsPolarity
    for i in tqdm(data):
        collections.insert_one({
            'id': i[0],
            'product_id': i[1],
            'avg_ct': i[2],
            'avg_pt': i[3],
            'sentiment_st': i[4],
            'sentiment_sc': i[5]
        })


def main():
    delete_collection()
    insert_review_data_mongodb(get_review_data_from_sql())
    insert_products_data_mongodb(get_product_data_from_sql())
    insert_product_polarity_mongodb(get_product_polarity_from_sql())


if __name__ == '__main__':
    main()