
import urllib.request,json
from .models import News


# Getting api key
api_key = None
# Getting the news base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config["NEWS_API_BASE_URL"]

def get_everything(everything):
    '''
    Function that gets the json response to our url request
    '''
    get_everything_url = base_url.format(everything,api_key)

    with urllib.request.urlopen(get_everything_url) as url:
        get_everything_data = url.read()
        get_everything_response = json.loads(get_everything_data)

        everything_results = None

        if get_everything_response['articles']:
            everything_results_list = get_everything_response['articles']
            everything_results = process_results(everything_results_list)


    return everything_results

def process_results(everything_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        everything_list: A list of dictionaries that contain news details

    Returns :
        everything_results: A list of news objects
    '''
    everything_results = []
    for everything_item in everything_list:
        id = everything_item.get('id')
        title = everything_item.get('title')
        author = everything_item.get('author')
        url = everything_item.get('url')
        name = everything_item.get('name')
        description = everything_item.get('description')
        urlToImage = everything_item.get('urlToImage')
        publishedAt = everything_item.get('publishedAt')
        content = everything_item.get('content')
        
        
        everything_object = News(id,title,author,url,name,description,urlToImage,publishedAt,content)
        everything_results.append(everything_object)

    return everything_results

def get_news(id):
    get_news_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
            id = news_details_response.get('id')
            title = news_details_response.get('title')
            url = news_details_response.get('url')
            name = news_details_response.get('name')
            description = news_details_response.get('description')
            urlToImage = news_details_response.get('urlToImage')
            author = news_details_response.get('author')
            publishedAt = news_details_response.get('publishedAt')
            content = news_details_response.get('content')

            news_object = News(id,title,author,url,name,description,urlToImage,publishedAt,content)

    return news_object    

def search_news(news_name):
    search_news_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(news_name,api_key)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_articles = None

        if search_news_response['articles']:
            search_news_list = search_news_response['articles']
            search_news_articles = process_results(search_news_list)


    return search_news_articles