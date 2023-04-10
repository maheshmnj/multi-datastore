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
