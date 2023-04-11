from pymongo import MongoClient
import urllib.parse

# Define your MongoDB connection string with properly escaped username and password
username = "robin25tech"
password = "Poojjaat@123"
cluster_url = "cluster0.hwzufsr.mongodb.net"
connection_string = f"mongodb+srv://{urllib.parse.quote_plus(username)}:{urllib.parse.quote_plus(password)}@{cluster_url}/?retryWrites=true&w=majority"

# Create a MongoDB client
client = MongoClient(connection_string)

# Access the desired database and collection
db = client['mydb']
attendees_collection = db['attendees']

query = {"event_id": "55980b2b-4f50-4f11-80a2-4ad62e2ca860", "users.user_id": "e3cd5c37-00a9-46ff-9004-0afac0df9c70"}

# Update the documents matching the query
updated_docs = attendees_collection.update_many(query, {"$set": {"users.$.user_information.isAdmin": False}})

# Print the number of documents updated
print(f"Number of documents updated: {updated_docs.modified_count}")
