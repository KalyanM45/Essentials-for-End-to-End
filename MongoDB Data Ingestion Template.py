import pymongo
import pandas as pd

df = pd.read_csv('data.csv')

# Converting the DataFrame to a dictionary
data = df.to_dict(orient='records')

# Configuring connection to MongoDB
client = pymongo.MongoClient('<YOUR_MONGO_URI>')
database = client['<YOUR_DB_NAME>']
collection = database['<YOUR_COLLECTION_NAME>']

# Pushing the data to the MongoDB collection
collection.insert_many(data)

# Retrieving data from MongoDB
records = collection.find()
retreived_data = pd.DataFrame(list(records))
