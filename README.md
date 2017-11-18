# Telegram Bot

## Requirements

First, Redis is needed:
```bash
$ sudo apt install redis-server
```

These are the Python packages dependencies.
```
python-telegram-bot>=8.1.1
requests>=2.18.1
redis>=2.10.6
```

The `TELEGRAM_TOKEN` environment variable must be set.

## To start bot

```bash
$ python3 bot.py
```
