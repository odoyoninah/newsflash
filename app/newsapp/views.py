from flask import render_template
from . import newsapp
from ..request import get_news

@newsapp.route('/')
def index():
    
    """
    View root page function that returns the index page and its data
    """

    news = get_news()
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title = title, news = news)
    