#Zachary Halvorson, Boston University 2021
#EC601 Project 2 Final

#Following the getting started documentation at:
#https://docs.tweepy.org/en/stable/getting_started.html
#https://github.com/tweepy/tweepy
#Also utilized the tutorial here:
#https://www.geeksforgeeks.org/python-api-user_timeline-in-tweepy/
#For Google-NLP, used the following resources:
#https://cloud.google.com/natural-language/docs/reference/libraries?hl=en_US#client-libraries-install-python
#https://stackoverflow.com/questions/45501082/set-google-application-credentials-in-python-project-to-use-google-api
#https://googleapis.dev/python/language/latest/usage.html

#Following the guide below, I utilized "Odds-API" to pull live sports betting odds for specific events
#https://the-odds-api.com/liveapi/guides/v4/#parameters
import json
import requests
import argparse

import sys

API_KEY = ''
SPORT = 'mma_mixed_martial_arts'
REGIONS = 'us' # uk | us | eu | au
MARKETS  = 'h2h,spreads,totals' # h2h | spreads | totals
ODDS_FORMAT = 'decimal' # decimal | american
DATE_FORMAT = 'iso' # iso | unix

import tweepy

# Imports the Google Cloud client library
from google.cloud import language_v1
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=""

# Instantiates a Google client
client = language_v1.LanguageServiceClient()


#Enter Twitter credentials here - do not push to GitHub
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def print_user_tweets(user_name):
	#Example to pull tweets of a specific user (myself as default)
	user_tweets = api.user_timeline(user_name, count = 5, tweet_mode = 'extended')
	for tweet in user_tweets:
		print(tweet.user.name)
		print(tweet.full_text)
		print('')

def print_current_comments(search_query):
	#Example to search for a specific hashtag, excluding retweets
	search_results = api.search(q = search_query, lang = 'en', results_type = 'recent', count = 50, tweet_mode = 'extended')
	for result in search_results:
		if ("RT @" not in result.full_text):
			print(result.user.screen_name)
			print(result.user.created_at)
			print(result.full_text)
			print('')

def get_trends_by_location(location_of_interest):
	#Example to print Twitter trends by geolocation - selecting the first 10
	location_trends = api.trends_place(location_of_interest)
	for trend in location_trends[0]["trends"][:10]:
		print(trend["name"])

def google_nlp_current_sentiment(search_query):
	#Example to search for a specific hashtag, excluding retweets
	search_results = api.search(q = search_query, lang = 'en', results_type = 'recent', count = 10, tweet_mode = 'extended')
	for result in search_results:
		if ("RT @" not in result.full_text):
			text = result.full_text
			document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
			sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
			print("Text: {}".format(text))
			print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))

def google_nlp_current_entities(search_query):
	#Example to search for a specific hashtag, excluding retweets
	search_results = api.search(q = search_query, lang = 'en', results_type = 'recent', count = 10, tweet_mode = 'extended')
	for result in search_results:
		if ("RT @" not in result.full_text):
			text = result.full_text
			document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
			response = client.analyze_entities(request = {'document': document})
			for entity in response.entities:
				print('=' * 20)
				print('         name: {0}'.format(entity.name))
				print('     metadata: {0}'.format(entity.metadata))
				print('     salience: {0}'.format(entity.salience))

def get_current_matches():
	# Pulled from https://github.com/the-odds-api/samples-python/blob/master/sample-v4.py
	odds_response = requests.get(f'https://api.the-odds-api.com/v4/sports/{SPORT}/odds', params={
    	'api_key': API_KEY,
    	'regions': REGIONS,
    	'markets': MARKETS,
    	'oddsFormat': ODDS_FORMAT,
    	'dateFormat': DATE_FORMAT,
	})

	if odds_response.status_code != 200:
	    print(f'Failed to get odds: status_code {odds_response.status_code}, response body {odds_response.text}')
	    return
	else:
	    print("Odds API Call Succeeded", file=sys.stderr)
	    odds_json = odds_response.json()
	    print('Number of events:', len(odds_json))
	    print(odds_json)

	    # Check the usage quota
	    print('Remaining requests', odds_response.headers['x-requests-remaining'])
	    print('Used requests', odds_response.headers['x-requests-used'])

	# Save the data to reduce API requests during testing
	with open('data.json', 'w') as f:
		json.dump(odds_json, f)

def fighter_information_request():
	fighter_list = []

	with open('data.json') as f:
		d = json.load(f)

	for match in d:
		fighter_list.append(match["home_team"])
		fighter_list.append(match["away_team"])

	# Sort alphabetically and print with numbers for user selection
	fighter_list.sort()
	for i in range(1, len(fighter_list)):
		print(str(i) + '. ' + fighter_list[i])

	# Validate number selected from range
	print("Please select a fighter for further analysis:")
	fighter_selection = int(input())
	if (fighter_selection in range(1, len(fighter_list))):
		# Calls other functions
		fighter_research(fighter_list[fighter_selection], d, fighter_list)
	else:
		print("Invalid user input", file=sys.stderr)
		print("Invalid user input")

def fighter_research(fighter_name, saved_bets, fighter_list):

	print(fighter_name)
	# Google Sentiment Analysis on Twitter comments 
	print("Google Sentiment Analysis on Twitter Tweets from Fighter Name Selection")
	google_nlp_current_sentiment(fighter_name)

	# Formatting and displaying of betting odds for specific fighter
	for match in saved_bets:
		if (match["home_team"] == fighter_name):
			match_printer(match, fighter_name)
		elif (match["away_team"] == fighter_name):
			match_printer(match, fighter_name)

def match_printer(match, fighter_name):
	print("Bettings Odds for " + fighter_name)
	print(json.dumps(match, indent=2))


if __name__ == "__main__":
	# print("User Tweet Test")
	# print_user_tweets("@zach_halvorson")

	# print("Current Comments Test - Nick Diaz")
	# print_current_comments("Nick Diaz")

	# print("Current Comments Test - Robbie Lawler")
	# print_current_comments("Robbie Lawler")

	# print("Location Trending - New York Test")
	# get_trends_by_location(2459115)

	# print("Location Trending - Los Angeles Test")
	# get_trends_by_location(2442047)

	# print("Location Trending - San Francisco Test")
	# get_trends_by_location(2487956)

	# print("Sentiment Analysis - Nick Diaz Tweets")
	# google_nlp_current_sentiment("Nick Diaz")

	# print("Sentiment Analysis - Robbie Lawler Tweets")
	# google_nlp_current_sentiment("Robbie Lawler")

	# print("Entity Analysis - Nick Diaz Tweets")
	# google_nlp_current_entities("Nick Diaz")

	# print("Entity Analysis - Robbie Lawler Tweets")
	# google_nlp_current_entities("Robbie Lawler")

	# When running for the first time, call get_current_matches() to get the most current list of upcoming fights and fighters from Odds-API

	# After calling get_current_matches(), call fighter_information_request to use the saved JSON from the first call to avoid unecessary API calls.

	# print("Odds-API")
	# get_current_matches()

	# print("Saved Odds-API")
	# fighter_information_request()

	print("Hello World!")