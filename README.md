# Startup requirements

ci-demon application service accept one necessary argument: [configuration file](#configuration-file-requirements)

## Configuration file requirements

- accept only json format
- all keys should be in upper case

### Example of configuration file

```json
{
  "AUTH": {
    "TOKEN": "secret-token"
  },
  "TRANSLITERATE_BOT": {
    "TG_TOKEN": "1111:1xXx1",
    "BOT_FOLDER": "/path/to/main/executable/file",
    "MAIN_EXECUTABLE_FILE": "bot"
  }
}

```

#### Description of configuration values

1. AUTH
    1. TOKEN - token to authorize http requests [necessary]
2. TRANSLITERATE_BOT - settings to start the 'transliterate' bot
    1. TG_TOKEN - unique telegram token
    2. BOT_FOLDER - absolute path to MAIN_EXECUTABLE_FILE
    3. MAIN_EXECUTABLE_FILE - main executable file