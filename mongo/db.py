from pymongo import MongoClient
import urllib.parse

# Define your MongoDB connection string with properly escaped username and password
username = "robin25tech"
password = "Poojjaat@123"
cluster_url = "cluster0.hwzufsr.mongodb.net"
connection_string = f"mongodb+srv://{urllib.parse.quote_plus(username)}:{urllib.parse.quote_plus(password)}@{cluster_url}/?retryWrites=true&w=majority"


# client = pymongo.MongoClient("mongodb+srv://robin25tech:<password>@cluster0.al3xown.mongodb.net/?retryWrites=true&w=majority")
# db = client.test

# client = pymongo.MongoClient("mongodb+srv://robin25tech:<password>@cluster0.i2xyuvx.mongodb.net/?retryWrites=true&w=majority")
# db = client.test


# Create a MongoDB client
client = MongoClient(connection_string)

# Access the desired database and create collections with validators
db = client['mydb']

# Define validation schemas for collections
attendees_validator = {
    '$jsonSchema': {
        'bsonType': 'object',
        'required': ['id', 'event_id', 'users'],
        'properties': {
            'id': {'bsonType': 'string'},
            'event_id': {'bsonType': 'string'},
            'users': {
                'bsonType': 'array',
                'items': {
                    'bsonType': 'object',
                    'required': ['user_id', 'user_information'],
                    'properties': {
                        'user_id': {'bsonType': 'string'},
                        'user_information': {
                            'bsonType': 'object',
                            'required': ['username', 'email','avatar_url', 'isAdmin'], # Update with the actual user information fields
                            'properties': {
                                'username': {'bsonType': 'string'},
                                'email': {'bsonType': 'string'},
                                'avatar_url': {'bsonType': 'string'},
                                'isAdmin': {'bsonType': 'bool'},
                            }
                        }
                    }
                }
            }
        }
    }
}

# Define validation schemas for collections
leaderboard_validator = {
    '$jsonSchema': {
        'bsonType': 'object',
        'required': ['user_id', 'score', 'userinformation'],
        'properties': {
            'user_id': {'bsonType': 'string'},
            'score': {'bsonType': 'int'},
            'userinformation': {
                'bsonType': 'object',
                'required': ['username', 'email','avatar_url', 'isAdmin'], # Update with the actual user information fields
                'properties': {
                    'username': {'bsonType': 'string'},
                    'email': {'bsonType': 'string'},
                    'avatar_url': {'bsonType': 'string'},
                    'isAdmin': {'bsonType': 'bool'},
                }
            }
        }
    }
}

feedback_validator = {
    '$jsonSchema': {
        'bsonType': 'object',
        'required': ['user_id', 'event_id', 'feedback_text'],
        'properties': {
            'user_id': {'bsonType': 'string'},
            'event_id': {'bsonType': 'string'},
            'feedback_text': {'bsonType': 'string'}
        }
    }
}


# Create collections with validators
db.create_collection('leaderboard', validator=leaderboard_validator)
db.create_collection('feedback', validator=feedback_validator)

# Create collections with validators
db.create_collection('attendees', validator=attendees_validator)

print("Collections created successfully.")


# db.feedback.insertMany([
#   { event_id: '55980b2b-4f50-4f11-80a2-4ad62e2ca860', user_id: 'e3cd5c37-00a9-46ff-9004-0afac0df9c70', rating: 5, comment: 'Great event!' },
#   { event_id: 'ccacfe1e-398a-42cb-bccc-fd3a5f8ef293', user_id: 'c52b33a3-4fbb-4a72-b64c-8bd6563810ae', rating: 3, comment: 'Could be better' },
#   { event_id: '2d8c4bf8-ff8a-4cb9-b60a-b514c4df6ee4', user_id: '2e0cee35-2ffe-4624-a043-c19cecd0b472', rating: 4, comment: 'Interesting topic' }
# ]);
