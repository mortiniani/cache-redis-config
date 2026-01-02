package helpers

import (
	"encoding/json"
	"errors"
	"fmt"
	"log"
	"net/http"
	"os"
	"strconv"
	"strings"

	"github.com/go-redis/redis/v9"
)

var (
	redisClient *redis.Client
)

func init() {
	redisAddr := os.Getenv("REDIS_ADDR")
	redisPort := os.Getenv("REDIS_PORT")
	redisDB := os.Getenv("REDIS_DB")
	redisPassword := os.Getenv("REDIS_PASSWORD")

	if redisAddr == "" || redisPort == "" || redisDB == "" {
		log.Fatal("Redis environment variables not set")
	}

	db, err := strconv.Atoi(redisDB)
	if err != nil {
		log.Fatal(err)
	}

	redisClient = redis.NewClient(&redis.Options{
		Addr:     fmt.Sprintf("%s:%s", redisAddr, redisPort),
		Password: redisPassword,
		DB:       db,
	})
}

func GetRedisClient() *redis.Client {
	return redisClient
}

func GetValue(key string) (string, error) {
	val, err := redisClient.Get(key).Result()
	if err != nil {
		if errors.Is(err, redis.Nil) {
			return "", nil
		}
		return "", err
	}
	return val, nil
}

func SetValue(key string, value string) error {
	return redisClient.Set(key, value, 0).Err()
}

func DeleteKey(key string) error {
	return redisClient.Del(key).Err()
}

func HandleError(err error) {
	if err != nil {
		log.Println(err)
		http.Error(nil, err.Error(), http.StatusInternalServerError)
	}
}

func StringToJson(str string) (map[string]interface{}, error) {
	var jsonMap map[string]interface{}
	err := json.Unmarshal([]byte(str), &jsonMap)
	if err != nil {
		return nil, err
	}
	return jsonMap, nil
}

func JsonToString(jsonMap map[string]interface{}) (string, error) {
	jsonStr, err := json.Marshal(jsonMap)
	if err != nil {
		return "", err
	}
	return string(jsonStr), nil
}

func SplitString(s string, sep string) []string {
	return strings.Split(s, sep)
}