import os

from elasticsearch import AsyncElasticsearch
from dotenv import load_dotenv
load_dotenv()
elasticsearch_client: AsyncElasticsearch = None
mapping = {
    "PostTypeId": {
        "type": "integer"
    },
    "AcceptedAnswerId": {
        "type": "integer"
    },
    "CreationDate": {
        "type": "date",
        "format": "strict_date_optional_time"
    },
    "Score": {
        "type": "integer"
    },
    "ViewCount": {
        "type": "integer"
    },
    "Body": {
        "type": "text"
    },
    "OwnerUserId": {
        "type": "integer"
    },
    "LastActivityDate": {
        "type": "date",
        "format": "strict_date_optional_time"
    },
    "Title": {
        "type": "text"
    },
    "Tags": {
        "type": "text"
    },
    "AnswerCount": {
        "type": "integer"
    },
    "CommentCount": {
        "type": "integer"
    },
    "ContentLicense": {
        "type": "text"
    },
    "LastEditorUserId": {
        "type": "integer"
    },
    "LastEditDate": {
        "type": "date",
        "format": "strict_date_optional_time"
    }
}


async def connect_elasticsearch_and_init():
    global elasticsearch_client
    elasticsearch_url = os.getenv('ELASTICSEARCH_URI')
    try:
        elasticsearch_client = AsyncElasticsearch(elasticsearch_url)
        await elasticsearch_client.info()
        print(f"elastic\t OK\t {elasticsearch_url}")

    except Exception as Ex:
        print(f"elastic\t ERROR\t{Ex} | {elasticsearch_url}")


async def close_connect_ES():
    if elasticsearch_client is None:
        return
    await elasticsearch_client.close()


def get_elasticsearch_client():
    return elasticsearch_client
