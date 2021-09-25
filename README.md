# ec601_project2

## Phase 1a - I defined three test programs in project2.py:

print_user_tweets() to print a subset of tweets by a specified user.
print_current_comments() to print a recently selected set of tweets given by search string.
get_trends_by_location() to print a list of trends by WOEID location.

get_trends_by_location() can be improved through the use of a Yahoo API look-up search for WOEID locations given the name of the location as WOEID's are not commonly known

## Phase 1b - I defined two additional programs building upon "print_current_comments()" to use Google NLP API's for sentiment analysis and entity analysis on recent tweets by keyword search:

google_nlp_current_sentiment() - returns the sentiment analysis of a recent set of tweets by search string
google_nlp_current_entities() - returns the entity analysis results of a recent set of tweets by search string


## Phase 2:  Build your own social media analyzer
Define MVP and user stories
Translate user stories to a modular design
Who is your user?
What are the basic user stories?




TO-DO:

Error conditions
What happens if twitter is not responding
What happens if I pass the wrong handle
What happens if Google NLP API does not respond back
Data back and forth
What do I send?
What do I get?
What is the format of the data?
How can I use such data?