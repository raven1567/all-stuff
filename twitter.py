# '''
import json

tweetFile = open("twitterfile.json", "r")

tweetData = json.load(tweetFile)

tweetFile.close()

print("Tweet id: ", tweetData[0]["id"])

print("Tweet text: ", tweetData[0]["text"])


# First ask students how might they use loops
# to print the ["text"] of all the tweets:

# Show them the following two options:

# Explain how here, we're using index and
# counting the number of tweets in the tweetData
# using the python len() function.
# for idx in range(len(tweetData)):
# 	print("Tweet text: " + tweetData[idx]["text"])
#
# # Explain here how Python lets you get objects
# # directly without having to use an index.
# for tweet in tweetData:
# 	print("Tweet text: " + tweet["text"])

# Encourage students to think about how there are
# often multiple solutions for each problem, and
# how each solution might have strenghts and drawbacks.
