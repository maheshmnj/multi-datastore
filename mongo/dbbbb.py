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
# leaderboard_collection = db['leaderboard']
feedback_collection = db['feedback']

# Define sample data for attendees
# attendee1 = {
#     'id': '1',
#     'event_id': '55980b2b-4f50-4f11-80a2-4ad62e2ca860',
#     'users': [
#         {
#             'user_id': 'e3cd5c37-00a9-46ff-9004-0afac0df9c70',
#             'user_information': {
#                 'username': 'diane parker',
#                 'email': 'dianeparker@example.com',
#                 'avatar_url': 'https://i.pravatar.cc/150?img=16',
#                 'isAdmin': True
#             }
#         },
#         {
#             'user_id': 'db6f8bb4-474d-4301-9bc9-1845b6758f45',
#             'user_information': {
#                 'username': 'brianharris',
#                 'email': 'brianharris@example.com',
#                 'avatar_url': 'http://example.com/avatar7.jpg',
#                 'isAdmin': False

#             }
#         }
#     ]
# }

# attendee2 = {
#     'id': '2',
#     'event_id': 'ccacfe1e-398a-42cb-bccc-fd3a5f8ef293',
#     'users': [
#         {
#             'user_id': 'c52b33a3-4fbb-4a72-b64c-8bd6563810ae',
#             'user_information': {
#                 'username': 'kellygreen',
#                 'email': 'kellygreen@example.com',
#                 'avatar_url': 'https://i.pravatar.cc/150?img=18',
#                 'isAdmin': False
#             }
#         },
#         {
#             'user_id': '9cb9323a-7235-499c-996a-8a989558d292',
#             'user_information': {
#                 'username': 'emilytaylor',
#                 'email': 'emilytaylor@example.com',
#                 'avatar_url': 'http://example.com/avatar10.jpg',
#                 'isAdmin': False
#             }
            
#         }
#     ]
# }

attendee3 = {
    'id': '3',
    'event_id': '2d8c4bf8-ff8a-4cb9-b60a-b514c4df6ee4',
    'users': [
        {
            'user_id': '2e0cee35-2ffe-4624-a043-c19cecd0b472',
            'user_information': {
                'username': 'williamturner',
                'email': 'williamturner@example.com',
                'avatar_url': 'https://i.pravatar.cc/150?img=19',
                'isAdmin': False
            }
        },
        {
            'user_id': '8c6b30f8-ac41-4ad0-be1b-3da9e36eb3cb',
            'user_information': {
                'username': 'davidsanchez',
                'email': 'davidsanchez@example.com',
                'avatar_url': 'http://example.com/avatar3.jpg',
                'isAdmin': False
            }
        }
    ]
}


# leaderboard_data = [
#     {
#         'user_id': 'e3cd5c37-00a9-46ff-9004-0afac0df9c70',
#         'score': 100,
#         'user_information': {
#                 'username': 'diane parker',
#                 'email': 'dianeparker@example.com',
#                 'avatar_url': 'https://i.pravatar.cc/150?img=16',
#                 'isAdmin': True
#             }
#     },
#     {
#         'user_id': 'db6f8bb4-474d-4301-9bc9-1845b6758f45',
#         'score': 1600,
#         'user_information': {
#                 'username': 'brianharris',
#                 'email': 'brianharris@example.com',
#                 'avatar_url': 'http://example.com/avatar7.jpg',
#                 'isAdmin': False
#             }
#     },
#     {
#         'user_id': 'ccacfe1e-398a-42cb-bccc-fd3a5f8ef293',
#         'score': 900,
#         'user_information': {
#                 'username': 'kellygreen',
#                 'email': 'kellygreen@example.com',
#                 'avatar_url': 'https://i.pravatar.cc/150?img=18',
#                 'isAdmin': False
#             }
#     },

#     {
#         'user_id': '9cb9323a-7235-499c-996a-8a989558d292',
#         'score': 575,
#         'user_information': {
#                 'username': 'emilytaylor',
#                 'email': 'emilytaylor@example.com',
#                 'avatar_url': 'http://example.com/avatar10.jpg',
#                 'isAdmin': False
#             }
#     },
#     {
#         'user_id': '2e0cee35-2ffe-4624-a043-c19cecd0b472',
#         'score': 595,
#         'user_information': {
#                 'username': 'williamturner',
#                 'email': 'williamturner@example.com',
#                 'avatar_url': 'https://i.pravatar.cc/150?img=19',
#                 'isAdmin': False
#             }
#     },
#     {
#         'user_id': '8c6b30f8-ac41-4ad0-be1b-3da9e36eb3cb',
#         'score': 1955,
#         'user_information': {
#                 'username': 'davidsanchez',
#                 'email': 'davidsanchez@example.com',
#                 'avatar_url': 'http://example.com/avatar3.jpg',
#                 'isAdmin': False
#             }
#     },
    
#     # Add more user data as needed
# ]


# leaderboard_data = [
#     {
#         'user_id': 'e3cd5c37-00a9-46ff-9004-0afac0df9c70',
#         'score': 100,
#         'userinformation': {
#                 'username': 'diane parker',
#                 'email': 'dianeparker@example.com',
#                 'avatar_url': 'https://i.pravatar.cc/150?img=16',
#                 'isAdmin': True
#             }
#     },
#     {
#         'user_id': 'db6f8bb4-474d-4301-9bc9-1845b6758f45',
#         'score': 1600,
#         'userinformation': {
#                 'username': 'brianharris',
#                 'email': 'brianharris@example.com',
#                 'avatar_url': 'http://example.com/avatar7.jpg',
#                 'isAdmin': False
#             }
#     },
#     {
#         'user_id': 'ccacfe1e-398a-42cb-bccc-fd3a5f8ef293',
#         'score': 900,
#         'userinformation': {
#                 'username': 'kellygreen',
#                 'email': 'kellygreen@example.com',
#                 'avatar_url': 'https://i.pravatar.cc/150?img=18',
#                 'isAdmin': False
#             }
#     },
#     {
#         'user_id': 'db6f8bb4-474d-4301-9bc9-1845b6758f45',
#         'score': 1600,
#         'userinformation': {
#                 'username': 'brianharris',
#                 'email': 'brianharris@example.com',
#                 'avatar_url': 'http://example.com/avatar7.jpg',
#                 'isAdmin': False
#             }
#     },  
#     {
#         'user_id': '9cb9323a-7235-499c-996a-8a989558d292',
#         'score': 575,
#         'userinformation': {
#                 'username': 'emilytaylor',
#                 'email': 'emilytaylor@example.com',
#                 'avatar_url': 'http://example.com/avatar10.jpg',
#                 'isAdmin': False
#             }
#     },
#     {
#         'user_id': '2e0cee35-2ffe-4624-a043-c19cecd0b472',
#         'score': 595,
#         'userinformation': {
#                 'username': 'williamturner',
#                 'email': 'williamturner@example.com',
#                 'avatar_url': 'https://i.pravatar.cc/150?img=19',
#                 'isAdmin': False
#             }
#     },
#     {
#         'user_id': '8c6b30f8-ac41-4ad0-be1b-3da9e36eb3cb',
#         'score': 1955,
#         'userinformation': {
#                 'username': 'davidsanchez',
#                 'email': 'davidsanchez@example.com',
#                 'avatar_url': 'http://example.com/avatar3.jpg',
#                 'isAdmin': False
#             }
#     },
# ]





data = [
    {'user_id': 'e3cd5c37-00a9-46ff-9004-0afac0df9c70','event_id': '55980b2b-4f50-4f11-80a2-4ad62e2ca860',  'feedback_text': 'The event was well-organized and the speakers were informative. Great job!'},
    {'user_id': 'c52b33a3-4fbb-4a72-b64c-8bd6563810ae','event_id': 'ccacfe1e-398a-42cb-bccc-fd3a5f8ef293', 'feedback_text': 'This is a great app'},
    {'user_id': '2e0cee35-2ffe-4624-a043-c19cecd0b472','event_id': '2d8c4bf8-ff8a-4cb9-b60a-b514c4df6ee4',  'feedback_text': 'This is a wonderful app ' },
    {'user_id': '5c6cb802-0834-46e1-ae1b-396c3cbc75c8','event_id': 'a8a68074-b46e-4ead-8ed1-68791af31247',  'feedback_text': 'good app'},
    {'user_id': '519ad26c-d4f3-4380-b9dc-09a3a2fe6e36','event_id': '0366a101-12f0-4fbd-a727-2f13cfa9cd5c',  'feedback_text': 'make ui more attractive'},
    {'user_id': '9cb9323a-7235-499c-996a-8a989558d292','event_id': '593eb395-001b-44a7-b675-1f6fa5957857',  'feedback_text': 'make ux more responsive'},
    {'user_id': 'c8828526-01c8-44dc-a09e-afa162ccc9c7','event_id': 'd7cba507-b008-4fdc-a9e1-b26bbf667ae3',  'feedback_text': 'i loved the app logo'},
    {'user_id': 'c8828526-01c8-44dc-a09e-afa162ccc9c7','event_id': 'cce7dd0e-7c71-49c4-9642-aafaeee9d8be',  'feedback_text': 'i loved the design'},
    {'user_id': 'c52b33a3-4fbb-4a72-b64c-8bd6563810ae','event_id': '593eb395-001b-44a7-b675-1f6fa5957857',  'feedback_text': 'I loved the venue and the decorations at the event. It created a wonderful atmosphere'},
    {'user_id': '457d3c28-57ba-44bf-9bba-2c844b2a0c4c','event_id': '593eb395-001b-44a7-b675-1f6fa5957857',  'feedback_text': 'The event exceeded my expectations. The topics discussed were relevant and engaging.'},
    {'user_id': 'c52b33a3-4fbb-4a72-b64c-8bd6563810ae','event_id': 'ccacfe1e-398a-42cb-bccc-fd3a5f8ef293',  'feedback_text': 'The event registration process was seamless and user-friendly. Kudos to the team!'},
    {'user_id': '2e0cee35-2ffe-4624-a043-c19cecd0b472','event_id': '2d8c4bf8-ff8a-4cb9-b60a-b514c4df6ee4',  'feedback_text': 'The networking opportunities at the event were fantastic. I made valuable connections.'},
    {'user_id': '5c6cb802-0834-46e1-ae1b-396c3cbc75c8','event_id': 'a8a68074-b46e-4ead-8ed1-68791af31247',  'feedback_text': 'The food and beverages provided at the event were delicious. Thumbs up!'},
    {'user_id': '519ad26c-d4f3-4380-b9dc-09a3a2fe6e36','event_id': '0366a101-12f0-4fbd-a727-2f13cfa9cd5c',  'feedback_text': 'The event had a good mix of keynote speakers and interactive sessions. I learned a lot'},
    {'user_id': '9cb9323a-7235-499c-996a-8a989558d292','event_id': '593eb395-001b-44a7-b675-1f6fa5957857',  'feedback_text': 'The event app was helpful in keeping me updated with the schedule and session details.'},
    {'user_id': 'c8828526-01c8-44dc-a09e-afa162ccc9c7','event_id': 'd7cba507-b008-4fdc-a9e1-b26bbf667ae3',  'feedback_text': 'The event had a diverse range of attendees, which made for interesting discussions.'},
    {'user_id': 'c8828526-01c8-44dc-a09e-afa162ccc9c7','event_id': 'cce7dd0e-7c71-49c4-9642-aafaeee9d8be',  'feedback_text': 'The event team was responsive and accommodating to any queries or requests. Thank you!'},
    {'user_id': 'c52b33a3-4fbb-4a72-b64c-8bd6563810ae','event_id': '593eb395-001b-44a7-b675-1f6fa5957857',  'feedback_text': 'The event had a great variety of activities and entertainment options, keeping the attendees engaged throughout.'},
    {'user_id': '457d3c28-57ba-44bf-9bba-2c844b2a0c4c','event_id': '593eb395-001b-44a7-b675-1f6fa5957857',  'feedback_text': 'The event had a well-designed agenda with well-timed breaks and transitions. It flowed smoothly'},
    {'user_id': 'e3cd5c37-00a9-46ff-9004-0afac0df9c70','event_id': '55980b2b-4f50-4f11-80a2-4ad62e2ca860',  'feedback_text': 'The event provided ample opportunities for learning and skill-building. I left feeling inspired.'},
    {'user_id': 'c52b33a3-4fbb-4a72-b64c-8bd6563810ae','event_id': 'ccacfe1e-398a-42cb-bccc-fd3a5f8ef293',  'feedback_text': 'The event had engaging and interactive sessions that encouraged participation and discussion'},
    {'user_id': '2e0cee35-2ffe-4624-a043-c19cecd0b472','event_id': '2d8c4bf8-ff8a-4cb9-b60a-b514c4df6ee4',  'feedback_text': 'The event had a positive and welcoming atmosphere, making it easy to connect with fellow attendees.'},
]

# Insert the sample data into the attendees collection
attendees_collection.insert_many([attendee3])
# leaderboard_collection.insert_many(leaderboard_data)
# feedback_collection.insert_many(data)

print("Data inserted successfully.")
