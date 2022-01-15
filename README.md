# COTI API 

This objective of this project is to retrieve data from COTI's website, store it and then make it available for queries trough an API.

The project was divided in 2 main parts: the scraper and the API. 
- For the scarper several libraries have been used, however the two most important ones where [BeautifulSoup](https://pypi.org/project/bs4/) and requests. 
Since COTI’s website was JavaScript rendered and the project required not only data from the Front-End but also data not available there, POST and GET protocols of the website have been emulated applying reverse engineering to get the expected response. 
The data was then stored in a MongoDB repository by using [pymongo](https://docs.mongodb.com/drivers/pymongo/) driver. 

- For the API, [FastAPI](https://fastapi.tiangolo.com) was used for its development. 
Further information on how to run the project can be found below. 

## GENERAL INSTRUNCTIONS

The project contains 2 main files: 
-	scraper.py
-	API.py

The transactions’ information was already uploaded to MongoDB and is ready to be used trough the API. However, if you want to reload the information just uncomment the last line in the scarper.py file. 

To use the api please proceed as follows:

