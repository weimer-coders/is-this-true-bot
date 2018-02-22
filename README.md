# Is This True Bot
<<<<<<< HEAD
This is simple bot that responds to Tweets with potential fact checks. A person must reply to a Tweet with a link, tagging [@IsThisTrueBot](www.twitter.com/IsThisTrueBot) in order to return as to whether a fact-check that matches exists, if there isn't one or if not link was found.

This bot is still in the early stages of development. Currently, it only searches PolitiFact for fact-checks. We plan to expand the evaluation to pull in different sources, including Snopes and Google fact-check supporting websites. The longer-term goal is to use machine learning to expand our evaluation of sources.

If you tag a response and it's correct, please favorite the Tweet so we can begin to gather data on what is working well and what isn't as we dive into machine learning. Your feedback will help us improve this in the weeks to come.

## How does this work?

This script grabs the ID of the Tweet a person responds to and gets the URL of the article linked within it. From there, it takes the headline, searches it on PolitiFact and gets the search results on the first page.

After that, it parses the words and weights them according to headline, body text, rating text and the sources used to find the best match to the link on Twitter. It assigns a score to all of the matches, and if it meets a minimum confidence level, will reply to your Tweet with the link.
=======
This is simple bot that responds to Tweets with potential fact checks. A person must reply to a Tweet with a link, tagging [@IsThisTrueBot](www.twitter.com/IsThisTrueBot) and using the hashtag `#IsThisTrue`. Once they do, the bot will reply with a matching fact-check (if one exists) or an error if no link was found.

This bot is still in the early stages of development. Currently, it only searches PolitiFact for fact-checks. We plan to expand the evaluation to pull in different sources, including Snopes and other sites which support [`ClaimReview`](http://pending.webschemas.org/ClaimReview). The longer-term goal is to use machine learning to enhance our evaluation of sources.

If you tag a response and the bot is correct, please favorite the Tweet so we can begin to gather data on what is working well and what isn't as we dive into machine learning. Your feedback will help us improve this in the weeks to come.

## How Does This Work?

This script grabs the Tweet the tagged reply was in response to and gets the URL of the article linked within it. From there, it takes the headline, searches it on PolitiFact and gets the search results on the first page.

After that, it parses the words and weighs them according to headline, body text and the sources referenced in the article to find the best match to the link on Twitter. It assigns a score to all of the matches, and if the article meets a minimum confidence level, it will reply to your Tweet with the link.
>>>>>>> origin/master

## Installing a Development Copy
These instructions are mostly for us, but feel free to download a copy to play around with.

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
$ python isthistruebot/bot.py start
```

You can also stop or restart the stream listener
```bash
$ python isthistruebot/bot.py stop
$ python isthistruebot/bot.py restart
```


---
Made by [Andrew Briz](https://github.com/brizandrew) and [Caitlin Ostroff](https://github.com/ceostroff)
