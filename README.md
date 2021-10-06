# EC601 Project 2

## Phase 1a - I defined three test programs in project2.py:

print_user_tweets() to print a subset of tweets by a specified user.
print_current_comments() to print a recently selected set of tweets given by search string.
get_trends_by_location() to print a list of trends by WOEID location.

get_trends_by_location() can be improved through the use of a Yahoo API look-up search for WOEID locations given the name of the location as WOEID's are not commonly known

## Phase 1b - I defined two additional programs:

Building upon "print_current_comments()", I incorporated Google NLP API's for sentiment analysis and entity analysis on recent tweets by keyword search:

google_nlp_current_sentiment() - returns the sentiment analysis of a recent set of tweets by search string
google_nlp_current_entities() - returns the entity analysis results of a recent set of tweets by search string


## Phase 2:  Build your own social media analyzer


### User Story:

As a sports gambler, I want relevant information to specific sports events so that I can make more informed bets and improve my winning percentage.

As a bookie, I want relevant information to specific sports events so that I can more effectively set odds and ensure that my books are properly balanced.


### Minimum Viable Product:

This tool is for US based sports gamblers and bookies to view real-time sentiment analysis trends of specific events and their betting lines, focusing initially on combat sports (boxing, MMA, muay thai, etc.).


### Modular Design:

1. User queries specific events from a pre-set list (Or inputs a custom query that is then parsed)

2. Selection is processed and API's are called:
	2a. Twitter for real time text related to query
	2b. Google NLP on Twitter content for sentiment analysis
	2c. Multiple sports betting API's for current lines for the event
	2d. Possibly: Query news stories and articles for text analysis as well

3. Results are displayed to the user 

4. User inputs a decision to bet, and tool stores that decision

5. After the event, the tool compares the user decision to final result of that bet
	5a. Later used for algorithm development, labeled bets with text as inputs for ML model



## TO-DO:

Error conditions
What happens if twitter is not responding
What happens if I pass the wrong handle
What happens if Google NLP API does not respond back
Data back and forth
What do I send?
What do I get?
What is the format of the data?
How can I use such data?
