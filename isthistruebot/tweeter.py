#! /usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
import re
from credentials import TWITTER_KEYS
from tweepy import TweepError
from politifact import search_pf
from scraper import get_headline
from evaluator import get_best_answer

twitter_auth = tweepy.OAuthHandler(TWITTER_KEYS['consumer_key'], TWITTER_KEYS['consumer_secret'])
twitter_auth.set_access_token(TWITTER_KEYS['access_token'], TWITTER_KEYS['access_token_secret'])
twitter = tweepy.API(twitter_auth)


def get_tweet_response_link(tweet_id):
    """
    Receives a Tweet Id and finds the Tweet it was in response to.
    Then finds the link in that Tweet that was responded to.
    Returns the link.
    """
    reply_tweet = twitter.get_status(tweet_id)
    top_level_id = reply_tweet.in_reply_to_status_id

    try:
        top_level_tweet = twitter.get_status(top_level_id, tweet_mode='extended')
    except TweepError:
        return None

    try:
        url = top_level_tweet.entities["urls"][0]["expanded_url"]
    except IndexError:
        return None

    twitter_regex = re.compile('^https?://twitter\.com')
    if twitter_regex.match(url):
        return None
    else:
        return url


def genererate_response(answer=0):
    """
    Creates a dynamic message based on the answer chosen (or if no answer was chosen).
    Creates an error message if no answer is passed to the function.
    Returns the message.
    """
    # Error Text
    if answer == 0:
        text = "Hmm. I can't seem to find a link." + u"\U0001F914"
        text += " Are you sure you're replying to a Tweet with a link?"
    # Failure Text
    elif answer is None:
        text = "Sorry. I couldn't find anything in any of my sources."
        text += " I'm constantly learning though, so try again another time! " + u"\U0001F605 " + "#JustBotProbz"
    # Success Text
    else:
        # text = "I found this on" + answer["source"] + ". I think it might help."
        text = "I found this on {s}. I think it might help.".format(
            s=answer["source"]
        )
        text += " They rated the following as \"{answer}\". #FactCheck {link}".format(
            answer=answer["answer"],
            link=answer["link"]
        )

    return text


def handle_incoming_tweet(tweet_id):
    """
    Recieves a Tweet Id and generates a response based on the Tweet.
    Returns the response.
    """
    article = get_tweet_response_link(tweet_id)

    if article is None:
        return genererate_response()

    headline = get_headline(article)
    pages = search_pf(headline)
    answer = get_best_answer(pages)

    return genererate_response(answer)


def tweet_reply(message, reply_id, username):
    """
    Tweets a message in reply to a specific Tweet and user.
    """
    message = "@{username} {message}".format(
        username=username,
        message=message
    )

    twitter.update_status(message, reply_id)


class StreamListener(tweepy.StreamListener):
    """
    Uses the Twitter Stream API to listen to incoming tweets.
    """
    def on_status(self, status):
        """
        Generates a response based on a Tweet.
        Responds to the original Tweeter with the response.
        """
        message = handle_incoming_tweet(status.id)
        user = status.user.screen_name
        tweet_reply(message, status.id, user)
