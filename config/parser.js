const fs = require('fs');
const path = require('path');

class ConfigParser {
  constructor(configFile) {
    this.configFile = configFile;
    this.config = {};
  }

  readConfig() {
    try {
      const data = fs.readFileSync(this.configFile, 'utf8');
      this.config = JSON.parse(data);
    } catch (error) {
      if (error.code === 'ENOENT') {
        throw new Error(`Config file not found: ${this.configFile}`);
      } else if (error instanceof SyntaxError) {
        throw new Error(`Invalid JSON in config file: ${this.configFile}`);
      } else {
        throw error;
      }
    }
  }

  getConfig() {
    return this.config;
  }

  getRedisConfig() {
    return this.config.redis;
  }

  getCacheConfig() {
    return this.config.cache;
  }
}

function loadConfig(configFile) {
  const parser = new ConfigParser(configFile);
  parser.readConfig();
  return parser;
}

module.exports = loadConfig;