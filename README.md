# Is This True Bot
A simple bot that responds to tweets with potential fact checks.

## Getting Started

Create a virtualenv to store the codebase.
```bash
$ virtualenv is-this-true-bot
```

Activate the virtualenv.
```bash
$ cd is-this-true-bot
$ . bin/activate
```

Clone the git repository from GitHub.
```bash
$ git clone https://github.com/weimer-coders/is-this-true-bot repo
```

Enter the repo and install its dependencies.
```bash
$ cd repo
$ pip install -r requirements.txt
```

Make a copy of the credentials file to add your own credentials
```bash
$ cp isthistruebot/credentials.template isthistruebot/credentials.py
```

Start the stream listener
```bash
$ python isthistruebot/bot.py
```
