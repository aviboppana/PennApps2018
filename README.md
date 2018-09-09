# P.O.I.R.O.T. (Politically Optimized Intelligent Real-Fake Organizing Tool)
**Background**
* What is POIROT?
    * POIROT is a chrome plug in to predict whether a political news article is real or fake. It was developed by Xavier Boudreau, Avi Boppana, and Hari Amoor at PennApps XVIII.


* How accurate is POIROT?
    * POIROT is 88% accurate for a 10-fold cross-validated dataset of 2000 political news articles.


* Where does POIROT's training data come from?
    * We use NEWS API to search for articles by sources known to be credible or false (e.g. BBC is credible, Onion is false). We don't distinguish between satire and non-satire.
    * We use Megan Risdal's data set for more articles known to be false: https://www.kaggle.com/mrisdal/fake-news#fake.csv

    * We use DiffBot API to get the text of an article from a URL
    * Using these methods our training data contains 1000 true articles and 1000 false articles

**Model 1**
79% accuracy

We use Natural Language Tool Kit to consider over 30 features including parts-of-speech, lexical diversity, and punctuation. The features were chosen based on which features were used successfully for classification in existing studies.

We store the processed data (with features) as a Pandas data frame. 

For the first model, we use a stacking classifier combines several classifying methodologies into one pipeline.

The accuracy of this model was calculated by training the model on 80% of the 2000 article data set and testing it on the remaining 20%

**Model 2 (used in production)**
88% accuracy

For preprocessing we removed stop words and capitalization. The input vectors were made with term frequency-inverse document frequency. That is, we weighted words by how often they appeared in the article contrasted to how often they appeared "in the wild".

We used a random forest classifier enhanced by XGBoost. We verified the accuracy of this model by using a 10-fold cross-validation.
