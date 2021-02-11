from flask import Flask, render_template, url_for
application = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@application.route("/")
@application.route("/home")
def home():
    return render_template('home.html', posts=posts)


@application.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    application.run(debug=True)
