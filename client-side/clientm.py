# Twitter Web Services


import tweepy

consumer_key        = "<get_your_own>"
consumer_secret     = "<get_your_own>"
access_token        = "<get_your_own>"
access_secret       = "<get_your_own>"

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

tweets = api.search(q='#python')

# display results to screen
for t in tweets:
    print t.created_at, t.text, "\n"
