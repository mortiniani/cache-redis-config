package cache_redis_config

import (
	"log"
	"os"
	"time"

	"github.com/go-redis/redis/v7"
)

func NewRedisClient() *redis.Client {
	client := redis.NewClient(&redis.Options{
		Addr:     os.Getenv("REDIS_ADDR"),
		Password: os.Getenv("REDIS_PASSWORD"),
		DB:       0,
	})

	_, err := client.Ping().Result()
	if err != nil {
		log.Fatal(err)
	}

	return client
}

func NewRedisClientWithTimeout(addr string, password string, db int, timeout time.Duration) *redis.Client {
	client := redis.NewClient(&redis.Options{
		Addr:     addr,
		Password: password,
		DB:       db,
		DialTimeout: timeout,
		ReadTimeout: timeout,
		WriteTimeout: timeout,
	})

	_, err := client.Ping().Result()
	if err != nil {
		log.Fatal(err)
	}

	return client
}