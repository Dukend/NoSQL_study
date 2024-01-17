import asyncio
import os

import aioredis_cluster
from fastapi import Depends

import aioredis_cluster


class RedisManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'redis'):
            self.redis = None

    async def connect(self):
        if self.redis is None:
            print(os.getenv("REDIS_URL"))
            try:
                self.redis = await aioredis_cluster.create_redis_cluster([
                    (os.getenv("REDIS_URL")),
                ])
                print("Connected to Redis Cluster")
            except Exception as e:
                print(f"Failed to connect to Redis Cluster: {e}, тут")

    async def disconnect(self):
        if self.redis:
            self.redis.close()
            await self.redis.wait_closed()
            print("Disconnected from Redis Cluster")

    async def lock_cache(self, key, timeout=10):
        lock_key = f"lock:{key}"
        acquired = await self.redis.set(lock_key, "locked", expire=timeout, exist="SET_IF_NOT_EXIST")
        return acquired

    async def get(self, key):
        try:
            value = await self.redis.get(key, encoding='utf-8')
            return value
        except Exception as e:
            print(f"Failed to get value from Redis: {e}")
            return None

    async def set(self, key, value):
        try:
            await self.redis.set(key, value)
            print(f"Set value {value} for key {key} in Redis")
        except Exception as e:
            print(f"Failed to set value in Redis: {e}")

    async def setex(self, key, time, value):
        try:
            await (self.redis.setex(key, time, value))
            return value
        except Exception as e:
            print(f"Failed to setex value in Redis: {e}")
