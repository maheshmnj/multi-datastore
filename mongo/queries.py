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

query = {"event_id":"55980b2b-4f50-4f11-80a2-4ad62e2ca860"}

# Execute the query and retrieve the results
results = attendees_collection.find(query)

# Print the results
for result in results:
    print(result)