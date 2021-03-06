import sys
import tweepy

from tweeter import twitter, StreamListener
from daemon import Daemon


reload(sys)
sys.setdefaultencoding('utf-8')


class BotDaemon(Daemon):
    def run(self):
        """
        Create a Custom Tweepy stream listener and start listening for Tweets tagged with @IsThisTrueBot
        """
        stream = tweepy.Stream(auth=twitter.auth, listener=StreamListener())
        stream.filter(track=['@IsThisTrueBot #IsThisTrue'], async=True)


if __name__ == "__main__":
    daemon = BotDaemon('/tmp/daemon-example.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)
