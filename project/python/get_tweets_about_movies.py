# language, id, date, user_id, tweet
from pyspark import SparkConf, SparkContext
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

conf = SparkConf().setAppName("Retrieving user-tweets tuples")
sc = SparkContext(conf=conf)

tweets = sc.textFile("/datasets/tweets-leon")
good_tweets = tweets.map(lambda s: tuple(s.split('\t'))).filter(lambda s: s[0] == 'en')

# There are 12 488 903 101 tweets in english, in the dataset

def users_talking_about_movies(row):
    """
    This function is used to filter out tweets based on if they rate
    an IMDB movie or not.
    Returns a True or False depending on wether they rate a movie.
    """
    if len(row) < 5:
        return None
    if "imdb" in row[4].lower() and "i rated" in row[4].lower():
        return row[3]
    return None

# There are 21 426 users talking about movies in the whole dataset, it's fine to collect 21 426 objects
user_about_movies = good_tweets.map(lambda x: users_talking_about_movies(x)).distinct().collect()
user_as_key = good_tweets.filter(lambda x: len(x) == 5).map(lambda x: (x[3],[x[4]])).filter(lambda x: x[0] in user_about_movies)
# We reduce them by username, and combine their tweets altogether
tweets_list_u_m = user_as_key.reduceByKey(lambda a, b: a + b)
tweets_csv_format_u_m = tweets_list_u_m.mapValues(lambda v: "\t".join(v)).map(lambda x: "|".join(x))

# Saving them to hdfs
tweets_csv_format_u_m.saveAsTextFile('rating_users_tweets')
