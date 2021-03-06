import random
from newsapi import NewsApiClient

#keyword (string) is the genre of the article, and isTrue (boolean) is whether the article is fake or real
def get_articles(genre, isTrue):
    news_token = open("newstoken.txt").readline().rstrip()
    newsapi = NewsApiClient(api_key=news_token)

    fake_news = 'theonion.com, clickhole.com, thedailymash.co.uk, beforeitsnews.com'
    real_news = 'yahoo.com, huffingtonpost.com, cnn.com, nytimes.com, foxnews.com, nbcnews.com, washingtonpost.com, wsj.com,   bbc.com, usatoday.com, latimes.com'

    sources = ''
    if isTrue:
        sources = real_news
    else:
        sources = fake_news
        
    all_articles = newsapi.get_everything(q=genre, language = 'en', page_size =100, page = 1, domains = sources)
    
    totalNum = all_articles['totalResults']
    
    upperBoundary = 10000
    if(totalNum < upperBoundary):
        upperBoundary = totalNum
    num = random.randint(0, upperBoundary)
    
    page_num = num % 100
    if page_num == 100:
        page_num == 99
    
    all_articles = newsapi.get_everything(q=genre, language = 'en', page_size =100, page = page_num, domains = sources)
    
    item = random.choice(all_articles['articles'])
    
    return(item['url'], item['title'], isTrue)

def fake_news_validate(genre, domain):
    news_token = open("newstoken.txt").readline().rstrip()
    newsapi = NewsApiClient(api_key=news_token)

    if(newsapi.get_everything(q=genre, language = 'en', page_size =100, page = 1, domains = domain)['totalResults'] > 0):
        return True
    else:
        return False 

if __name__ == '__main__':
	print(fake_news_validate('politics', 'newsthump.com'))
    
