import os
import json
from typing import Dict
from redis import Redis

class RedisConfig:
    def __init__(self, host: str = 'localhost', port: int = 6379, db: int = 0):
        self.host = host
        self.port = port
        self.db = db
        self.redis_client = Redis(host=host, port=port, db=db)

    def get_config(self, key: str) -> str:
        return self.redis_client.get(key)

    def set_config(self, key: str, value: str) -> bool:
        return self.redis_client.set(key, value)

    def delete_config(self, key: str) -> int:
        return self.redis_client.delete(key)

    def get_all_configs(self) -> Dict:
        configs = {}
        for key in self.redis_client.scan_iter():
            configs[key] = self.redis_client.get(key)
        return configs

def main():
    config = RedisConfig()
    while True:
        print("1. Get config")
        print("2. Set config")
        print("3. Delete config")
        print("4. Get all configs")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            key = input("Enter key: ")
            print(config.get_config(key))
        elif choice == "2":
            key = input("Enter key: ")
            value = input("Enter value: ")
            print(config.set_config(key, value))
        elif choice == "3":
            key = input("Enter key: ")
            print(config.delete_config(key))
        elif choice == "4":
            print(config.get_all_configs())
        elif choice == "5":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()