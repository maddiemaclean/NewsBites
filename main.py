from backend import story, categoryHeadlines, getHeadlines, break_headlines
from databaseFunctions import getEmailList, addEmail, searchEmails, removeEmail

api_key = 'c0e2a705b0f759c3d7579496f184927b'

tech = categoryHeadlines('technology')
top_stories = getHeadlines(api_key, tech.topic)
break_headlines(getHeadlines(api_key, tech.topic), tech)

business = categoryHeadlines('business')
break_headlines(getHeadlines(api_key, business.topic), business)

general = categoryHeadlines('general')
break_headlines(getHeadlines(api_key, general.topic), general)

world = categoryHeadlines('world')
break_headlines(getHeadlines(api_key, world.topic), world)

nation = categoryHeadlines('nation')
break_headlines(getHeadlines(api_key, nation.topic), nation)