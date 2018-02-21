import unittest
from tweeter import handle_incoming_tweet
from scraper import get_headline


class IsThisTrueBotTest(unittest.TestCase):
    def test_fact_check(self):
        message = handle_incoming_tweet("963350466968121344")
        should_be = "I found this on @PolitiFact. I think it might help. They rated the following as "
        should_be += "\"Pants on Fire!\". #FactCheck http://www.politifact.com/punditfact/statements/2018/feb/"
        should_be += "15/politico-news/no-four-million-democrat-votes-were-not-declared-f/"
        self.assertEqual(message, should_be)

    def test_no_fact_check_available(self):
        message = handle_incoming_tweet("965984263341473793")
        should_be = "Sorry. I couldn't find anything in any of my sources. I'm constantly learning though, so try "
        should_be += "again another time! " + u"\U0001f605" + " #JustBotProbz"
        self.assertEqual(message, should_be)

    def test_no_link_in_tweet(self):
        message = handle_incoming_tweet("956535969469124611")
        should_be = "Hmm. I can't seem to find a link. "
        should_be += u"\U0001F914" + " Are you sure you're replying to a Tweet with a link?"
        self.assertEqual(message, should_be)

    def test_not_response_tweet(self):
        message = handle_incoming_tweet("964944917222092800")
        should_be = "Hmm. I can't seem to find a link. "
        should_be += u"\U0001F914" + " Are you sure you're replying to a Tweet with a link?"
        self.assertEqual(message, should_be)

    def test_no_headline(self):
        headline = get_headline("http://andrewbriz.com/file-transfer/blank.html")
        self.assertEqual(headline, None)

    def test_tweet_to_itself(self):
        message = handle_incoming_tweet("966395681953931264")
        self.assertEqual(message, "")
