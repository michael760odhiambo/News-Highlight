
from flask import render_template,request,redirect,url_for
from app import app
from .request import get_everything
from .request import get_news,get_news,search_news
from  .models import reviews
from .forms import ReviewForm
Review = reviews.Review

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
     
    
    popular_news = get_everything('business')
    print(popular_news)
    upcoming_news = get_everything('entertainment')
    now_showing_news = get_everything('general')
    from .request import get_news,get_news,search_news

    title = 'Home - Welcome to The best News Review Website Online'

    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('search',news_name=search_news))
    else:
        return render_template('index.html', title = title,popular_news = popular_news,entertainment=upcoming_news,general=now_showing_news,)

@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    #reviews = Review.get_reviews(news.id)
    title = f'{news.title}'
    news = get_news(id)
    return render_template('news.html',id = news_id,news=news,reviews = reviews,title=title)    

@app.route('/search/<news_name>')
def search(news_name):
    '''
    View function to display the search results
    '''
    news_name_list = news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f'search results for {news_name}'
    return render_template('search.html',news = searched_news,title=title) 

@app.route('/news/review/new/<int:id>', methods = ['GET','POST'])
def new_review(id):
    form = ReviewForm()
    news = get_news(id)

    #all_reviews = []

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(news.id,title,news.urlToImage,review)
        new_review.save_review()
        return redirect(url_for('news',id = news.id ))

    title = f'{news.title} review'
    return render_template('new_review.html',title = title, review_form=form, news=news)


        

        