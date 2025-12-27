const fs = require('fs');
const path = require('path');

class Parser {
  constructor(filePath) {
    this.filePath = filePath;
    this.config = {};
  }

  readConfig() {
    try {
      const data = fs.readFileSync(this.filePath, 'utf8');
      this.config = JSON.parse(data);
    } catch (error) {
      if (error.code === 'ENOENT') {
        console.error(`File ${this.filePath} not found.`);
      } else if (error instanceof SyntaxError) {
        console.error(`Invalid JSON in file ${this.filePath}.`);
      } else {
        console.error(`Error reading file ${this.filePath}: ${error}`);
      }
      throw error;
    }
  }

  getConfig() {
    return this.config;
  }

  validateConfig() {
    if (!this.config.redis) {
      throw new Error('Redis configuration not found in config file.');
    }
    if (!this.config.redis.host || !this.config.redis.port) {
      throw new Error('Redis host or port not specified in config file.');
    }
  }

  parse() {
    this.readConfig();
    this.validateConfig();
    return this.getConfig();
  }
}

module.exports = Parser;