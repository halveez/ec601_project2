# EC601 Project 2 and Project 3

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

Building upon the previous phases, I incorporated [The Odds API](https://the-odds-api.com/liveapi/guides/v4/#overview) to pull sports betting odds for MMA fighters, and then incorporated those results into a Google Sentiment Analysis and Twitter Based Tweet search to display alongside the betting lines. This combined access to information will allow sports betters or bookies to more accurately assess public sentiment around bets, and make more informted decisions more rapidly.

get_current_matches() - must be called initially to request the information from Odds API, then storing the information in a JSON file that is saved to prevent repeated API calls

fighter_information_request() - loads the saved data, formats the list of fighters, and presents it to the user for selection from an alphabetized and numbered list, calling other helper functions that follow

fighter_research() - calls google_nlp_current_sentiment() on the fighter's name that was selected by the user, and also validates the selection before calling a printer function to display the betting data

match_printer() - function defined specifically for printing the JSON match data for a specific fight, can later be expanded to print the information in a table format, or other method

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
	2c. Sports betting API's for current lines for the event

3. Results are displayed to the user 

4. (Not in MVP) User inputs a decision to bet, and tool stores that decision

5. (Not in MVP) After the event, the tool compares the user decision to final result of that bet
	5a. Later used for algorithm development, labeled bets with text as inputs for ML model
	
	
### Project 3:

Added PyTest files for unit testing.

