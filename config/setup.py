# Libraries and dependencies
from pymongo import MongoClient
######################## URLS AND CONNECTION CREDENTIALS ###################################


URL_POST0 = "https://www.google-analytics.com/j/collect?v=1&_v=j96&a=832329480&t=pageview&_s=1&dl=https%3A%2F%2Fexplorer.coti.io%2Faddress%2F51dbd2feecb8c9e3b5c88129da88156d738d00d57bf4524cc780221c4e414ffc9372b00ad7d75679032d928776b044d40d5febb783d8ac9b241b7c0b1cad77de9b699c23&dp=Transactions%20by%20address&ul=es-es&de=UTF-8&dt=COTI%20Explorer&sd=24-bit&sr=1080x1920&vp=150x833&je=0&_u=QACAAEABAAAAAC~&jid=1553990046&gjid=1227547208&cid=1036153246.1642087336&tid=UA-108807921-15&_gid=2091742395.1642087336&_r=1&_slc=1&z=1504919713"
URL_POST1 = "https://stats.g.doubleclick.net/j/collect?t=dc&aip=1&_r=3&v=1&_v=j96&tid=UA-108807921-15&cid=1036153246.1642087336&jid=1553990046&gjid=1227547208&_gid=2091742395.1642087336&_u=QACAAEAAAAAAAC~&z=758774129"
URL_GET0 = "https://mainnet-nodemanager.coti.io/wallet/nodes"
URL_GET1 = "https://coti.primenode.io/websocket/info?t=1642091027400"
URL_POST2 = "https://coti.primenode.io/transaction/addressTransactions"

payload_get_1 = {"t": 1642091027400}
payload_post_2 = {"address": "51dbd2feecb8c9e3b5c88129da88156d738d00d57bf4524cc780221c4e414ffc9372b00ad7d75679032d928776b044d40d5febb783d8ac9b241b7c0b1cad77de9b699c23"}
payload_get_0 = {"Access-Control-Allow-Origin": "*",
                 "Cache-Control": "no-cache, no-store, max-age=0, must-revalidate",
                 "Connection": "keep-alive",
                 "Content-Encoding": "gzip",
                 "Content-Type": "application/json;charset=UTF-8",
                 "Date": "Thu, 13 Jan 2022 15:59:19 GMT",
                 "Expires": 0,
                 "Pragma": "no-cache",
                 "Server": "nginx",
                 "Strict-Transport-Security": "max-age=31536000; includeSubdomains; preload",
                 "Transfer-Encoding": "chunked",
                 "Vary": "Accept-Encoding",
                 "Vary": "Origin",
                 "Vary": "Access-Control-Request-Method",
                 "Vary": "Access-Control-Request-Headers",
                 "X-Content-Type-Options": "nosniff",
                 "X-Content-Type-Options": "nosniff",
                 "X-Frame-Options": "DENY",
                 "X-Frame-Options": "SAMEORIGIN",
                 "X-XSS-Protection": "1; mode=block",
                 "X-XSS-Protection": "1; mode=block"

                 }
payload_post_0 = {"v": 1,
                  "_v": "j96",
                  "a": 832329480,
                  "t": "pageview",
                  "_s": 1,
                  "dl": "https%3A%2F%2Fexplorer.coti.io%2Faddress%2F51dbd2feecb8c9e3b5c88129da88156d738d00d57bf4524cc780221c4e414ffc9372b00ad7d75679032d928776b044d40d5febb783d8ac9b241b7c0b1cad77de9b699c23",
                  "dp": "Transactions%20by%20address",
                  "ul": "es-es",
                  "de": "UTF-8",
                  "dt": "COTI%20Explorer",
                  "sd": "24-bit",
                  "sr": "1080x1920",
                  "vp": "150x833",
                  "je": 0,
                  "_u": "QACAAEABAAAAAC~",
                  "jid": 1553990046,
                  "gjid": 1227547208,
                  "cid": "1036153246.1642087336",
                  "tid": "UA-108807921-15",
                  "_gid": "2091742395.1642087336",
                  "_r": 1,
                  "_slc": 1,
                  "z": 1504919713}
payload_post_1 = {"t": "dc",
                  "aip": 1,
                  "_r": 3,
                  "v": 1,
                  "_v": "j96",
                  "tid": "UA-108807921-15",
                  "cid": "1036153246.1642087336",
                  "jid": 1553990046,
                  "gjid": 1227547208,
                  "_gid": "2091742395.1642087336",
                  "_u": "QACAAEAAAAAAAC~",
                  "z": 758774129}

## Create connection to the MongoDB database

mongo_client = "mongodb+srv://admin:1234@cluster0.i1gmk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
cluster = MongoClient(mongo_client)
db = cluster["coti"]
Mdb = db["data"]