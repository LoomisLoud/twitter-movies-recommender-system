# Tweet and Chill

# Abstract
Wouldn't it be great to be able to recommend movies for every single average user of twitter, this is the main goal of the project. We want to be able to ask you for your twitter handle, and if you've sent a few tweets, we should be able to recommend movies for you to watch ! Even more than just recommend movies, we should be able to tell the grand story of movie success, is it possible to predict success for a movie simply from the public's opinion before its premiere ? What about the preference by country ? Is there any movie genre tied to some parts of the world ? Are french people really that romantic ?
We want to be able to tell all of these stories, and to actually do something good, recommend movies related to what you like generally and not forcibly linked to which movies you previously watched.


# Research questions
We want to investigate a few things during the project:
- Can we measure the "hype" around a movie before its release in movie theaters ?
- Is there any way to differentiate "cult" movies from other movies by measuring the way people tweet about them long after they premiered ?
- Can we recommend movies to a twitter user by taking into account only his tweets ?
- Can we predict the ratings of a movie according to how people tweet about it ?
- Do inhabitants from different countries like different types of movies ?


# Dataset
We want to use the twitter dataset you provide coupled with the well known [TMDB Kaggle database](https://www.kaggle.com/tmdb/tmdb-movie-metadata/data). The idea here would be to select english tweets from your dataset, talking about movies, from anywhere. All the same, pick movies from the database that are talked about in the tweets. I do not think that we would need any enrichment yet, maybe by working more on the project we could find some interesting ways to enrich it, but for now it doesn't seem interesting yet.
Since there is not yet any description of the tweets database, what we would expect from it would be, at best, the date, description, user id, and maybe the geolocalisation of each tweet.
As for the Movies dataset, all that we needed was the rating, name an date of each movie, but we have way more than that, we have the whole cast, ratings, number of ratings, genre, budget, language, etc. Having all of that means that we could do way more than just recommending movies, this is what's gotten so excited about it.

# A list of internal milestones up until project milestone 2
We want to create our own subset of the datasets. That is to say:
- choosing only english tweets
- select tweets talking about movies
- select movies discussed on twitter

With these subsets we want to create a training set to have a clearer plan moving forward onto milestone 3.

We then need to build a recommender system around the movies, and perform a sentiment analysis upon the tweets. When done we can checkout how people from twitter would rate the movies and if it correlates with the ratings of the movies dataset. When we take into account the similarities between twitter users' tweets, we should be able to recommend movies for users not even talking about movies, and THAT'S fun.

# Milestone 2
We reached all of our goals for Milestone 2, and even more ! So out of around 9 billion users, about 90000 are rating movies on the IMDB website. In fact we found out that there are a few tweets formatted this way "I rated Invicible 7/10 on #IMDB" which we regarded as tweets from the "share" option of the IMDB website. This has helped us tremendously as it simply means that we can simply parse all of the tweets from spark and only retrieve these ones.

Which is basically what we did. The idea is to look for the specific tweets rating sepcific movies, and pick up all of the users rating movies. Doing so, we get the users interested in movies, and we can start to create a matrix of users interested in movies that will be quite helpful for the recommendation system.

Now looking at our pipeline, we have a few key modules needed to have the final recommender system. First of all we have the vectors computed out of a TFIDF run over our sample of 2 million tweets, that we will easily be able to scale using spark after gathering the users talking about movies. To do so, we already have a function that we can use to filter the tweets using spark, after a few tests, it works flawlessly (see notebook, spark section). Using a cosine similarity, we can compare each new, never seen before twitter user to each other twitter user talking about movies, and figure out to which users the new user is closest. 

The goals of the next milestone are quite obvious, finishing the recommender system will be the highest priority as it will enable us to have a lot of useful dumps out of the 12 billion tweets. Using these new data sources as data enrichments, we will be able to analyze way more stuff, for example the hype around a movie as it is coming out.

The updated pipeline for milestone 3 will be in the notebook.
