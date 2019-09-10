class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,title,author,url,name,description,urlToImage,publishedAt,content):
        self.id =id
        self.title = title
        self.author = author
        self.url = url
        self.name = name
        self.description = description
        self.urlToImage =urlToImage
        self.publishedAt =publishedAt
        self.content =content