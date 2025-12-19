import os
import redis
from dotenv import load_dotenv

load_dotenv()

class RedisConfig:
    def __init__(self):
        self.host = os.getenv('REDIS_HOST')
        self.port = int(os.getenv('REDIS_PORT'))
        self.db = int(os.getenv('REDIS_DB'))
        self.password = os.getenv('REDIS_PASSWORD')

    def connect(self):
        try:
            self.redis_client = redis.Redis(host=self.host, port=self.port, db=self.db, password=self.password)
            return self.redis_client
        except Exception as e:
            print(f"Error connecting to Redis: {str(e)}")
            return None

def main():
    config = RedisConfig()
    redis_client = config.connect()
    if redis_client:
        print("Connected to Redis")
        # example usage
        redis_client.set('test_key', 'test_value')
        print(redis_client.get('test_key'))
    else:
        print("Failed to connect to Redis")

if __name__ == "__main__":
    main()