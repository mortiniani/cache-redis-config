import logging
import redis
from typing import Optional

class RedisConfig:
    def __init__(self, host: str, port: int, db: int, password: Optional[str] = None):
        self.host = host
        self.port = port
        self.db = db
        self.password = password

class RedisClient:
    def __init__(self, config: RedisConfig):
        self.config = config
        self.client = self._create_client()

    def _create_client(self) -> redis.Redis:
        client = redis.Redis(host=self.config.host, port=self.config.port, db=self.config.db, password=self.config.password)
        return client

    def get(self, key: str) -> str:
        return self.client.get(key)

    def set(self, key: str, value: str) -> bool:
        return self.client.set(key, value)

    def exists(self, key: str) -> bool:
        return self.client.exists(key)

    def delete(self, key: str) -> int:
        return self.client.delete(key)

def create_redis_client(config: RedisConfig) -> RedisClient:
    return RedisClient(config)

def main():
    config = RedisConfig(host='localhost', port=6379, db=0)
    client = create_redis_client(config)
    logging.info(client.get('test_key'))

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()