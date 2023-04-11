
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore



# Use a service account
cred = credentials.Certificate("serviceaccount.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

class Event:
    def __init__(self):
        self.id = None,
        self.name = None,
        self.description = None,
        self.startsAt = None,
        self.endsAt = None,
        self.cover_image = None,
        self.address = None,
        self.private = None,
        self.deleted = None,
        self.user = None;


    def event_to_dict(self):
        return {
            u'id': self.id,
            u'name': self.name,
            u'description': self.description,
            u'startsAt': self.startsAt,
            u'endsAt': self.endsAt,
            u'cover_image': self.cover_image,
            u'address': self.address,
            u'private': self.private,
            u'deleted': self.deleted,
            u'user': self.user.user_to_dict(),
        }

# event object from dictionary
    def event_from_dict(self, event_dict):
        self.id = event_dict['id']
        self.name = event_dict['name']
        self.description = event_dict['description']
        self.startsAt = event_dict['startsAt']
        self.endsAt = event_dict['endsAt']
        self.cover_image = event_dict['cover_image']
        self.address = event_dict['address']
        self.private = event_dict['private']
        self.deleted = event_dict['deleted']
        self.user = event_dict['user']
        return self

    def insert_bookmark(self,user):
        doc_ref = db.collection(u'bookmarks').document(u'{}'.format(user.email))
        doc_ref.set({
            u'user_id': user.user_id,
            u'name': user.name,
            u'email': user.email,
            u'username': user.username,
            u'avatar_url': user.avatar_url,
        })
        doc_ref.collection(u'events').document().set({
            u'event_id': self.id,
            u'user_id': user.user_id,
            u'name': self.name,
            u'description': self.description,
            u'startsAt': self.startsAt,
            u'endsAt': self.endsAt,
            u'cover_image': self.cover_image,
            u'address': self.address,
            u'private': self.private,
            u'deleted': self.deleted,
        })



class User:
    def __init__(self):
        self.user_id = None,
        self.name = None,
        self.email = None,
        self.username= None,
        self.avatar_url= None

    def user_to_dict(self):
        return {
            u'user_id': self.user_id,
            u'name': self.name,
            u'email': self.email,
            u'username': self.username,
            u'avatar_url': self.avatar_url,
        }

    def user_from_dict(self, user_dict):
        # user_dict = json.loads(user_dict)
        self.user_id = user_dict['user_id']
        self.name = user_dict['name']
        self.email = user_dict['email']
        self.username = user_dict['username']
        self.avatar_url = user_dict['avatar_url']
        return self

user_dicts = [
    {
        'user_id':  '38d61eba-45ef-460a-b9d3-ccdbaf7a4187',
        'email': 'johnsmith@example.com',
        'avatar_url': 'http://example.com/avatar1.jpg',
        'isAdmin': True,
        'username': 'johnsmith',
        'name': 'John Smith',
        'created_at': '2019-01-01 00:00:00',
    },
    {
        'user_id':  '5c6cb802-0834-46e1-ae1b-396c3cbc75c8',
        'email': 'janedoe@example.com',
        'avatar_url': 'http://example.com/avatar2.jpg',
        'isAdmin': False,
        'username': 'johndoe',
        'isAdmin': False,
        'name': 'Jane Doe',
        'createdAt': '2019-01-01 00:00:00',
    }
]

event_dicts = [
    # (id, created_at, name, description, starts_at, ends_at, cover_image, address, private, deleted, user_id)

    {
        "id": "b293293b-b133-4a2b-8aa4-d9afb488c680",
        "createdAt": "2019-01-01 00:00:00",
            "name": "TED2023 Conference",
            "description": "TED is a nonprofit devoted to spreading ideas, usually in the form of short, powerful talks.",
            "startsAt": "2019-02-01 00:00:00",
            "endsAt": "2019-02-04 00:00:00",
            "cover_image": "https://ted.com/talks/cover.jpg",
            "address": "Vancouver Convention Centre, Vancouver, Canada",
            "private": False,
            "deleted": False,
            "user": User().user_from_dict(user_dicts[0])
    },
    {
            "id": "ccacfe1e-398a-42cb-bccc-fd3a5f8ef293",
            "createdAt": "2019-01-01 00:00:00",
            "name": "Web Summit 2023",
            "description": "Web Summit brings together the people and companies redefining the global tech industry.",
            "startsAt": "2019-02-01 00:00:00",
            "endsAt": "2019-02-04 00:00:00",
            "cover_image": "https://websummit.com/cover.jpg",
            "address": "Altice Arena, Lisbon, Portugal",
            "private": False,
            "deleted": False,
            "user": User().user_from_dict(user_dicts[1])

    },
    {
            "id": "2d8c4bf8-ff8a-4cb9-b60a-b514c4df6ee4",
            "createdAt": "2019-01-01 00:00:00",
            "name": "Comic Con 2023",
            "description": "Comic Con is a multi-genre entertainment and comic convention.",
            "startsAt": "2019-02-01 00:00:00",
            "endsAt": "2019-02-04 00:00:00",
            "cover_image": "https://comiccon.com/cover.jpg",
            "address": "San Diego Convention Center, San Diego, USA",
            "private": False,
            "deleted": False,
            "user": User().user_from_dict(user_dicts[0])
    },
    {
    "id": "a8a68074-b46e-4ead-8ed1-68791af31247",
    "createdAt": "2019-01-01 00:00:00",
    "name": "Cannes Film Festival 2023",
    "description": "Cannes Film Festival is an annual film festival held in Cannes, France.",
    "startsAt": "2019-02-01 00:00:00",
    "endsAt": "2019-02-04 00:00:00",
    "cover_image": "https://cannes.com/cover.jpg",
    "address": "Palais des Festivals et des Congrès, Cannes, France",
    "private": False,
    "deleted": False,
    "user": User().user_from_dict(user_dicts[1])
    },
    {
    "id": "b293293b-b133-4a2b-8aa4-d9afb488c680",
    "createdAt": "2019-01-01 00:00:00",
    "name": "TED2023 Conference",
    "description": "TED is a nonprofit devoted to spreading ideas, usually in the form of short, powerful talks.",
    "startsAt": "2019-02-01 00:00:00",
    "endsAt": "2019-02-04 00:00:00",
    "cover_image": "https://ted.com/talks/cover.jpg",
    "address": "Vancouver Convention Centre, Vancouver, Canada",
    "private": False,
    "deleted": False,
    "user": User().user_from_dict(user_dicts[0])
    },
    {
    "id": "cce7dd0e-7c71-49c4-9642-aafaeee9d8be",
    "createdAt": "2019-01-01 00:00:00",
    "name": "New York Fashion Week",
    "description": "This is a Fashion week in the times Square",
    "startsAt": "2019-02-01 00:00:00",
    "endsAt": "2019-02-04 00:00:00",
    "cover_image": "https://artbasel.com/cover.jpg",
    "address": "Messe Basel, Basel, Switzerland",
    "private": False,
    "deleted": False,
    "user": User().user_from_dict(user_dicts[1])
    },
    {
    "id": "0366a101-12f0-4fbd-a727-2f13cfa9cd5c",
    "createdAt": "2019-01-01 00:00:00",
    "name": "Coachella 2023",
    "description": "Coachella is an annual music and arts festival held in California.",
    "startsAt": "2019-02-01 00:00:00",
    "endsAt": "2019-02-04 00:00:00",
    "cover_image": "https://coachella.com/cover.jpg",
    "address": "Empire Polo Club, Indio, California, USA",
    "private": False,
    "deleted": False,
    "user": User().user_from_dict(user_dicts[0])
    }
]



if __name__ == '__main__':
    event = Event()
    user = User()

    for i in range(0, len(event_dicts)):
        event_dict = event_dicts[i]
        user_dict = user_dicts[i% len (user_dicts)]
        event = event.event_from_dict(event_dict)
        user = user.user_from_dict(user_dict)
        event.insert_bookmark(user)
        print(event.event_to_dict())


