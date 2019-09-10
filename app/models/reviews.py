class Review:

    all_reviews = []

    def __init__(self,news_id,title,urlToImage,description):
        self.news_id = news_id
        self.title = title
        self.urlToImage = urlToImage
        self.description = description


    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()