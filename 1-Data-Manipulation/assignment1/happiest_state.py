import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    statesAbv = {
            'AK': 'Alaska',
            'AL': 'Alabama',
            'AR': 'Arkansas',
            'AS': 'American Samoa',
            'AZ': 'Arizona',
            'CA': 'California',
            'CO': 'Colorado',
            'CT': 'Connecticut',
            'DC': 'District of Columbia',
            'DE': 'Delaware',
            'FL': 'Florida',
            'GA': 'Georgia',
            'GU': 'Guam',
            'HI': 'Hawaii',
            'IA': 'Iowa',
            'ID': 'Idaho',
            'IL': 'Illinois',
            'IN': 'Indiana',
            'KS': 'Kansas',
            'KY': 'Kentucky',
            'LA': 'Louisiana',
            'MA': 'Massachusetts',
            'MD': 'Maryland',
            'ME': 'Maine',
            'MI': 'Michigan',
            'MN': 'Minnesota',
            'MO': 'Missouri',
            'MP': 'Northern Mariana Islands',
            'MS': 'Mississippi',
            'MT': 'Montana',
            'NA': 'National',
            'NC': 'North Carolina',
            'ND': 'North Dakota',
            'NE': 'Nebraska',
            'NH': 'New Hampshire',
            'NJ': 'New Jersey',
            'NM': 'New Mexico',
            'NV': 'Nevada',
            'NY': 'New York',
            'OH': 'Ohio',
            'OK': 'Oklahoma',
            'OR': 'Oregon',
            'PA': 'Pennsylvania',
            'PR': 'Puerto Rico',
            'RI': 'Rhode Island',
            'SC': 'South Carolina',
            'SD': 'South Dakota',
            'TN': 'Tennessee',
            'TX': 'Texas',
            'UT': 'Utah',
            'VA': 'Virginia',
            'VI': 'Virgin Islands',
            'VT': 'Vermont',
            'WA': 'Washington',
            'WI': 'Wisconsin',
            'WV': 'West Virginia',
            'WY': 'Wyoming'
    }
    statesFull = {}
    stateSent = {}
    for s in statesAbv.iteritems():
        statesFull[s[1]] = s[0]
        stateSent[s[0]] = [0, 0]

    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    rawTweets = tweet_file.readlines()
    for rt in rawTweets:
        sent = 0
        tweet = json.loads(rt)
        if 'text' in tweet:
            text = tweet['text'].split()
            for t in text:
                if scores.has_key(t):
                    sent += scores[t]
            if 'user' in tweet and 'location' in tweet['user']:
                loc = tweet['user']['location'].split()
                for l in loc:
                    if l in statesAbv:
                        stateSent[l][0] += sent
                        stateSent[l][1] += 1
                        break
                    elif l in statesFull:
                        stateSent[statesFull[l]][0] += sent
                        stateSent[statesFull[l]][1] += 1
                        break
    
    topState = ''
    topScore = 0
    for ss in stateSent.iteritems():
        avgScore = 0 if ss[1][1] == 0 else float(ss[1][0]) / ss[1][1]
        if avgScore > topScore:
            topScore = avgScore
            topState = ss[0]
    print topState
if __name__ == '__main__':
    main()
