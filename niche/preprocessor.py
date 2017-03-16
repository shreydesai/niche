import os
import re
import copy
import string
import fileinput

MIN_TWEET_LENGTH = 3

def has_retweet(tweet):
    """Determines if tweet is a retweet (RT)

    Args:
        tweet (str): Tweet

    Returns:
        bool: True, if there is a match between the tweet
        and regular expression, otherwise False
    """

    pattern = r'^RT'
    return re.match(pattern, tweet)

def has_mention(tweet):
    """Determines if tweet starts with a mention

    Args:
        tweet (str): Tweet

    Returns:
        bool: True, if there is a match between the tweet
        and regular expression, otherwise False
    """

    pattern = r'^\@[\w\d]+'
    return re.match(pattern, tweet)

def is_link(token):
    """Determines if a token is a link

    Args:
        token (str): Individual word from tweet

    Returns:
        bool: True, if there is a match between the token
        and regular expression, otherwise False
    """

    pattern = r'ht{2}p(s|)\:\/\/(w{3}.|)[\w]+\.[\w]+\/[\w\d]+'
    return re.match(pattern, token)

def is_ascii(token):
    """Determines if a token has acceptable ASCII characters,
    the primary intention is to remove emojis.

    Args:
        token (str): Individual word from tweet

    Returns:
        bool: True, if all characters are ASCII, otherwise False
    """

    printable = set(string.printable)

    for char in token:
        if char not in printable:
            return False

    return True

def preprocess_tweets(read_dir, write_dir, category,
                        blacklist, whitelist, min_tweet_length):
    """Processes the tweets by applying various filters
    and ultimately building the 'processed' corpus.

    Args:
        read_dir (str): Directory to read tweets from
        write_dir (str): Directory to write tweets to
        category (str): Category to process
        blacklist (Set[str]): Set of tokens to exclude
        whitelist (Set[str]): Set of tokens to include
        min_tweet_length: Length processed tweets must meet

    Returns:
        int: Length of processed tweets
    """

    # Keep track of duplicate tweets
    processed_tweets = set()

    for doc in os.listdir(read_dir):
        read_path = os.path.join(read_dir, doc)
        write_path = os.path.join(write_dir, doc)
        f = open(write_path, 'a')

        for line in fileinput.input([read_path]):
            # Apply various filters to the tweet
            tweet = line.rstrip()
            cleaned_tweet = clean_tweet(tweet, blacklist,
                whitelist, min_tweet_length)

            # Add the tweet to the processed corpus if it a) meets the
            # minimum length requirement and b) is not a duplicate
            if cleaned_tweet and cleaned_tweet not in processed_tweets:
                f.write('{}\n'.format(cleaned_tweet))
                processed_tweets.add(cleaned_tweet)

        # Close file stream
        f.close()

    return len(processed_tweets)

def clean_tweet(tweet, blacklist, whitelist, min_tweet_length):
    """Cleans tweet with various filters

    Args:
        tweet (str): Tweet
        blacklist (Set[str]): Set of tokens to exclude
        whitelist (Set[str]): Set of tokens to include
        min_tweet_length (int): Length processed tweets must meet

    Returns:
        str: Tweet with filters applied, or None if the tweet violates
        a filter requirement
    """

    # Exclude retweets or tweets that start with mentions
    if has_retweet(tweet) or has_mention(tweet):
        return None

    # Remove tokens that are in the blacklist, links, or if
    # any of their characters are non-ASCII
    tokens = [w for w in tweet.split()]
    for token in copy.copy(tokens):
        if token in blacklist or is_link(token) or not is_ascii(token):
            tokens.remove(token)

    # Remove extra punctuation from the tweet with the exception
    # of punctuation marks that are whitelisted
    punc = ''.join([p for p in string.punctuation if p not in whitelist])
    tokens = [t.strip(punc).lower() for t in tokens]

    # Return tweets that meet the minimum length requirement or
    # None if they do not
    if len(tokens) >= min_tweet_length:
        return ' '.join(tokens)
    else:
        return None

if __name__ == '__main__':
    categories = ['news', 'entertainment', 'sports', 'fun']
    parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Process tweets from each category
    for category in categories:
        preprocessed = preprocess_tweets(
            read_dir=os.path.join(parent, 'corpus', 'unprocessed', category),
            write_dir=os.path.join(parent, 'corpus', 'processed', category),
            category=category,
            blacklist=set(['&amp;']),
            whitelist=set(['#', '@']),
            min_tweet_length=MIN_TWEET_LENGTH
        )
        print('{} - {}'.format(category, preprocessed))
