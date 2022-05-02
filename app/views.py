from flask import render_template
from app import app

@app.route('/')
def index():
        """
        Render the index page
        """
        return render_template('index.html')
