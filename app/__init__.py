from flask import Flask, jsonify
from pymongo import MongoClient
from neo4j import GraphDatabase
from cassandra.cluster import Cluster
import boto3
from dotenv import load_dotenv
import os
from app.neo4j import Neo4JApp

app = Flask(__name__)

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Create MongoDB connection
def connect_mongodb():
    client = MongoClient('localhost', 27017)
    db = client['csevents']
    return db.users.find()

# Create Neo4j connection
def connect_neo4j():
    driver = GraphDatabase.driver("neo4j+s://f007a9d0.databases.neo4j.io", auth=( os.environ.get('USERNAME_NEO4J') , os.environ.get("NEO4J_PASSWORD")))
    with driver.session() as session:
        results = session.run("MATCH (n:Event) RETURN n")
        return jsonify({'events': results.data()})

# Create Cassandra connection
def connect_cassandra():
    cluster = Cluster(['localhost'], port=9042)
    session = cluster.connect('csevents')
    rows = session.execute('SELECT * FROM bookmarks')
    return rows

# Create DynamoDB connection
def connect_dynamodb():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('bookmarks')
    response = table.scan()
    return response['Items']

# API endpoint to get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = connect_mongodb()
    return jsonify({'users': users})

# API endpoint to get all events
@app.route('/events', methods=['GET'])
def insert_events():
    uri = "neo4j+s://fc691a1c.databases.neo4j.io"
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    user = os.environ.get('USERNAME_NEO4J')
    password = os.environ.get("PASSWORD_NEO4J")
    neo4jApp = Neo4JApp(uri, user, password)
    result = neo4jApp.insert_events()
    result = neo4jApp.create_tags()
    neo4jApp.close()
    return jsonify({'events': 'success'})

# API endpoint to get all bookmarks
@app.route('/bookmarks', methods=['GET'])
def get_bookmarks():
    bookmarks = connect_dynamodb()
    return jsonify({'bookmarks': bookmarks})

# API endpoint to get all feedback
@app.route('/feedback', methods=['GET'])
def get_feedback():
    feedback = connect_cassandra()
    return jsonify({'feedback': feedback})