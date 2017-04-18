import os

from tweepy.api import API
from tweepy.auth import OAuthHandler

f = open('dev_keys.txt', 'r')
API_KEY = f.readline().strip()
API_SECRET = f.readline().strip()
ACCESS_TOKEN = f.readline().strip()
ACCESS_TOKEN_SECRET = f.readline().strip()

USER_LIMIT = 5
MAX_TWEET_COUNT = 200

def parse_users(read_dir, category, limit):
    """Builds list of users to retrieve tweets from
    the category specified.

    Args:
        read_dir (str): Directory to read users from
        category (str): Category the user belongs to
        limit (int): Number of users to parse

    Returns:
        List[str]: Users to retrieve tweets from
    """

    try:
        f = open(read_dir + '/{}.txt'.format(category), 'r')
    except IOError as e:
        print('File does not exist')

    users = [x.strip() for x in f.read().split()]

    if limit:
        return users[:limit]
    else:
        return users

def get_tweets(api, screen_name, count):
    """Downloads approx 3000 tweets from the user.

    Args:
        api (obj): Tweepy API object
        screen_name (str): Twitter username
        count: Number of tweets to download at once

    Returns:
        List[str]: Tweets retrieved from the user
    """

    tweets, new_tweets = [], api.user_timeline(
        screen_name=screen_name,
        count=count
    )
    tweets.extend(new_tweets)

    oldest_tweet_id = tweets[-1].id - 1

    while len(new_tweets):
        new_tweets = api.user_timeline(
            screen_name=screen_name,
            count=count,
            max_id=oldest_tweet_id
        )
        tweets.extend(new_tweets)
        oldest_tweet_id = tweets[-1].id - 1

    return [tweet.text for tweet in tweets]

if __name__ == '__main__':
    parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    categories = ['entertainment', 'sports', 'fun', 'games',
                    'weather', 'politics', 'science', 'technology']
    # Set up Tweepy API object
    auth = OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = API(
        auth_handler=auth,
        wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True
    )

    for category in categories:
        print('Downloading {}'.format(category))
        category_count = 0

        # Get list of users from each category
        users = parse_users(
            read_dir=os.path.join(parent, 'corpus', 'users'),
            category=category,
            limit=USER_LIMIT
        )

        # Retrieve tweets from each user in the category
        for user in users:
            write_dir = os.path.join(parent, 'corpus', 'unprocessed', category)
            f = open(write_dir + '/{}.txt'.format(user), 'a')

            tweets = get_tweets(
                api=api,
                screen_name=user,
                count=MAX_TWEET_COUNT
            )
            print(' ' * 2, '{} - {}'.format(user, len(tweets)))
            category_count += len(tweets)

            # Condense the tweet to one line (removes multiple lines)
            # and write to the 'unprocessed' directory
            if tweets:
                for tweet in tweets:
                    tweet = ' '.join(tweet.split())
                    f.write('{}\n'.format(tweet))

            f.close()

        print(' ' * 2, '* {} total tweets'.format(category_count))
