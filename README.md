# How to use

1. Download this repository
2. `cd ci-demon`
3. Run `python setup.py install`. It will install `ci-demon` package (and some dependencies) to your system, and it will
   be accessible from command line
4. Check `pip list -l`.
   You should see something like that
   ```text
   Package                   Version
   ------------------------- -------
   ci-demon                   0.1.0
   ```
5. execute `ci-demon <path_to_configuration_file>` See [configuration file](#configuration-file-requirements) for more
   details

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

## Remove ci-demon

To remove `ci-demon` just write: `pip uninstall ci-demon`

## Start as a service

To add `ci-demon` as a system service, do the following steps:

```shell
$ cd ci-demon
$ sudo cp ci-demon.service /etc/systemd/system/ci-demon.service
$ sudo systemctl daemon-reload
$ sudo systemctl enable ci-demon.service
$ sudo systemctl start ci-demon.service
# check the status
$ sudo systemctl status ci-demon.service
```

To remove `ci-demon`:

```shell
$ cd ~
$ sudo systemctl disable ci-demon.service
$ rm /etc/systemd/system/ci-demon.service
$ sudo systemctl daemon-reload
```