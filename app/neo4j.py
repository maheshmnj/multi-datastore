import os
from dotenv import load_dotenv
from neo4j import GraphDatabase
import logging
from neo4j.exceptions import ServiceUnavailable

class Neo4JApp:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        # Don't forget to close the driver connection when you are finished with it
        self.driver.close()

    def insert_events(self):
        insertQuery = (
            """
            CREATE (e:Event {
                id: "0d7ee532-9a9c-4df8-8b02-52c5483b3c79",
                name: "Tech Summit",
                description: "Join us for a day of talks and networking with industry leaders in tech",
                starts_at: "2023-05-12T09:00:00Z",
                ends_at: "2023-05-12T17:00:00Z",
                cover_image: "https://example.com/images/tech_summit.jpg",
                address: "123 Main St, Anytown, USA",
                private: false,
                max_capacity: 100,
                created_at: "2023-04-09T10:00:00Z"
                })
            WITH e
            MATCH (e:Event {id: '0d7ee532-9a9c-4df8-8b02-52c5483b3c79'})
            MERGE (t:Tag {tag_name: 'Innovation'})
            MERGE (e)-[:HAS_TAG]->(t)
            """)
        with self.driver.session(database="neo4j") as session:
            # Write transactions allow the driver to handle retries and transient errors
            result = session.execute_write(self._insert_and_return_event, insertQuery)
            for row in result:
                print("Created event: {row}".format(row=row))

    @staticmethod
    def _insert_and_return_event(tx, insertQuery):
        result = tx.run(insertQuery)
        return [{"id": row["id"], "name": row["name"]}
                for row in result]


    def create_tags(self):
        insertQuery = (
            """
            CREATE (t1:Tag {tag_id: 1, tag_name: 'Technology'})
            CREATE (t2:Tag {tag_id: 2, tag_name: 'Innovation'})
            CREATE (t3:Tag {tag_id: 3, tag_name: 'Science'})
            CREATE (t4:Tag {tag_id: 4, tag_name: 'Art'})
            CREATE (t5:Tag {tag_id: 5, tag_name: 'Design'})
            CREATE (t6:Tag {tag_id: 6, tag_name: 'Fashion'})
            CREATE (t7:Tag {tag_id: 7, tag_name: 'Music'})
            CREATE (t8:Tag {tag_id: 8, tag_name: 'Film'})
            CREATE (t9:Tag {tag_id: 9, tag_name: 'Entertainment'})
            """)
        with self.driver.session(database="neo4j") as session:
            # Write transactions allow the driver to handle retries and transient errors
            result = session.execute_write(self._create_and_return_tag, insertQuery)
            for row in result:
                print("Created tag: {row}".format(row=row))

    @staticmethod
    def _create_and_return_tag(tx, insertQuery):
        result = tx.run(insertQuery)
        return [{"tag_id": row["tag_id"], "tag_name": row["tag_name"]}
                for row in result]

    def find_tags(self):
        with self.driver.session(database="neo4j") as session:
            # Read transactions allow the driver to handle retries and transient errors
            result = session.execute_read(self._find_and_return_tag)
            for row in result:
                print("Found tag: {row}".format(row=row))

    @staticmethod
    def _find_and_return_tag(tx):
        query = (
            "MATCH (t:Tag) "
            "RETURN t.tag_id AS tag_id, t.tag_name AS tag_name"
        )
        result = tx.run(query)
        return [{"tag_id": row["tag_id"], "tag_name": row["tag_name"]}
                for row in result]


