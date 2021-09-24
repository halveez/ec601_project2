#Zachary Halvorson, Boston University 2021
#EC601 Project 2 Phase 1a


#Following the getting started documentation at:
#https://docs.tweepy.org/en/stable/getting_started.html
#https://github.com/tweepy/tweepy
#Also utilized the tutorial here:
#https://www.geeksforgeeks.org/python-api-user_timeline-in-tweepy/


import tweepy

#Enter credentials here - do not push to GitHub
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
	search_results = api.search(q = search_query, lang = 'en', results_type = 'recent', count = 5, tweet_mode = 'extended')
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


if __name__ == "__main__":
	print("User Tweet Test")
	print_user_tweets("@zach_halvorson")

	print("Current Comments Test - Nick Diaz")
	print_current_comments("Nick Diaz")

	print("Current Comments Test - Robbie Lawler")
	print_current_comments("Robbie Lawler")

	print("Location Trending - New York Test")
	get_trends_by_location(2459115)

	print("Location Trending - Los Angeles Test")
	get_trends_by_location(2442047)

	print("Location Trending - San Francisco Test")
	get_trends_by_location(2487956)
