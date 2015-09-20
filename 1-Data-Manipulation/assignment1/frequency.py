import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])

    termCt = 0
    terms = {}
    rawTweets = tweet_file.readlines()
    for rt in rawTweets:
        tweet = json.loads(rt)
        if tweet.has_key('text'):
            text = tweet['text'].split()
            for t in text:
                if terms.has_key(t):
                    terms[t] += 1
                else:
                    terms[t] = 1
                termCt += 1
    for term in terms.iteritems():
        print term[0], float(term[1]) / termCt

if __name__ == '__main__':
    main()
