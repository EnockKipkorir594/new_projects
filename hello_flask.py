from flask import Flask, render_template


app = Flask(__name__)
posts = [
    {
        'id':'1',
        'title':'My first post',
        'author':'Enock',
        'post':'This is my first flask web. This is my first blog post inside the web'
    },
    {
        'id':'2',
        'title':'My second post',
        'author':'Kipkorir',
        'post':'This is my second blog post inside the web.I enjoy using flask '
    }
]

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return "<h2>About page</h2><p>Thia is a simple flask app .</p>"


if __name__ == '__main__':
   
    app.run(debug = True)