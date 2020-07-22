# Modules you will be needing
from textblob import TextBlob
import sys , tweepy
import matplotlib.pyplot as plt

def percentage(part,whole):
    return 100*float(part)/float(whole)

#Api credentials and authentication    

apikey = ""
apisecretkey = "" 
accesstoken = ""
accesstokensecret = ""

auth = tweepy.OAuthHandler(consumer_key=apikey, consumer_secret=apisecretkey)
auth.set_access_token(accesstoken,accesstokensecret)
api  = tweepy.API(auth)

#Asking for keyword specific tweets

searchTerm = input("Enter the keyword :")
noOfSearches = int(input("How many Tweets "))

tweets = tweepy.Cursor(api.search , q = searchTerm).items(noOfSearches)
 
positive = 0
negative = 0
neutral = 0
polarity = 0

#Using text blob and checking for polarity

for tweet in tweets:
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity

    if(analysis.sentiment.polarity == 0):
        neutral += 1
    elif(analysis.sentiment.polarity < 0.00):
        negative += 1    
    elif(analysis.sentiment.polarity > 0.00):
        positive += 1     

positive = percentage(positive,noOfSearches)  
negative = percentage(negative,noOfSearches)  
neutral = percentage(neutral,noOfSearches)  
polarity = percentage(polarity,noOfSearches)  


positive = format(positive,'2f')
negative = format(negative,'2f')
neutral = format(neutral,'2f')

print ("How people are reacting on " + searchTerm + " by analyzing " + str(noOfSearches) + " Tweets")

if (polarity == 0):
    print("neutral")
elif (polarity < 0.00):
    print("negative")

elif (polarity > 0.00):
    print("positive")      

#Plotting a pychart for the results

labels = ['Positive ['+str(positive) + '%]' , 'Neutral ['+str(neutral) + '%]' , 'Negative ['+str(negative) + '%]']   
size = [positive,neutral,negative]
colors = ['yellowgreen', 'gold', 'red']
patches , text = plt.pie(size , colors = colors , startangle = 90)
plt.legend(patches,labels,loc = "best")
plt.title('How people are reacting on ' + searchTerm +  'by analyzing' + str(noOfSearches) + 'Tweets')
plt.axis('equal')
plt.tight_layout()
plt.show()
