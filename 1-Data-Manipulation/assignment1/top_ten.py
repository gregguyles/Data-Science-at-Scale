import sys
import json
from operator import itemgetter
def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    
    hashTags = {}
    rawTweets = tweet_file.readlines()
    for rt in rawTweets:
        tweet = json.loads(rt)
        if 'entities' in tweet and 'hashtags' in tweet['entities']:
            for htObj in tweet['entities']['hashtags']:
                ht = htObj['text']
                hashTags[ht] = 1 if ht not in hashTags else hashTags[ht] + 1 
   
    
    htList = []
    for h in hashTags.iteritems():
        htList.append([h[0], h[1]])
    sortedHt = sorted(htList, key=itemgetter(1), reverse=True)
    for i in range(10):
        print sortedHt[i][0], sortedHt[i][1]
if __name__ == '__main__':
    main()
