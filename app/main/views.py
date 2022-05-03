from flask import render_template

from app import main
from . import main
from ..request import get_news

@main.route('/')
def index():
    
    """
    View root page function that returns the index page and its data
    """

    news = get_news("trending")
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title = title, news = news)


    