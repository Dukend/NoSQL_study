import os

from pymemcache import HashClient, Client

from src.cache.json_serialaizer import JsonSerializer

memcached_client: Client = None


def get_memcached_clinet() -> Client:
    return memcached_client


def init_memcached_connection():
    global memcached_client
    memcached_URI = "localhost:11211,localhost:11212,localhost:11213"
    try:

        memcached_client = HashClient(
            memcached_URI.split(","),
            serde=JsonSerializer())
        print(f"memcached\t OK\t {memcached_URI}")
    except Exception as Ex:
        print(f"memcached\t ERROR\t{Ex}")


def close_memcached_connection():
    global memcached_client
    if memcached_client is None:
        return
    memcached_client.close()
