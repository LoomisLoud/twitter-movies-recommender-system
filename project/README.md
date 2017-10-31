# Title

# Abstract
A 150 word description of the project idea, goals, dataset used. What story you would like to tell and why? What's the motivation behind your project?
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
Add here a sketch of your planning for the next project milestone.

We want to create our own subset of the datasets. That is to say:
- choosing only english tweets
- select tweets talking about movies
- select movies discussed on twitter

With these subsets we want to create a training set to have a clearer plan moving forward onto milestone 3.

We then need to build a recommender system around the movies, and perform a sentiment analysis upon the tweets. When done we can checkout how people from twitter would rate the movies and if it correlates with the ratings of the movies dataset. When we take into account the similarities between twitter users' tweets, we should be able to recommend movies for users not even talking about movies, and THAT'S fun.

# Questions for TAa
Add here some questions you have for us, in general or project-specific.
- What will be the clear formatting of the twitter dataset ?
- What is the full date range of the twitter dataset ?
- What proportion of the tweets will contain geolocalisation of the tweets ?
- Would you be able to advise us on which metric would be best when comparing tweets after text preprocessing in order to find the closest users for example ?
