from fastapi import FastAPI
from config import setup
from schemas.models import transactionsEntity
import time
import datetime

# Setting of mongo and Fastapi
app = FastAPI()
mongoDB_ = setup.Mdb

#Responses 
@app.get('/{hash}')
async def find_by_hash(hash):
    return transactionsEntity(mongoDB_.find({'hash': hash}))

@app.get('/{day}/{month}/{year}')
async def find_by_date(day,month, year):
    date = datetime.datetime.strptime("{}/{}/{}".format(day, month, year), "%d/%m/%Y")
    date_1 = time.mktime(date.timetuple())
    date_2 = time.mktime((date + datetime.timedelta(days=1)).timetuple())
    print(date_1)
    return transactionsEntity(mongoDB_.find({'createTime': {"$gte": date_1, "$lt": date_2}}))

@app.get('/{day_1}/{month_1}/{year_1}/{day_2}/{month_2}/{year_2}')
async def find_between_date(day_1,month_1, year_1, day_2, month_2, year_2):
    date_1 = datetime.datetime.strptime("{}/{}/{}".format(day_1, month_1, year_1), "%d/%m/%Y")
    date_1 = time.mktime(date_1.timetuple())
    date_2 = datetime.datetime.strptime("{}/{}/{}".format(day_2, month_2, year_2), "%d/%m/%Y")
    date_2 = time.mktime((date_2 + datetime.timedelta(days=1)).timetuple())
    print(date_1)
    return transactionsEntity(mongoDB_.find({'createTime': {"$gte": date_1, "$lt": date_2}}))
