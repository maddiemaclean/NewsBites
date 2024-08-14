from newsapi import NewsApiClient

class story:
    def __init__(self):
        self.title = None
        self.link = None
        self.summary = None

class categoryHeadlines:
    def __init__(self, topic):
        self.topic = topic
        self.story1 = story()
        self.story2 = story()
        self.story3 = story()

def getHeadlines(api_key,topicIn):
    newsapi = NewsApiClient(api_key=api_key)
    topHeadlines = newsapi.get_top_headlines(
            category= topicIn,
            language='en',
        )
        
    headlines = [(article['title'], article['url']) for article in topHeadlines['articles'][:3]]
    return headlines

def breakHeadlines(headlines,categoryHeadlinesIn):
        categoryHeadlinesIn.story1.title, categoryHeadlinesIn.story1.link = headlines[0]
        categoryHeadlinesIn.story2.title, categoryHeadlinesIn.story2.link = headlines[1]
        categoryHeadlinesIn.story3.title, categoryHeadlinesIn.story3.title = headlines[2]

api_key = "ce2e201a09764e3f85fd47383a347b93"
test = categoryHeadlines("sports")
breakHeadlines(getHeadlines(api_key, test.topic),test)
getHeadlines(api_key, test.topic)
print(test.story1.title)
print(test.story2.link)
