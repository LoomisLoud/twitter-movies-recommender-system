# This codes cleans out the text features and
# computes bigrams and trigrams for them
from operator import add
from pyspark.ml.feature import NGram, StopWordsRemover
from pyspark.sql import SQLContext
from pyspark.sql.functions import udf
from pyspark.sql.types import ArrayType, StringType
from pyspark import SparkConf, SparkContext
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

conf = SparkConf().setAppName("Computing ngrams for a few million tweets")
sc = SparkContext(conf=conf)
spark = SQLContext(sc)

dd = sc.textFile('preprocessed_tweets.csv').map(lambda x: x.split(',', 1)).map(lambda x: (x[0], x[1].split()))
df = dd.toDF(['username', 'tweets'])

def remove_l_c_words(df, least, most):
  # Let's find out which words we keep
  vocabulary = df.map(lambda row: row.tweets).reduce(lambda x,y: x+y)
  count = sc.parallelize(vocabulary).map(lambda word: (word, 1)).reduceByKey(add)
  count = count.sortBy(lambda wc: wc[1], ascending=False)
  # Add to the list of stopwords
  stop_words_lc = count.filter(lambda wc: wc[1] == least).map(lambda wc: wc[0]).collect()
  if most < 1:
    stop_words = stop_words_lc
  else:
    stop_words_mc = count.map(lambda wc: wc[0]).take(most)
    stop_words = stop_words_lc + stop_words_mc
  remover = StopWordsRemover(inputCol="tweets", outputCol='cleaned_tweets', stopWords=stop_words)
  return remover.transform(df)

df = remove_l_c_words(df, least=1, most=50)
# Let's create the bigrams and trigrams
bigrams = NGram(n=2, inputCol='cleaned_tweets', outputCol='bigrams')
trigrams = NGram(n=3, inputCol='cleaned_tweets', outputCol='trigrams')
df = bigrams.transform(df)
ngramDF = trigrams.transform(df)
def add_col(x, y, z):
  return x + y + z

udf_concat = udf(add_col, ArrayType(StringType()))
final_df = ngramDF.withColumn("total", udf_concat("cleaned_tweets", "bigrams", "trigrams")).select('username', 'total').toDF('username', 'tweets')
df_to_save = remove_l_c_words(final_df, least=1, most=0).select('username', 'cleaned_tweets').rdd
df_to_save = df_to_save.map(lambda row: (row.username, ",".join(row.cleaned_tweets)))
df_to_save.map(lambda x: "|".join(x)).saveAsTextFile('ngrams_tweets')
