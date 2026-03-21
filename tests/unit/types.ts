// Types for cache-redis-config

declare module "@types/redis" {
  interface RedisClient {
    pubsub?: RedisPubSub;
  }

  interface RedisPubSub {
    onMessage: (channel: string, message: any) => void;
    onPMessage: (pattern: string, message: any) => void;
    onReadyStateChange: () => void;
    onConnection(): void;
    onConnectionEnd(): void;
    onMessageBufferLength(): void;
  }

  interface RedisScript {
    load: (script: string) => Promise<any>;
    run: (key: string, args: any[]) => Promise<any>;
  }

  interface RedisCluster {
    onMessage: (channel: string, message: any) => void;
    onPMessage: (pattern: string, message: any) => void;
    onReadyStateChange: () => void;
    onConnection(): void;
    onConnectionEnd(): void;
    onMessageBufferLength(): void;
  }

  interface RedisClusterNode {
    name: string;
    host: string;
    port: number;
    onMessage: (channel: string, message: any) => void;
    onPMessage: (pattern: string, message: any) => void;
  }
}

declare module "redis" {
  interface RedisClient {
    options: {
      queueLimit?: number;
      retryStrategy?: (times: number) => number;
      socketTimeout?: number;
      enableReadyCheck?: boolean;
      enableOffload?: boolean;
      enableMultiCores?: boolean;
    };
  }
}

declare module "redis-cluster" {
  interface RedisCluster {
    addNode(node: RedisClusterNode, options: any): void;
    delNode(node: string): void;
    rebalance(): void;
    addNode(node: RedisClusterNode, options: RedisClusterOptions): void;
  }

  interface RedisClusterOptions {
    maxRedirections?: number;
    onmessage?: (channel: string, message: any) => void;
    onpmmessage?: (pattern: string, message: any) => void;
  }
}