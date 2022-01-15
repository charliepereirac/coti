# Libraries and dependencies
import json
import requests
from bs4 import BeautifulSoup
from config import setup


# FUNCTIONS
def retrieve_transactions():
    """
    Sends post and get requests to URLs emulating the behaviour of COTI website,
    returns a JSON file with all transactions from the site.
    :return: JSON: JSON file with transaction data.
    """
    requests.post(setup.URL_POST0, json = setup.payload_post_0)
    requests.post(setup.URL_POST1, json = setup.payload_post_1)
    requests.get(setup.URL_GET0, params=setup.payload_get_0)
    requests.get(setup.URL_GET1, params=setup.payload_get_1)
    r2p = requests.post(setup.URL_POST2, json = setup.payload_post_2)
    soup2p=BeautifulSoup(r2p.content, 'html.parser')
    result = soup2p.text
    result = json.loads(result)
    transactions = result["transactionsData"]
    return transactions
transactions = retrieve_transactions()
print(transactions[0])

def store_data_MDB(Mdb, transactions):
    """
    Inserts data into a MongoDB collection.
    :param data: pymongo.collection.Collection: collection where the data must be inserted.
    :param transactions: JSON: JSON file to be inserted in collections.
    :return:
    """
    Mdb.delete_many({})
    Mdb.insert_many(transactions)

