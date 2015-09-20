import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)
   
    rawTweets = tweet_file.readlines()
    for rt in rawTweets:
        tweet = json.loads(rt)
        sent = 0
        if tweet.has_key('text'):
            text = tweet['text'].split()
            for t in text:
                if scores.has_key(t):
                    sent += scores[t]
        print sent

if __name__ == '__main__':
    main()
