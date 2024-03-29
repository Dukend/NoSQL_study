import asyncio

from src.cache.Memcached_utils import init_memcached_connection, close_memcached_connection
from src.mongo_interface.DBConnection import connect_and_init_db, close_connect
from src.elastic_interface.elasticsearch_utils import close_connect_ES, connect_elasticsearch_and_init


async def handle_startup():
    init_mongo_future = connect_and_init_db()
    init_elasticsearch_future = connect_elasticsearch_and_init()

    await asyncio.gather(init_mongo_future, init_elasticsearch_future)
    init_memcached_connection()


async def handle_shutdown():
    await close_connect()
    await close_connect_ES()
    close_memcached_connection
