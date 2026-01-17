import logging
import redis
from typing import Optional

class CacheConfig:
    def __init__(self, host: str = 'localhost', port: int = 6379, db: int = 0):
        self.host = host
        self.port = port
        self.db = db
        self.redis_client = None

    def connect(self):
        try:
            self.redis_client = redis.Redis(host=self.host, port=self.port, db=self.db)
            self.redis_client.ping()
        except redis.exceptions.RedisError as e:
            logging.error(f"Failed to connect to Redis: {e}")

    def get(self, key: str) -> Optional[str]:
        if self.redis_client:
            return self.redis_client.get(key)
        else:
            logging.error("Redis client is not connected")
            return None

    def set(self, key: str, value: str) -> bool:
        if self.redis_client:
            return self.redis_client.set(key, value)
        else:
            logging.error("Redis client is not connected")
            return False

def main():
    cache_config = CacheConfig()
    cache_config.connect()
    cache_config.set("test_key", "test_value")
    print(cache_config.get("test_key"))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()