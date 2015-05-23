from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
        return 'Index Page'

@app.route('/hello')
def hello():
	    return 'Hello-World!!'

#--------------------------------#
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<post_name>')
def show_post(post_name):
    # show the post with the given id, the id is an integer
    return 'Post %s' % post_name

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404
#--------------------------------#


if __name__ == '__main__':
    app.run(debug=True)