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

The following environment variables must be set:
- `TELEGRAM_TOKEN`
- `API_URL`

## To start bot

```bash
$ python3 bot.py
```
