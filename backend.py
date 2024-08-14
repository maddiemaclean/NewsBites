from newsapi import NewsApiClient

# TO DO: Filter out the description: none result from the top 3 

# Function to get entertainment headlines
def getEntertainmentHeadlines(api_key):
    newsapi = NewsApiClient(api_key=api_key)
    
    top_headlines = newsapi.get_top_headlines(
            category="entertainment",
            language='en',
        )
        
    entertainment_headlines = [(article['title'], article['url']) for article in top_headlines['articles'][:3]]
    
    return entertainment_headlines

# Function to get sports headlines
def getSportsHeadlines(api_key):
    newsapi = NewsApiClient(api_key=api_key)
    
    top_headlines = newsapi.get_top_headlines(
            category="sports",
            language='en',
        )
        
    sports_headlines = [(article['title'], article['url']) for article in top_headlines['articles'][:3]]
    
    return sports_headlines

# Function to print the headlines
def print_headlines(headlines, category):
    print(f"Top 3 {category.capitalize()} Stories:")
    for index, headline in enumerate(headlines, 1):
        print(f"\nStory {index}:")
        print(f"  Title: {headline[0]}")
        print(f"  URL: {headline[1]}")
    print() 

# Main script
api_key = "ce2e201a09764e3f85fd47383a347b93"
entertainment_headlines = getEntertainmentHeadlines(api_key)
sports_headlines = getSportsHeadlines(api_key)

print_headlines(entertainment_headlines, 'entertainment')
print_headlines(sports_headlines, 'sports')
