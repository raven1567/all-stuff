import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

tweet_data_polarity = []
tweet_data_subjectivity = []

#Get the JSON data
tweetFile = open("twitterfile.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()


combinedTweets = ""
for tweet in tweetData:
	combinedTweets += tweet['text']
tweetblob = TextBlob(combinedTweets)



wordsToFilter = ["about", "https", "in", "the", "thing", "will", "could"]
filteredDictionary = dict()


for word in tweetblob.words:
        #skip tiny words
    if len(word) < 2:
        continue
        #skip words with random characters or numbers
    if not word.isalpha():
        continue
            #skip words in our filter
    if word.lower() in wordsToFilter:
        continue
                #don't want lower case words smaller than 5 letters
    if len(word) < 5 and word.upper() != word:
        continue;

    filteredDictionary[word.lower()] = tweetblob.word_counts[word.lower()]

                        #Create the word cloud
wordcloud = WordCloud().generate_from_frequencies(filteredDictionary)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()








                        # tb = TextBlob(actual_text)
                        #
                        # polariy = tb.polarity
                        # tweet_data_polarity.append(tb.polarity)
                        # print("Tweet #" + str(counter)+ ": "+ str(tb.polarity))
                        #
                        #
                        # for x in range(len(tweetData)):
                        #     tb = TextBlob(tweetData[x]['text'])
                        #     tweet_data_polarity.append(tb.polarity)
                        #     tweet_data_subjectivity.append(tb.subjectivity)
                        #
                        #
                        #     total = sum(tweet_data_polarity)
                        #     average = total/len(tweet_data_polarity)
                        #     average_str = str(average)
                        #     print("Average polarity:" + " " + average_str)
                        #
                        #     total2 = sum(tweet_data_subjectivity)
                        #     average2 = total2/len(tweet_data_subjectivity)
                        #     average_str2 = str(average2)
                        #     print("Average subjectivity:" + " " + average_str2)
                        #
                        #     #
                        #     # # someList = [0.2, -0.3, -0.4, -1, 1, 0.3, 0.6, 0.2, 0.14, -0.16, -0.18, 0.25]
                        #     # plt.hist(tweet_data_polarity, bins=[-1,-.75,-.5,-.25,0,.25,.5,.75,1])
                        #     # plt.xlabel('Values')
                        #     # plt.ylabel('Number of Items')
                        #     # plt.title('Histogram of Numbers')
                        #     # plt.axis([-1.1, 1.1, 0, 80])
                        #     # plt.grid(True)
                        #     # plt.show()
