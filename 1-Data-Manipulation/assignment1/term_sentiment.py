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
    
    newScores = {}
    rawTweets = tweet_file.readlines()
    for rt in rawTweets:
        tweet = json.loads(rt)
        sent = 0
        if tweet.has_key('text'):
            text = tweet['text'].split()
            for t in text:
                if scores.has_key(t.lower()):
                    sent += scores[t.lower()]
            for t in text:
                if not scores.has_key(t.lower()):
                    if newScores.has_key(t.lower()):
                        newScores[t.lower()][0] += sent
                        newScores[t.lower()][1] += 1
                    else:
                        newScores[t.lower()] = [sent, 1]
    for ns in newScores.iteritems():
        print ns[0], float(ns[1][0]) / ns[1][1]

if __name__ == '__main__':
    main()
