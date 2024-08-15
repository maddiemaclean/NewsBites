import requests
from datetime import datetime, timedelta, timezone

class story:
    def __init__(self):
        self.title = None
        self.link = None
        self.summary = None
        self.image = None

class categoryHeadlines:
    def __init__(self, topic):
        self.topic = topic
        self.story1 = story()
        self.story2 = story()
        self.story3 = story()


def getHeadlines(api_key, category):
    # Calculate the date range for the last 24 hours
     end_date = datetime.now(timezone.utc)
     start_date = end_date - timedelta(days=1)
     start_date_str = start_date.isoformat()
     end_date_str = end_date.isoformat()
    

     url = 'https://gnews.io/api/v4/top-headlines'
     params = {
         'category': category,
         'from': start_date_str,
         'to': end_date_str,
         'lang': 'en',
         'max': 3,
         'apikey': api_key
     }
    
    # Make the request to the API
     response = requests.get(url, params=params)
    
    # Check if the request was successful
     if response.status_code == 200:
        articles = response.json().get('articles', [])
        
        # Extract relevant information for each article
        topStories = []
        for article in articles:
            topStories.append({
                'title': article.get('title'),
                'link': article.get('url'),
                'image': article.get('image'),
                'description': article.get('description')
            })
        
        return topStories
     else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def break_headlines(headlines, categoryHeadlinesIn):
            categoryHeadlinesIn.story1.title = headlines[0]['title']
            categoryHeadlinesIn.story1.link = headlines[0]['link']
            categoryHeadlinesIn.story1.image = headlines[0]['image']
            categoryHeadlinesIn.story1.summary = headlines[0]['description']
        
            categoryHeadlinesIn.story2.title = headlines[1]['title']
            categoryHeadlinesIn.story2.link = headlines[1]['link']
            categoryHeadlinesIn.story2.image = headlines[1]['image']
            categoryHeadlinesIn.story2.summary = headlines[1]['description']
        
            categoryHeadlinesIn.story3.title = headlines[2]['title']
            categoryHeadlinesIn.story3.link = headlines[2]['link']
            categoryHeadlinesIn.story3.image = headlines[2]['image']
            categoryHeadlinesIn.story3.summary = headlines[2]['description']

# Example usage
api_key = 'c0e2a705b0f759c3d7579496f184927b'

tech = categoryHeadlines('technology')
top_stories = getHeadlines(api_key, tech.topic)
break_headlines(getHeadlines(api_key, tech.topic), tech)
