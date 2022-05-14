# NLP tutorial

## Table of contents
1. [May 13th Linguistic Inquiry and Word Count (LIWC)](https://github.com/khyejin1231/Masters-Thesis/blob/main/Tutorial.md#may-13th-linguistic-inquiry-and-word-count-liwc)
2. Google colab Review
3. SHAP and interpretable machine learning
4. BERT Embeddings
5. SVM 
6. Deep learning (Tensorflow, Pytorch with Google Colab pro GPU)
7. [Twarc and Twitter API](https://github.com/khyejin1231/Masters-Thesis/blob/main/Tutorial.md#twarch-and-twitter-api) 
8. [Regex](https://github.com/khyejin1231/Masters-Thesis/blob/main/Tutorial.md#regex-or-pandas)


## May 13th Linguistic Inquiry and Word Count (LIWC)
### Introduction
The main website of LIWC can be found here: https://www.liwc.app/
It says: "LIWC is the gold standard in software for analyzing word use. It can be used to study a
single individual, groups of people over time or all of social media."
You may wonder why we need this tool at all. I think the value of this tool lies on the fact that
it focuses on pyschometric properties. The first line of the LIWC manual says: "The words that
people use in everyday life tell us about their psychological states: their beliefs, emotions, 
thinking habits, lived experiences, social relationships, and personalities." In other words,
"people's words have tremendous psychological value." It fits the goal of NLP.

The price of a 90-day license is $40 which is not too bad. Thank you BDS for your generous scholarship.
I want to make a review of whether it is worth it and what kind of insights it provides.

### How to install:
Installaion process is well explained and you get a separate email on it.

### Manual:
You can find the manual of the software here: https://www.liwc.app/help/psychometrics-manuals
I want to summarize the important points so that I can remember it in due time.
Firstly, there are two versions LIWC-22 and LIWC-15. I decided to use a newer version LIWC-22.
There are multiple modules in LIWC-22, namely, LIWC Analysis, Dictionary workbench, Word frequencies and word clouds
Topic modeling with the meaning extraction method, Narrative arc, Language style matching, Contextualizer, Case studies,
and Prepare transcripts. 
 
The main model is LIWC Analysis. LIWC Analysis uses an internal dictionary which is composed of over
12,000 words, word stems, phrases, and select emoticons. The manual covers how the LIWC-22 Dictionary is developed over time.
The LIWC-22 dictionary is tested on corpus that includes multiple sames of college applications, blogs
conversations, Enron emails, Facebook, movies, novels, NYT, Reddit, short stories, stream of consciousness essays,
U.S Congressional speeches, thematic apperception test, tweets and Yep reviews.

On page 11 of the manual, Table 2. shows the LIWC-22 language dimensions and reliability. 
LIWC-22 language dimensions are the outputs of LIWC Analytics. When you run the software on your data,
you receive a csv file (my input was csv file) of different language dimensions. 
Major categories are summary variables, linguistic dimensions, psychological process and expanded dictionary.

Summary variables include: 
world count, analytical thinking, clout, authentic, emotional tone, words per sentence, big words, dictionary words.

Psychological processes can be interesting to many.
This includes subcategories of drives, cognition, Memory, Affect, Social processes, Social referents.

Expanded dictionary include the followings:
Culture, lifestyle, physical, states, motives, perception, time orientation, conversational.

For internal validity, each subcategories have Cronbach's alpha. 
If you do not know what Cronbach's alpha is, please check [Crocnbach's alpha](https://stats.oarc.ucla.edu/spss/faq/what-does-cronbachs-alpha-mean/#:~:text=Cronbach's%20alpha%20is%20a%20measure,that%20the%20measure%20is%20unidimensional).


### Questions to be answered. 
About preprocessing. emoji, hashtag, etc.
Does BERT contains the information covered in LIWC?

## Twarch and Twitter API


## Regex or Pandas
May 14th
I wanted to cover Regex because I used it in many cases especially when I was searching for rows that contain specific strings.
For example I use Regex to remove certain words in a string or attach strings together.

But I did not know Pandas has a similar function. [Here](https://datatofish.com/substring-pandas-dataframe/) is a link to the website.


