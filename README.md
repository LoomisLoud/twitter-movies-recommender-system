# Recommending movies from tweets

Wouldn't it be great to be able to recommend movies for every single twitter user ? This is the main goal of the project, we want to be able to ask you for your twitter handle, and if you've sent a few tweets, we should be able to recommend movies for you to watch !

We want to be able to recommend movies related to what you like generally and not forcibly linked to which movies you previously watched.

## Dataset
We use a twitter dataset that EPFL's Data Lab provided coupled with the well known [TMDB Kaggle database](https://www.kaggle.com/tmdb/tmdb-movie-metadata/data). The idea here is to select english tweets rating movies from the dataset, and select the users of these tweets and all their own tweets. This means that we restrain ourselves to the movies rated by users inside the dataset we hold.

## Data Analysis
You can find in the notebook the analysis we made upon the genres of the rated movies, and the contents of the tweets.

We started off by visualizing the movies clustered by genres. As expected, the clusters are defined by a mix of multiple genres, which makes sense since movies are categorized as multiples genres most of the time.

Afterwards, we took our focus to the tweets' contents, performing a topic detection using Latent Dirichlet Allocation. It turns out that the most important topics were the movies ! Which made us think that recommending movies using the tweets themselves as a bag of words might just work !

## Recommender system
Here is how we recommend movies to twitter users. We find the most similar users from our target by cosine distance, and then compute the recommendations by averaging out the ratings of the closest few. To learn more about the technique, read the notebook and the [Medium](https://medium.com/@Loomisloud/recommending-movies-using-twitter-as-a-proxy-6e0cbf50b153) piece ! The idea was to provide a simple proof-of-concept, and not a full blown accurate recommender system, to simply show that it could be done. There are loads of possible improvements to be done.

### DISCLAIMER: TO SEE THE PLOTS EASILY, YOU SHOULD USE THIS [LINK](http://nbviewer.jupyter.org/github/LoomisLoud/ADA/blob/master/project/Twitter%20movie%20recommender%20system.ipynb) INSTEAD OF GITHUB'S VIEWER.
